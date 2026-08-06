# bot_sales.py - ربات فروش کانفیگ Purple-Panel
# 🟣 Customized by @AghaBanafshi

import asyncio
import os
import re
import secrets
from datetime import datetime, timedelta
from typing import Optional

import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, MessageHandler,
    filters, ConversationHandler, ContextTypes
)

# ── تنظیمات ──
TOKEN = os.environ.get("SALES_BOT_TOKEN", "").strip()
ADMIN_IDS = {int(x) for x in os.environ.get("SALES_ADMIN_IDS", "").replace(" ", "").split(",") if x.isdigit()}
CARD_NUMBER = os.environ.get("SALES_CARD_NUMBER", "").strip()
CARD_HOLDER = os.environ.get("SALES_CARD_HOLDER", "Purple-Panel").strip()
PANEL_URL = os.environ.get("PANEL_URL", "").strip()
PANEL_PASSWORD = os.environ.get("ADMIN_PASSWORD", "PurplePanel").strip()
PRICE = int(os.environ.get("SALES_PRICE", 50_000))  # تومان
CONFIG_NAME = os.environ.get("SALES_CONFIG_NAME", "کانفیگ ۱۰ گیگ ۳۰ روزه")
LIMIT_GB = int(os.environ.get("SALES_LIMIT_GB", 10))
EXPIRY_DAYS = int(os.environ.get("SALES_EXPIRY_DAYS", 30))

# ── وضعیت‌ها ──
(WAITING_FOR_PAYMENT, WAITING_FOR_CONFIG_NAME) = range(2)

# ── دیتا در حافظه (با ری‌استارت پاک میشه) ──
pending_payments: dict = {}  # user_id -> {"config_name": str, "amount": int, "date": str}
user_sessions: dict = {}  # user_id -> {"step": str, "data": {}}

# ── کیبورد شیشه‌ای ──
def glass_keyboard(buttons: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in buttons:
        keyboard.append([InlineKeyboardButton(row["text"], callback_data=row["callback"])])
    return InlineKeyboardMarkup(keyboard)

MAIN_MENU = glass_keyboard([
    {"text": "🟣 خرید کانفیگ", "callback": "buy"},
    {"text": "❓ راهنما", "callback": "help"},
    {"text": "📞 پشتیبانی", "callback": "support"},
])

def config_name_keyboard():
    return glass_keyboard([
        {"text": "🟣 کانفیگ ۱۰ گیگ / ۳۰ روز", "callback": f"config_{LIMIT_GB}GB_{EXPIRY_DAYS}d"},
        {"text": "✏️ سفارشی", "callback": "config_custom"},
        {"text": "🔙 بازگشت", "callback": "back"},
    ])

# ── Helper: ارسال پیام به ادمین ──
async def notify_admin(context: ContextTypes.DEFAULT_TYPE, text: str, keyboard: Optional[InlineKeyboardMarkup] = None):
    for admin_id in ADMIN_IDS:
        try:
            await context.bot.send_message(
                chat_id=admin_id,
                text=text,
                parse_mode="HTML",
                reply_markup=keyboard
            )
        except Exception:
            pass

# ── Helper: ساخت کانفیگ از طریق API پنل ──
async def create_config_via_panel(label: str, limit_gb: int, expiry_days: int) -> Optional[dict]:
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            # ۱. لاگین به پنل
            login_resp = await client.post(
                f"{PANEL_URL}/api/login",
                json={"password": PANEL_PASSWORD}
            )
            if login_resp.status_code != 200:
                return None
            session_token = login_resp.cookies.get("pp_session") or login_resp.cookies.get("session")
            headers = {"Cookie": f"pp_session={session_token}"}

            # ۲. ساخت کانفیگ
            payload = {
                "label": label,
                "limit_value": limit_gb,
                "limit_unit": "GB",
                "expires_days": expiry_days,
                "protocol": "vless-ws",
                "fingerprint": "chrome",
                "note": f"فروخته شده از ربات - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            }
            resp = await client.post(
                f"{PANEL_URL}/api/links",
                json=payload,
                headers=headers
            )
            if resp.status_code != 200:
                return None
            data = resp.json()
            return {
                "uuid": data.get("uuid"),
                "link": data.get("vless_link"),
                "label": data.get("label"),
                "sub_url": data.get("sub_url"),
            }
        except Exception as e:
            print(f"Error creating config: {e}")
            return None

# ── دستور /start ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = (
        f"🟣 <b>به ربات فروش Purple-Panel خوش اومدی!</b>\n\n"
        f"👤 کاربر: {user.first_name}\n"
        f"🆔 آیدی: {user.id}\n\n"
        f"📦 هر کانفیگ شامل:\n"
        f"• {LIMIT_GB} گیگابایت ترافیک\n"
        f"• {EXPIRY_DAYS} روز اعتبار\n"
        f"• قیمت: {PRICE:,} تومان\n\n"
        f"برای خرید، دکمه زیر رو بزن. 👇"
    )
    await update.message.reply_text(msg, parse_mode="HTML", reply_markup=MAIN_MENU)

# ── کالبک‌ها ──
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "buy":
        await query.edit_message_text(
            "🟣 <b>انتخاب کانفیگ</b>\n\n"
            "نوع کانفیگ مورد نظرت رو انتخاب کن:",
            parse_mode="HTML",
            reply_markup=config_name_keyboard()
        )

    elif data.startswith("config_"):
        parts = data.split("_")
        if parts[1] == "custom":
            user_sessions[user_id] = {"step": "waiting_custom_name"}
            await query.edit_message_text(
                "✏️ <b>نام کانفیگ</b>\n\n"
                "لطفاً نام دلخواه برای کانفیگت رو بفرست (مثلاً: کانفیگ علی):",
                parse_mode="HTML"
            )
            return

        limit_gb = int(parts[1].replace("GB", ""))
        expiry_days = int(parts[2].replace("d", ""))
        context.user_data["config_limit"] = limit_gb
        context.user_data["config_expiry"] = expiry_days

        await show_payment_info(query, user_id, limit_gb, expiry_days)

    elif data == "back":
        await query.edit_message_text(
            "🟣 <b>منوی اصلی</b>\n\n"
            "از دکمه‌های زیر استفاده کن:",
            parse_mode="HTML",
            reply_markup=MAIN_MENU
        )

    elif data == "help":
        await query.edit_message_text(
            "❓ <b>راهنما</b>\n\n"
            "۱. دکمه <b>خرید کانفیگ</b> رو بزن\n"
            "۲. کانفیگ مورد نظرت رو انتخاب کن\n"
            "۳. به شماره کارت مشخص‌شده واریز کن\n"
            "۴. رسید واریز رو تایید کن\n"
            "۵. منتظر تایید ادمین باش\n"
            "۶. لینک کانفیگ رو دریافت کن\n\n"
            f"💰 قیمت هر کانفیگ: {PRICE:,} تومان\n"
            f"📦 {LIMIT_GB} گیگ / {EXPIRY_DAYS} روز",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="back")]])
        )

    elif data == "support":
        await query.edit_message_text(
            "📞 <b>پشتیبانی</b>\n\n"
            "برای ارتباط با پشتیبانی، از لینک زیر استفاده کن:\n\n"
            "🟣 <a href='https://t.me/AghaBanafshiipvbot'>@AghaBanafshiipvbot</a>\n\n"
            "یا به ادمین پیام بده:",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 پیام به ادمین", url="https://t.me/AghaBanafshi")],
                [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
            ])
        )

    elif data.startswith("confirm_payment_"):
        # تایید واریز توسط ادمین
        payment_id = data.replace("confirm_payment_", "")
        if payment_id not in pending_payments:
            await query.edit_message_text("❌ این درخواست قبلاً تایید یا لغو شده.")
            return

        payment = pending_payments[payment_id]
        user_id_pay = payment["user_id"]
        config_name = payment["config_name"]
        limit_gb = payment["limit_gb"]
        expiry_days = payment["expiry_days"]

        # ساخت کانفیگ
        result = await create_config_via_panel(
            label=config_name,
            limit_gb=limit_gb,
            expiry_days=expiry_days
        )

        if result:
            # ارسال لینک به کاربر
            try:
                await context.bot.send_message(
                    chat_id=user_id_pay,
                    text=(
                        f"✅ <b>کانفیگ شما ساخته شد!</b>\n\n"
                        f"📌 <b>نام:</b> {result['label']}\n"
                        f"🔗 <b>لینک:</b> <code>{result['link']}</code>\n\n"
                        f"📱 <b>Sub URL:</b> <code>{result['sub_url']}</code>\n\n"
                        f"🟣 توی <a href='{PANEL_URL}/dashboard'>پنل</a> هم میتونی مدیریتش کنی."
                    ),
                    parse_mode="HTML"
                )
            except Exception:
                pass

            await query.edit_message_text(
                f"✅ <b>کانفیگ کاربر با موفقیت ساخته شد!</b>\n\n"
                f"👤 کاربر: {user_id_pay}\n"
                f"📌 نام: {config_name}\n"
                f"📦 سهمیه: {limit_gb} GB\n"
                f"📅 انقضا: {expiry_days} روز",
                parse_mode="HTML"
            )
        else:
            await query.edit_message_text(
                "❌ <b>خطا در ساخت کانفیگ!</b>\n"
                "لطفاً پنل رو چک کن.",
                parse_mode="HTML"
            )

        del pending_payments[payment_id]

    elif data == "payment_received":
        # کاربر رسید رو تایید کرده
        if user_id in pending_payments:
            payment = pending_payments[user_id]
            # به ادمین اطلاع بده
            await notify_admin(
                context,
                f"💳 <b>واریز جدید</b>\n\n"
                f"👤 کاربر: {payment['user_id']}\n"
                f"📌 کانفیگ: {payment['config_name']}\n"
                f"💰 مبلغ: {PRICE:,} تومان\n"
                f"📅 تاریخ: {payment['date']}\n\n"
                f"لطفاً رسید رو بررسی و تایید کن.",
                keyboard=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ تایید و ساخت کانفیگ", callback_data=f"confirm_payment_{payment['user_id']}_{payment['date']}")],
                    [InlineKeyboardButton("❌ لغو", callback_data=f"cancel_payment_{payment['user_id']}")]
                ])
            )
            await query.edit_message_text(
                "✅ <b>رسید شما ثبت شد!</b>\n\n"
                "به زودی توسط ادمین بررسی و تایید میشه.\n"
                "لطفاً صبور باش! 🟣",
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 منوی اصلی", callback_data="back")]])
            )

async def show_payment_info(query, user_id, limit_gb, expiry_days):
    msg = (
        f"💳 <b>اطلاعات واریز</b>\n\n"
        f"📦 <b>کانفیگ:</b> {limit_gb} گیگ / {expiry_days} روز\n"
        f"💰 <b>مبلغ:</b> {PRICE:,} تومان\n\n"
        f"🏦 <b>شماره کارت:</b>\n"
        f"<code>{CARD_NUMBER}</code>\n"
        f"👤 <b>به نام:</b> {CARD_HOLDER}\n\n"
        f"📌 <b>مراحل:</b>\n"
        f"۱. مبلغ رو به کارت بالا واریز کن\n"
        f"۲. بعد از واریز، دکمه <b>رسید واریز</b> رو بزن\n\n"
        f"⚠️ حتماً شماره رسید رو یادداشت کن!"
    )
    await query.edit_message_text(
        msg,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ رسید واریز", callback_data="payment_received")],
            [InlineKeyboardButton("🔙 انصراف", callback_data="back")]
        ])
    )
    # ذخیره اطلاعات پرداخت
    pending_payments[user_id] = {
        "user_id": user_id,
        "config_name": f"{limit_gb}GB-{expiry_days}D",
        "limit_gb": limit_gb,
        "expiry_days": expiry_days,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

# ── پیام‌های متنی ──
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id in user_sessions and user_sessions[user_id].get("step") == "waiting_custom_name":
        config_name = text.strip()[:50] or "کانفیگ سفارشی"
        limit_gb = LIMIT_GB
        expiry_days = EXPIRY_DAYS
        context.user_data["config_limit"] = limit_gb
        context.user_data["config_expiry"] = expiry_days
        del user_sessions[user_id]

        # ذخیره اطلاعات پرداخت
        pending_payments[user_id] = {
            "user_id": user_id,
            "config_name": config_name,
            "limit_gb": limit_gb,
            "expiry_days": expiry_days,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        msg = (
            f"✅ <b>نام کانفیگ ذخیره شد:</b> {config_name}\n\n"
            f"💳 <b>اطلاعات واریز</b>\n\n"
            f"📦 <b>کانفیگ:</b> {limit_gb} گیگ / {expiry_days} روز\n"
            f"💰 <b>مبلغ:</b> {PRICE:,} تومان\n\n"
            f"🏦 <b>شماره کارت:</b>\n"
            f"<code>{CARD_NUMBER}</code>\n"
            f"👤 <b>به نام:</b> {CARD_HOLDER}\n\n"
            f"📌 بعد از واریز، دکمه <b>رسید واریز</b> رو بزن."
        )
        await update.message.reply_text(
            msg,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ رسید واریز", callback_data="payment_received")],
                [InlineKeyboardButton("🔙 انصراف", callback_data="back")]
            ])
        )
        return

# ── راه‌اندازی ──
async def run_bot():
    if not TOKEN:
        print("❌ SALES_BOT_TOKEN تنظیم نشده!")
        return
    if not ADMIN_IDS:
        print("⚠️ SALES_ADMIN_IDS تنظیم نشده!")
    if not CARD_NUMBER:
        print("⚠️ SALES_CARD_NUMBER تنظیم نشده!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("🟣 ربات فروش Purple-Panel روشن شد!")
    await app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    asyncio.run(run_bot())

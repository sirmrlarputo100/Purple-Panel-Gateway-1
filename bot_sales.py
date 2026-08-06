# bot_sales.py - Purple-Panel Sales Bot v1.0
# tg
# Compatible with python-telegram-bot==13.7

import os
import asyncio
import re
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, MessageHandler,
    Filters, ConversationHandler, ContextTypes
)

# ── تنظیمات از متغیرهای محیطی ──
TOKEN = os.environ.get("SALES_BOT_TOKEN", "").strip()
ADMIN_IDS = {int(x) for x in os.environ.get("SALES_ADMIN_IDS", "").replace(" ", "").split(",") if x.isdigit()}
CARD_NUMBER = os.environ.get("SALES_CARD_NUMBER", "").strip()
CARD_HOLDER = os.environ.get("SALES_CARD_HOLDER", "Purple-Panel").strip()
PANEL_URL = os.environ.get("PANEL_URL", "").strip()
PANEL_PASSWORD = os.environ.get("ADMIN_PASSWORD", "PurplePanel").strip()
PRICE = int(os.environ.get("SALES_PRICE", 50000))
LIMIT_GB = int(os.environ.get("SALES_LIMIT_GB", 10))
EXPIRY_DAYS = int(os.environ.get("SALES_EXPIRY_DAYS", 30))

# ── وضعیت‌های مکالمه ──
WAITING_FOR_CUSTOM_NAME = 1

# ── دیتا در حافظه ──
pending_payments: Dict[int, dict] = {}
user_sessions: Dict[int, dict] = {}

# ── کیبورد شیشه‌ای (Glass Style) ──
def glass_keyboard(buttons: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in buttons:
        keyboard.append([InlineKeyboardButton(row["text"], callback_data=row["callback"])])
    return InlineKeyboardMarkup(keyboard)

# ── منوی اصلی ──
MAIN_MENU = glass_keyboard([
    {"text": "🟣 خرید کانفیگ", "callback": "buy"},
    {"text": "❓ راهنما", "callback": "help"},
    {"text": "📞 پشتیبانی", "callback": "support"},
])

# ── انتخاب کانفیگ ──
CONFIG_MENU = glass_keyboard([
    {"text": f"📦 {LIMIT_GB}GB / {EXPIRY_DAYS} روز", "callback": "config_default"},
    {"text": "✏️ سفارشی", "callback": "config_custom"},
    {"text": "🔙 بازگشت", "callback": "back"},
])

# ── تایید پرداخت ──
PAYMENT_KEYBOARD = glass_keyboard([
    {"text": "✅ رسید واریز", "callback": "payment_received"},
    {"text": "🔙 انصراف", "callback": "back"},
])

# ── Helper: ارسال به ادمین ──
async def notify_admin(context: ContextTypes.DEFAULT_TYPE, text: str, keyboard: InlineKeyboardMarkup = None):
    for admin_id in ADMIN_IDS:
        try:
            await context.bot.send_message(
                chat_id=admin_id,
                text=text,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard
            )
        except Exception as e:
            print(f"Admin notify error: {e}")

# ── Helper: ساخت کانفیگ از طریق پنل ──
async def create_config_via_panel(label: str, limit_gb: int, expiry_days: int) -> Optional[dict]:
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            # لاگین
            login = await client.post(
                f"{PANEL_URL}/api/login",
                json={"password": PANEL_PASSWORD}
            )
            if login.status_code != 200:
                return None
            cookies = login.cookies

            # ساخت کانفیگ
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
                cookies=cookies
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
            print(f"Create config error: {e}")
            return None

# ── دستور /start ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = (
        f"🟣 <b>به ربات فروش Purple-Panel خوش اومدی!</b>\n\n"
        f"👤 کاربر: {user.first_name}\n"
        f"🆔 آیدی: {user.id}\n\n"
        f"📦 <b>هر کانفیگ شامل:</b>\n"
        f"• {LIMIT_GB} گیگابایت ترافیک\n"
        f"• {EXPIRY_DAYS} روز اعتبار\n"
        f"• قیمت: {PRICE:,} تومان\n\n"
        f"برای خرید، دکمه زیر رو بزن. 👇"
    )
    await update.message.reply_text(msg, parse_mode=ParseMode.HTML, reply_markup=MAIN_MENU)

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
            parse_mode=ParseMode.HTML,
            reply_markup=CONFIG_MENU
        )

    elif data == "config_default":
        context.user_data["config_name"] = f"{LIMIT_GB}GB-{EXPIRY_DAYS}D"
        context.user_data["limit_gb"] = LIMIT_GB
        context.user_data["expiry_days"] = EXPIRY_DAYS
        await show_payment_info(query, user_id)

    elif data == "config_custom":
        user_sessions[user_id] = {"step": "waiting_custom_name"}
        await query.edit_message_text(
            "✏️ <b>نام کانفیگ</b>\n\n"
            "لطفاً نام دلخواه برای کانفیگت رو بفرست (مثلاً: کانفیگ علی):",
            parse_mode=ParseMode.HTML
        )

    elif data == "back":
        await query.edit_message_text(
            "🟣 <b>منوی اصلی</b>\n\n"
            "از دکمه‌های زیر استفاده کن:",
            parse_mode=ParseMode.HTML,
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
            parse_mode=ParseMode.HTML,
            reply_markup=glass_keyboard([{"text": "🔙 بازگشت", "callback": "back"}])
        )

    elif data == "support":
        await query.edit_message_text(
            "📞 <b>پشتیبانی</b>\n\n"
            "برای ارتباط با پشتیبانی:\n\n"
            "🟣 <a href='https://t.me/AghaBanafshiipvbot'>@AghaBanafshiipvbot</a>\n"
            "🟣 <a href='https://t.me/AghaBanafshi'>@AghaBanafshi</a>",
            parse_mode=ParseMode.HTML,
            reply_markup=glass_keyboard([{"text": "🔙 بازگشت", "callback": "back"}])
        )

    elif data == "payment_received":
        if user_id not in pending_payments:
            await query.edit_message_text("❌ درخواستی یافت نشد.", reply_markup=glass_keyboard([{"text": "🔙 بازگشت", "callback": "back"}]))
            return
        
        payment = pending_payments[user_id]
        payment_id = f"{user_id}_{datetime.now().timestamp()}"
        
        await notify_admin(
            context,
            f"💳 <b>واریز جدید</b>\n\n"
            f"👤 کاربر: {payment['user_id']}\n"
            f"📌 کانفیگ: {payment['config_name']}\n"
            f"💰 مبلغ: {PRICE:,} تومان\n"
            f"📅 تاریخ: {payment['date']}\n\n"
            f"لطفاً رسید رو بررسی و تایید کن.",
            keyboard=glass_keyboard([
                {"text": "✅ تایید و ساخت", "callback": f"confirm_{payment_id}"},
                {"text": "❌ لغو", "callback": f"cancel_{payment_id}"},
            ])
        )
        
        await query.edit_message_text(
            "✅ <b>رسید شما ثبت شد!</b>\n\n"
            "به زودی توسط ادمین بررسی میشه.\n"
            "🟣 لطفاً صبور باش!",
            parse_mode=ParseMode.HTML,
            reply_markup=glass_keyboard([{"text": "🔙 منوی اصلی", "callback": "back"}])
        )

    elif data.startswith("confirm_"):
        payment_id = data.replace("confirm_", "")
        # پیدا کردن پرداخت
        target_user = None
        for uid, p in pending_payments.items():
            if f"{uid}_{p.get('timestamp', '')}" == payment_id or f"{uid}_{datetime.now().timestamp()}" == payment_id:
                target_user = uid
                break
        
        if not target_user or target_user not in pending_payments:
            await query.edit_message_text("❌ این درخواز منقضی شده.")
            return
        
        payment = pending_payments[target_user]
        config_name = payment.get("config_name", f"{LIMIT_GB}GB-{EXPIRY_DAYS}D")
        limit_gb = payment.get("limit_gb", LIMIT_GB)
        expiry_days = payment.get("expiry_days", EXPIRY_DAYS)
        
        # ساخت کانفیگ
        result = await create_config_via_panel(config_name, limit_gb, expiry_days)
        
        if result:
            try:
                await context.bot.send_message(
                    chat_id=target_user,
                    text=(
                        f"✅ <b>کانفیگ شما ساخته شد!</b>\n\n"
                        f"📌 <b>نام:</b> {result['label']}\n"
                        f"🔗 <b>لینک:</b> <code>{result['link']}</code>\n\n"
                        f"📱 <b>Sub URL:</b> <code>{result['sub_url']}</code>\n\n"
                        f"🟣 توی <a href='{PANEL_URL}/dashboard'>پنل</a> هم مدیریتش کن."
                    ),
                    parse_mode=ParseMode.HTML
                )
            except Exception:
                pass
            
            await query.edit_message_text(
                f"✅ <b>کانفیگ کاربر ساخته شد!</b>\n\n"
                f"👤 کاربر: {target_user}\n"
                f"📌 نام: {config_name}\n"
                f"📦 سهمیه: {limit_gb} GB\n"
                f"📅 انقضا: {expiry_days} روز",
                parse_mode=ParseMode.HTML
            )
        else:
            await query.edit_message_text(
                "❌ <b>خطا در ساخت کانفیگ!</b>\n"
                "لطفاً پنل رو چک کن.",
                parse_mode=ParseMode.HTML
            )
        
        del pending_payments[target_user]

    elif data.startswith("cancel_"):
        payment_id = data.replace("cancel_", "")
        for uid in list(pending_payments.keys()):
            if f"{uid}_{pending_payments[uid].get('timestamp', '')}" == payment_id:
                del pending_payments[uid]
                break
        await query.edit_message_text("❌ درخواست لغو شد.", reply_markup=glass_keyboard([{"text": "🔙 منوی اصلی", "callback": "back"}]))

async def show_payment_info(query, user_id):
    config_name = query.message.chat.id  # workaround
    pending_payments[user_id] = {
        "user_id": user_id,
        "config_name": context.user_data.get("config_name", f"{LIMIT_GB}GB-{EXPIRY_DAYS}D"),
        "limit_gb": context.user_data.get("limit_gb", LIMIT_GB),
        "expiry_days": context.user_data.get("expiry_days", EXPIRY_DAYS),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "timestamp": datetime.now().timestamp()
    }
    
    msg = (
        f"💳 <b>اطلاعات واریز</b>\n\n"
        f"📦 <b>کانفیگ:</b> {context.user_data.get('config_name', f'{LIMIT_GB}GB-{EXPIRY_DAYS}D')}\n"
        f"💰 <b>مبلغ:</b> {PRICE:,} تومان\n\n"
        f"🏦 <b>شماره کارت:</b>\n"
        f"<code>{CARD_NUMBER}</code>\n"
        f"👤 <b>به نام:</b> {CARD_HOLDER}\n\n"
        f"📌 بعد از واریز، دکمه <b>رسید واریز</b> رو بزن."
    )
    await query.edit_message_text(msg, parse_mode=ParseMode.HTML, reply_markup=PAYMENT_KEYBOARD)

# ── پیام‌های متنی ──
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    
    if user_id in user_sessions and user_sessions[user_id].get("step") == "waiting_custom_name":
        config_name = text.strip()[:50] or "کانفیگ سفارشی"
        context.user_data["config_name"] = config_name
        context.user_data["limit_gb"] = LIMIT_GB
        context.user_data["expiry_days"] = EXPIRY_DAYS
        del user_sessions[user_id]
        
        pending_payments[user_id] = {
            "user_id": user_id,
            "config_name": config_name,
            "limit_gb": LIMIT_GB,
            "expiry_days": EXPIRY_DAYS,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "timestamp": datetime.now().timestamp()
        }
        
        msg = (
            f"✅ <b>نام کانفیگ ذخیره شد:</b> {config_name}\n\n"
            f"💳 <b>اطلاعات واریز</b>\n\n"
            f"📦 <b>کانفیگ:</b> {LIMIT_GB} گیگ / {EXPIRY_DAYS} روز\n"
            f"💰 <b>مبلغ:</b> {PRICE:,} تومان\n\n"
            f"🏦 <b>شماره کارت:</b>\n"
            f"<code>{CARD_NUMBER}</code>\n"
            f"👤 <b>به نام:</b> {CARD_HOLDER}\n\n"
            f"📌 بعد از واریز، دکمه <b>رسید واریز</b> رو بزن."
        )
        await update.message.reply_text(msg, parse_mode=ParseMode.HTML, reply_markup=PAYMENT_KEYBOARD)
        return
    
    await update.message.reply_text(
        "🟣 از دکمه‌های زیر استفاده کن:",
        reply_markup=MAIN_MENU
    )

# ── اجرا ──
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
    app.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
    
    print("🟣 ربات فروش Purple-Panel روشن شد!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(run_bot())

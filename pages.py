# pages.py - Purple-Panel v1.1
# 🟣 Customized by @AghaBanafshi
# Full-featured | Animated | Responsive

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · Purple-Panel v1.1</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0618;--card:rgba(20,10,45,0.85);--accent:#8B5CF6;--accent2:#A78BFA;--text:#F0E8FF;--dim:#6D4A9E;--mid:#A78BFA;--border:rgba(139,92,246,0.2);--glow:rgba(139,92,246,0.12)}
[data-theme="light"]{--bg:#F5F0FF;--card:rgba(255,255,255,0.88);--accent:#7C3AED;--accent2:#6D28D9;--text:#1A0E30;--dim:#7A5DA6;--mid:#4A2D6E;--border:rgba(124,58,237,0.15);--glow:rgba(124,58,237,0.06)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:16px;transition:background 0.6s ease;position:relative}
body::before{content:'';position:fixed;inset:0;z-index:0;background:radial-gradient(ellipse 60% 40% at 30% 20%,var(--glow),transparent 65%),radial-gradient(ellipse 50% 30% at 80% 80%,var(--glow),transparent 60%),var(--bg);animation:bgPulse 12s ease-in-out infinite}
@keyframes bgPulse{0%,100%{opacity:0.7}50%{opacity:1}}
.grid{position:fixed;inset:0;z-index:0;background-image:linear-gradient(rgba(139,92,246,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,0.04) 1px,transparent 1px);background-size:44px 44px;mask-image:radial-gradient(ellipse 60% 50% at 50% 40%,black 20%,transparent 80%);animation:gridMove 30s linear infinite}
@keyframes gridMove{from{transform:translateY(0)}to{transform:translateY(-44px)}}
.particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.particle{position:absolute;border-radius:50%;background:var(--accent);opacity:0;box-shadow:0 0 12px var(--accent);animation:floatParticle linear infinite}
@keyframes floatParticle{0%{transform:translateY(110vh) translateX(0) scale(0.3);opacity:0}10%{opacity:0.4}90%{opacity:0.2}100%{transform:translateY(-10vh) translateX(var(--drift)) scale(1);opacity:0}}
.orb{position:fixed;border-radius:50%;filter:blur(80px);z-index:0;animation:orbFloat 12s ease-in-out infinite}
.orb1{width:350px;height:350px;background:rgba(139,92,246,0.08);top:-80px;right:-60px}
.orb2{width:250px;height:250px;background:rgba(139,92,246,0.05);bottom:-40px;left:-40px;animation-delay:5s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(-20px,20px) scale(1.1)}66%{transform:translate(20px,-10px) scale(0.9)}}
.wrap{width:100%;max-width:400px;position:relative;z-index:10;animation:slideUp 0.7s cubic-bezier(0.16,1,0.3,1)}
@keyframes slideUp{from{opacity:0;transform:translateY(40px) scale(0.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.card{background:var(--card);border:1px solid var(--border);border-radius:24px;padding:38px 32px;backdrop-filter:blur(30px);box-shadow:0 30px 80px rgba(0,0,0,0.4),0 0 60px var(--glow);position:relative;overflow:hidden;transition:transform 0.4s cubic-bezier(0.16,1,0.3,1),box-shadow 0.4s ease}
.card:hover{transform:translateY(-4px);box-shadow:0 40px 100px rgba(0,0,0,0.5),0 0 80px var(--glow)}
.card::before{content:'';position:absolute;inset:-1px;border-radius:24px;padding:1px;z-index:-1;background:conic-gradient(from var(--ang,0deg),transparent 0%,var(--accent) 12%,transparent 28%,transparent 100%);mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);mask-composite:xor;-webkit-mask-composite:xor;opacity:0.5;animation:spinBorder 6s linear infinite}
@keyframes spinBorder{to{--ang:360deg}}
@property --ang{syntax:'<angle>';inherits:false;initial-value:0deg}
.card::after{content:'';position:absolute;top:0;left:20%;right:20%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5;animation:shineLine 3s ease-in-out infinite}
@keyframes shineLine{0%,100%{opacity:0.2;transform:scaleX(0.6)}50%{opacity:0.8;transform:scaleX(1)}}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:26px;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.1s backwards}
.brand-icon{width:50px;height:50px;border-radius:50%;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:24px;flex-shrink:0;box-shadow:0 0 40px rgba(139,92,246,0.3);animation:iconPulse 3s ease-in-out infinite}
@keyframes iconPulse{0%,100%{box-shadow:0 0 40px rgba(139,92,246,0.3)}50%{box-shadow:0 0 60px rgba(139,92,246,0.5)}}
.brand-name{font-size:19px;font-weight:800;color:var(--text);background:linear-gradient(135deg,var(--text),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.brand-sub{font-size:11px;color:var(--dim);margin-top:2px;display:flex;align-items:center;gap:5px}
.brand-sub .ver{background:var(--accent);color:#fff;padding:1px 8px;border-radius:20px;font-size:9px;font-weight:700;display:inline-block;animation:verPulse 2s ease-in-out infinite}
@keyframes verPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
h1{font-size:21px;font-weight:800;color:var(--text);margin-bottom:5px;letter-spacing:-0.02em;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.2s backwards}
.sub{font-size:12.5px;color:var(--mid);margin-bottom:24px;line-height:1.7;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.3s backwards}
@keyframes fadeIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.hint{display:flex;align-items:center;gap:10px;background:rgba(139,92,246,0.05);border:1px dashed var(--border);border-radius:10px;padding:10px 14px;margin-bottom:20px;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.4s backwards;transition:border-color 0.3s,background 0.3s}
.hint:hover{border-color:var(--accent);background:rgba(139,92,246,0.08)}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace;font-size:13px;font-weight:700;color:var(--accent);background:rgba(139,92,246,0.12);border:1px solid rgba(139,92,246,0.2);padding:4px 12px;border-radius:6px;cursor:pointer;transition:all 0.3s cubic-bezier(0.16,1,0.3,1)}
.hint-val:hover{transform:translateY(-2px) scale(1.05);background:rgba(139,92,246,0.2);box-shadow:0 4px 20px rgba(139,92,246,0.15)}
.hint-val:active{transform:scale(0.95)}
.field{margin-bottom:18px;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.5s backwards}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--dim);margin-bottom:7px;text-transform:uppercase;letter-spacing:0.06em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 14px;border-radius:12px;border:1.5px solid var(--border);background:rgba(0,0,0,0.2);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:all 0.3s cubic-bezier(0.16,1,0.3,1)}
[data-theme="light"] input[type=password]{background:rgba(124,58,237,0.04)}
input:focus{border-color:var(--accent);background:rgba(139,92,246,0.06);box-shadow:0 0 0 4px rgba(139,92,246,0.06);transform:translateY(-1px)}
.ic-lock{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:0.3s}
input:focus~.ic-lock{color:var(--accent);animation:lockWiggle 0.4s ease}
@keyframes lockWiggle{0%,100%{transform:translateY(-50%) rotate(0)}25%{transform:translateY(-50%) rotate(-8deg)}75%{transform:translateY(-50%) rotate(8deg)}}
.btn{width:100%;padding:14px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,#8B5CF6,#6D28D9,#5B21B6);background-size:200% 200%;color:#fff;font-family:inherit;font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 8px 30px rgba(139,92,246,0.35);transition:all 0.3s cubic-bezier(0.16,1,0.3,1);position:relative;overflow:hidden;animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.6s backwards,gradientMove 4s ease infinite}
@keyframes gradientMove{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,0.15),transparent);width:60%;transform:translateX(-200%);transition:transform 0.6s}
.btn:hover::before{transform:translateX(300%)}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 40px rgba(139,92,246,0.5)}
.btn:active{transform:scale(0.97)}
.btn:disabled{opacity:0.5;cursor:not-allowed}
.btn .ripple{position:absolute;border-radius:50%;background:rgba(255,255,255,0.3);transform:scale(0);animation:rippleAnim 0.6s linear}
@keyframes rippleAnim{to{transform:scale(4);opacity:0}}
.err{display:none;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;color:#F87171;font-size:12.5px;align-items:center;gap:8px;animation:shake 0.4s cubic-bezier(0.16,1,0.3,1)}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-6px)}40%{transform:translateX(6px)}60%{transform:translateX(-3px)}80%{transform:translateX(3px)}}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;flex-direction:column;align-items:center;gap:5px;font-size:10.5px;color:var(--dim);animation:fadeIn 0.7s cubic-bezier(0.16,1,0.3,1) 0.7s backwards}
.footer .row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center}
.footer a{color:var(--accent);font-weight:700;text-decoration:none;transition:all 0.3s}
.footer a:hover{filter:brightness(1.2);transform:translateY(-1px)}
.footer .credit{font-size:9px;color:var(--dim);opacity:0.6}
.theme-switch{position:fixed;top:20px;left:20px;z-index:50}
.theme-btn{width:42px;height:42px;border-radius:12px;background:var(--card);border:1px solid var(--border);color:var(--mid);display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;backdrop-filter:blur(16px);transition:all 0.4s cubic-bezier(0.16,1,0.3,1)}
.theme-btn:hover{transform:rotate(30deg) scale(1.1);border-color:var(--accent);color:var(--accent2)}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:420px){.card{padding:30px 22px;border-radius:18px}.hint{flex-wrap:wrap}.footer .row{font-size:10px}}
@media(prefers-reduced-motion:reduce){*{animation-duration:0.001s !important}}
</style>
</head>
<body>
<div class="grid"></div><div class="particles" id="particles"></div>
<div class="orb orb1"></div><div class="orb orb2"></div>
<div class="theme-switch"><button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="themeIcon"></i></button></div>
<div class="wrap"><div class="card">
<div class="brand"><div class="brand-icon"><i class="ti ti-brand-azure"></i></div><div><div class="brand-name">Purple-Panel</div><div class="brand-sub">v<span class="ver">1.1</span></div></div></div>
<h1>ورود به پنل</h1>
<p class="sub">رمز عبور را برای دسترسی به داشبورد مدیریت وارد کنید</p>
<div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="errText"></span></div>
<div class="hint"><i class="ti ti-info-circle"></i><span class="hint-label">رمز پیش‌فرض</span><span class="hint-val" onclick="fillDefault()">PurplePanel</span></div>
<form id="form">
<div class="field"><label>رمز عبور</label><div class="inp-wrap"><input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required><i class="ti ti-lock ic-lock"></i></div></div>
<button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
</form>
<div class="footer">
<div class="row">✨ کاستوم‌سازی: <a href="https://t.me/AghaBanafshi" target="_blank">@AghaBanafshi</a></div>
<div class="row">📱 پشتیبانی: <a href="https://t.me/AghaBanafshiipvbot" target="_blank">@AghaBanafshiipvbot</a></div>
<div class="row"><span class="credit">🟣 <a href="https://github.com/TheAghaBanafshi" target="_blank">github.com/TheAghaBanafshi</a></span></div>
</div>
</div></div>
<script>
let isDark=localStorage.getItem('pp-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('themeIcon').className='ti '+(dark?'ti-sun':'ti-moon')}
function toggleTheme(){isDark=!isDark;localStorage.setItem('pp-theme',isDark?'dark':'light');applyTheme(isDark);const b=document.querySelector('.theme-btn');b.style.transform='rotate(30deg) scale(1.1)';setTimeout(()=>b.style.transform='',400)}
applyTheme(isDark);
function fillDefault(){document.getElementById('pw').value='PurplePanel';document.getElementById('pw').focus()}
(function(){const box=document.getElementById('particles');for(let i=0;i<25;i++){const p=document.createElement('div');p.className='particle';const s=2+Math.random()*4;p.style.width=s+'px';p.style.height=s+'px';p.style.left=Math.random()*100+'vw';p.style.setProperty('--drift',(Math.random()*80-40)+'px');p.style.animationDuration=(12+Math.random()*18)+'s';p.style.animationDelay=(Math.random()*15)+'s';box.appendChild(p)}})();
document.querySelector('.btn')?.addEventListener('click',function(e){if(this.disabled)return;const r=document.createElement('span');r.className='ripple';const rect=this.getBoundingClientRect();const x=e.clientX-rect.left,y=e.clientY-rect.top;r.style.left=x+'px';r.style.top=y+'px';r.style.width='20px';r.style.height='20px';this.appendChild(r);setTimeout(()=>r.remove(),600)});
document.getElementById('form').addEventListener('submit',async e=>{e.preventDefault();const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('errText');err.classList.remove('show');btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>';try{const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا')}location.href='/dashboard'}catch(e){et.textContent=e.message;err.classList.add('show');btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد'}});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Purple-Panel v1.1</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0618;--bg2:#140a2a;--bg3:#1e0f3a;
  --card:#1a0d30;--card-b:rgba(139,92,246,0.12);--card-bh:rgba(139,92,246,0.28);
  --accent:#8B5CF6;--accent2:#A78BFA;--accent-d:rgba(139,92,246,0.08);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);
  --t1:#F0E8FF;--t2:#9C8ABF;--t3:#6D4A9E;
  --sidebar-w:240px;--radius:14px;
  --shadow:0 4px 24px rgba(0,0,0,0.35);
  --glow:rgba(139,92,246,0.06);
}
[data-theme="light"]{
  --bg:#F5F0FF;--bg2:#EBE0FF;--bg3:#DFD0FF;
  --card:#FFFFFF;--card-b:rgba(139,92,246,0.14);--card-bh:rgba(139,92,246,0.28);
  --accent:#7C3AED;--accent2:#6D28D9;--accent-d:rgba(124,58,237,0.06);
  --green:#059669;--green-bg:rgba(5,150,105,0.06);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.06);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.06);
  --t1:#1A0E30;--t2:#4A2D6E;--t3:#7A5DA6;
  --shadow:0 4px 16px rgba(80,40,160,0.08);
  --glow:rgba(124,58,237,0.04);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background 0.6s ease,color 0.6s ease;position:relative}
body::before{content:'';position:fixed;inset:0;z-index:-1;background:radial-gradient(ellipse 50% 30% at 20% 10%,var(--glow),transparent 65%),radial-gradient(ellipse 40% 20% at 90% 90%,var(--glow),transparent 60%),var(--bg);animation:bodyGlow 15s ease-in-out infinite}
@keyframes bodyGlow{0%,100%{opacity:0.7}50%{opacity:1}}
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg2);border-radius:4px}
a{color:inherit;text-decoration:none}
.floating-menu{position:fixed;bottom:24px;right:24px;z-index:300;display:flex;flex-direction:column;align-items:center;gap:8px;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.5s backwards}
.fm-toggle{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#8B5CF6,#6D28D9);border:none;color:#fff;font-size:24px;cursor:pointer;box-shadow:0 4px 24px rgba(139,92,246,0.4);transition:all 0.3s cubic-bezier(0.16,1,0.3,1);position:relative;display:flex;align-items:center;justify-content:center}
.fm-toggle::after{content:'';position:absolute;inset:-3px;border-radius:50%;border:1.5px solid var(--accent);opacity:0.4;animation:ringPulse 2.4s ease-in-out infinite}
@keyframes ringPulse{0%,100%{transform:scale(1);opacity:0.4}50%{transform:scale(1.12);opacity:0}}
.fm-toggle:hover{transform:scale(1.06)}
.fm-toggle:active{transform:scale(0.93)}
.fm-items{display:flex;flex-direction:column;gap:6px;opacity:0;transform:translateY(20px) scale(0.8);pointer-events:none;transition:all 0.3s cubic-bezier(0.16,1,0.3,1)}
.fm-items.open{opacity:1;transform:translateY(0) scale(1);pointer-events:auto}
.fm-item{width:44px;height:44px;border-radius:50%;background:var(--card);border:1px solid var(--card-b);color:var(--t2);font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.25s cubic-bezier(0.16,1,0.3,1);box-shadow:var(--shadow);backdrop-filter:blur(12px)}
.fm-item:hover{background:var(--accent-d);color:var(--accent);transform:scale(1.08)}
.fm-item:active{transform:scale(0.92)}
.fm-item i{font-size:18px}
.sidebar{position:fixed;top:0;right:0;bottom:0;width:var(--sidebar-w);background:var(--bg2);border-left:1px solid var(--card-b);padding:20px 16px;display:flex;flex-direction:column;gap:4px;z-index:100;transition:transform 0.3s cubic-bezier(0.16,1,0.3,1);backdrop-filter:blur(16px)}
.sidebar .logo{display:flex;align-items:center;gap:12px;padding-bottom:16px;border-bottom:1px solid var(--card-b);margin-bottom:12px}
.sidebar .logo-icon{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 0 20px rgba(139,92,246,0.2);animation:logoPulse 3s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 20px rgba(139,92,246,0.2)}50%{box-shadow:0 0 35px rgba(139,92,246,0.35)}}
.sidebar .logo-name{font-size:14px;font-weight:800;color:var(--t1);background:linear-gradient(135deg,var(--t1),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sidebar .logo-sub{font-size:10px;color:var(--t3);margin-top:2px}
.sb-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;color:var(--t3);font-size:12.5px;cursor:pointer;transition:all 0.25s cubic-bezier(0.16,1,0.3,1);border-right:2px solid transparent}
.sb-item:hover{background:var(--accent-d);color:var(--t2);transform:translateX(-3px)}
.sb-item.active{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:0 0 20px rgba(139,92,246,0.04)}
.sb-item i{font-size:16px;width:18px;text-align:center}
.sb-footer{margin-top:auto;padding-top:14px;border-top:1px solid var(--card-b);display:flex;flex-direction:column;gap:6px}
.sb-footer button{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);border-radius:8px;padding:8px;font-family:inherit;font-size:12px;font-weight:600;cursor:pointer;transition:all 0.25s cubic-bezier(0.16,1,0.3,1);display:flex;align-items:center;justify-content:center;gap:6px}
.sb-footer button:hover{background:var(--card-b);color:var(--t1);transform:translateY(-2px)}
.sb-footer .logout{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,0.15)}
.sb-footer .logout:hover{background:rgba(239,68,68,0.2)}
.main{margin-right:var(--sidebar-w);padding:24px 28px 80px;flex:1;min-height:100vh}
.pg{display:none;animation:fadePage 0.4s cubic-bezier(0.16,1,0.3,1)}
.pg.active{display:block}
@keyframes fadePage{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.topbar{display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;margin-bottom:18px}
.tb-title{font-size:19px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-0.02em}
.tb-title i{color:var(--accent);font-size:21px;animation:titlePulse 3s ease-in-out infinite}
@keyframes titlePulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.tb-sub{font-size:11px;color:var(--t3);margin-top:3px}
.tb-actions{display:flex;gap:6px;flex-wrap:wrap}
.badge{font-size:9.5px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:4px;transition:all 0.3s ease}
.badge:hover{transform:scale(1.05)}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block;flex-shrink:0}
.dg{background:var(--green)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 18px 14px;transition:all 0.3s cubic-bezier(0.16,1,0.3,1);cursor:default;position:relative;overflow:hidden}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:0.3s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric .m-icon{width:36px;height:36px;border-radius:9px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;color:var(--accent);font-size:17px;margin-bottom:10px;transition:transform 0.3s ease}
.metric:hover .m-icon{transform:scale(1.1) rotate(-5deg)}
.metric .m-label{font-size:10px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:0.05em}
.metric .m-val{font-size:26px;font-weight:700;color:var(--t1);line-height:1.1}
.metric .m-unit{font-size:13px;font-weight:400;color:var(--t3)}
.metric .m-sub{font-size:10px;color:var(--t3);margin-top:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:all 0.3s cubic-bezier(0.16,1,0.3,1)}
.card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:14px;display:flex;align-items:center;gap:7px}
.card-title i{color:var(--accent);font-size:17px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:18px}
.ch{height:200px;position:relative;animation:chartIn 0.8s cubic-bezier(0.16,1,0.3,1)}
@keyframes chartIn{from{opacity:0;transform:scale(0.96)}to{opacity:1;transform:scale(1)}}
.ch-sm{height:150px;position:relative}
.sr{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(139,92,246,0.04);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:5px}
.sr-v{color:var(--t1);font-weight:600}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 0.8s}
.empty{text-align:center;padding:40px 16px;color:var(--t3)}
.empty i{font-size:36px;opacity:0.3;display:block;margin-bottom:10px}
.btn{font-family:inherit;font-size:11.5px;font-weight:600;border-radius:8px;padding:7px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all 0.25s cubic-bezier(0.16,1,0.3,1)}
.btn i{font-size:13px}
.btn:hover{transform:translateY(-2px)}
.btn:active{transform:scale(0.95)}
.btn-p{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#fff;box-shadow:0 4px 16px rgba(139,92,246,0.3)}
.btn-p:hover{box-shadow:0 6px 24px rgba(139,92,246,0.4)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(139,92,246,0.12)}
.btn-g:hover{background:rgba(139,92,246,0.16)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,0.15)}
.btn-d:hover{background:rgba(239,68,68,0.2)}
.btn-sm{padding:4px 10px;font-size:10px}
.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(60px);background:var(--card);border:1px solid var(--card-b);border-radius:10px;padding:10px 18px;font-size:12px;color:var(--t1);box-shadow:var(--shadow);opacity:0;transition:all 0.4s cubic-bezier(0.16,1,0.3,1);z-index:999;white-space:nowrap;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,0.25);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,0.25);background:var(--red-bg);color:var(--red-t)}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:820px){
  .sidebar{transform:translateX(100%);width:200px}
  .sidebar.open{transform:translateX(0);box-shadow:0 0 40px rgba(0,0,0,0.4)}
  .main{margin-right:0;padding:16px 14px 80px}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:480px){
  .metrics{grid-template-columns:1fr}
  .main{padding:12px 10px 72px}
  .floating-menu{bottom:16px;right:16px}
  .fm-toggle{width:48px;height:48px;font-size:20px}
  .fm-item{width:38px;height:38px;font-size:14px}
}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="floating-menu" id="floatingMenu">
<div class="fm-items" id="fmItems">
<button class="fm-item" onclick="toggleTheme()"><i class="ti ti-sun" id="themeIcon"></i></button>
<button class="fm-item" onclick="navTo('overview')"><i class="ti ti-layout-dashboard"></i></button>
<button class="fm-item" onclick="navTo('links')"><i class="ti ti-link-plus"></i></button>
<button class="fm-item" onclick="navTo('traffic')"><i class="ti ti-chart-area"></i></button>
<button class="fm-item" onclick="navTo('connections')"><i class="ti ti-plug-connected"></i></button>
<button class="fm-item" onclick="logout()"><i class="ti ti-logout"></i></button>
</div>
<button class="fm-toggle" id="fmToggle" onclick="toggleMenu()"><i class="ti ti-menu-2"></i></button>
</div>
<div class="sidebar" id="sidebar">
<div class="logo"><div class="logo-icon"><i class="ti ti-brand-azure"></i></div><div><div class="logo-name">Purple-Panel</div><div class="logo-sub">v1.1</div></div></div>
<div class="sb-item active" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
<div class="sb-item" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div>
<div class="sb-item" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
<div class="sb-item" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات</div>
<div class="sb-item" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
<div class="sb-item" data-pg="logs"><i class="ti ti-history"></i> لاگ‌ها</div>
<div class="sb-item" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
<div class="sb-footer">
<button onclick="toggleTheme()"><i class="ti ti-moon" id="themeIcon2"></i> <span id="themeLabel">تم روشن</span></button>
<button class="logout" onclick="logout()"><i class="ti ti-logout"></i> خروج</button>
</div>
</div>
<div class="main" id="mainContent">
<section class="pg active" id="pg-overview">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="lastUpdate">در حال بارگذاری...</div></div><div class="tb-actions"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
<div class="metrics"><div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="mConns">—</div><div class="m-sub"><span class="dot dg pulse"></span></div></div><div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="mTraffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div><div class="metric"><div class="m-icon" style="background:var(--green-bg);color:var(--green-t)"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="mAlinks">—</div><div class="m-sub" id="mLsub">از کل</div></div><div class="metric"><div class="m-icon" style="background:var(--red-bg);color:var(--red-t)"><i class="ti ti-alert-triangle"></i></div><div class="m-label">خطاها</div><div class="m-val" id="mErrs">—</div><div class="m-sub">از راه‌اندازی</div></div></div>
<div class="g3"><div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی</div><div class="ch"><canvas id="chart1"></canvas></div></div><div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="chart2"></canvas></div></div></div>
<div class="g2"><div class="card"><div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div><div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">فعال ✓</span></div><div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS/WS</span><span class="sr-v" style="color:var(--green-t)">فعال ✓</span></div><div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription</span><span class="sr-v" style="color:var(--green-t)">فعال ✓</span></div><div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptimeInline">—</span></div></div><div class="card"><div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها</div><div id="linkSummary">—</div></div></div>
<div style="font-size:10px;color:var(--t3);text-align:center;padding-top:10px;border-top:1px solid var(--card-b);margin-top:10px">🟣 Purple-Panel v1.1 · <a href="https://github.com/TheAghaBanafshi" target="_blank" style="color:var(--accent2)">github.com/TheAghaBanafshi</a> · ✨ <a href="https://t.me/AghaBanafshi" target="_blank" style="color:var(--accent2)">@AghaBanafshi</a></div>
</section>
<section class="pg" id="pg-links">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">مدیریت کانفیگ‌ها</div></div><div class="tb-actions"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
<div class="card" style="margin-bottom:14px"><div class="card-title"><i class="ti ti-square-rounded-plus"></i> ساخت کانفیگ جدید</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:8px"><input id="nlLabel" placeholder="عنوان" style="padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"><input id="nlVal" type="number" min="0" step="0.1" placeholder="سهمیه (MB)" style="padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"></div>
<div style="display:flex;gap:8px;flex-wrap:wrap"><input id="nlExp" type="number" min="0" step="1" placeholder="انقضا (روز)" style="flex:1;padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"><button class="btn btn-p" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت</button></div></div>
<div id="linksGrid"></div>
<div class="empty" id="linksEmpty"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-traffic">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">مصرف پهنای باند</div></div></div>
<div class="card"><div class="card-title"><i class="ti ti-activity"></i> روند مصرف</div><div class="ch" style="height:280px"><canvas id="chart3"></canvas></div></div>
</section>
<section class="pg" id="pg-connections">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">در لحظه</div></div></div>
<div class="card"><div id="connsGrid"><div class="empty"><i class="ti ti-plug-off"></i><p>اتصالی نیست</p></div></div></div>
</section>
<section class="pg" id="pg-security">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
<div class="g2"><div class="card"><div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div><div class="sr"><span class="sr-k">TLS</span><span class="sr-v" style="color:var(--green-t)">فعال ✓</span></div><div class="sr"><span class="sr-k">UUID Auth</span><span class="sr-v" style="color:var(--green-t)">فعال ✓</span></div><div class="sr"><span class="sr-k">Fingerprint</span><span class="sr-v">Chrome</span></div></div><div class="card"><div class="card-title"><i class="ti ti-key"></i> تغییر رمز</div><div style="display:flex;flex-direction:column;gap:8px"><input type="password" id="cpCur" placeholder="رمز فعلی" style="padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"><input type="password" id="cpNew" placeholder="رمز جدید" style="padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"><input type="password" id="cpCf" placeholder="تکرار رمز جدید" style="padding:9px 12px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:border-color 0.3s" onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor=''"><button class="btn btn-p" onclick="changePassword()"><i class="ti ti-shield-check"></i> تغییر رمز</button></div></div></div>
</section>
<section class="pg" id="pg-logs">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div></div></div>
<div class="card"><div id="logsList"><div class="empty"><i class="ti ti-history-toggle"></i><p>لاگی وجود ندارد</p></div></div></div>
</section>
<section class="pg" id="pg-settings">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
<div class="card"><div class="card-title"><i class="ti ti-server-2"></i> اطلاعات سرور</div>
<div class="sr"><span class="sr-k">دامنه</span><span class="sr-v" id="setHost">—</span></div>
<div class="sr"><span class="sr-k">نسخه</span><span class="sr-v">v1.1</span></div>
<div class="sr"><span class="sr-k">پلتفرم</span><span class="sr-v">Railway</span></div>
</div>
</section>
</div>
<script>
let isDark=localStorage.getItem('pp-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';['themeIcon','themeIcon2'].forEach(id=>{const el=document.getElementById(id);if(el)el.className='ti '+icon});['themeLabel'].forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=label})}
function toggleTheme(){isDark=!isDark;localStorage.setItem('pp-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2500)}
function toggleMenu(){document.getElementById('fmItems').classList.toggle('open')}
function closeMenu(){document.getElementById('fmItems').classList.remove('open')}
function navTo(name){
document.querySelectorAll('.sb-item').forEach(el=>el.classList.toggle('active',el.dataset.pg===name));
document.querySelectorAll('.pg').forEach(el=>el.classList.toggle('active',el.id==='pg-'+name));
closeMenu();window.scrollTo({top:0,behavior:'smooth'});
if(name==='links')loadLinks();if(name==='traffic')loadTraffic();if(name==='connections')loadConns();if(name==='logs')loadLogs();
}
document.querySelectorAll('.sb-item').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
async function authF(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){if(expired)return '⛔ منقضی';if(!exp)return '♾ نامحدود';const d=daysLeft(exp);if(d<=0)return '⛔ منقضی';if(d<=3)return '⚠️ '+toFa(d)+' روز';return '✅ '+toFa(d)+' روز'}
function protoBadge(p){const m={'vless-ws':'VLESS/WS','xhttp':'XHTTP Ultra'};return m[p]||p}
let chart1,chart2,chart3;
async function fetchStats(){
try{const r=await authF('/stats'),d=await r.json();
document.getElementById('mConns').textContent=d.active_connections||0;
document.getElementById('mTraffic').innerHTML=(d.total_traffic_mb||0).toFixed(1)+'<span class="m-unit">MB</span>';
document.getElementById('mAlinks').textContent=d.active_links||0;
document.getElementById('mLsub').textContent='از '+(d.links_count||0)+' کانفیگ';
document.getElementById('mErrs').textContent=d.total_errors||0;
document.getElementById('uptimeInline').textContent=d.uptime||'—';
document.getElementById('lastUpdate').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
if(d.hourly){const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));if(chart1){chart1.data.labels=labels;chart1.data.datasets[0].data=vals;chart1.update()}}
}catch(e){console.error(e)}}
function initCharts(){
const ctx1=document.getElementById('chart1')?.getContext('2d');if(ctx1){chart1=new Chart(ctx1,{type:'line',data:{labels:[],datasets:[{label:'MB',data:[],borderColor:'#8B5CF6',backgroundColor:'rgba(139,92,246,0.08)',fill:true,tension:0.4,pointRadius:0}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{beginAtZero:true}}}})}
const ctx2=document.getElementById('chart2')?.getContext('2d');if(ctx2){chart2=new Chart(ctx2,{type:'doughnut',data:{labels:['VLESS/WS','XHTTP','HTTP'],datasets:[{data:[60,25,15],backgroundColor:['#8B5CF6','#10B981','#6D28D9']}]},options:{responsive:true,maintainAspectRatio:false,cutout:'70%',plugins:{legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10}}}}}})}
const ctx3=document.getElementById('chart3')?.getContext('2d');if(ctx3){chart3=new Chart(ctx3,{type:'line',data:{labels:[],datasets:[{label:'مصرف (MB)',data:[],borderColor:'#8B5CF6',backgroundColor:'rgba(139,92,246,0.06)',fill:true,tension:0.4,pointRadius:0}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{beginAtZero:true}}}})}
}
let allLinks=[];
async function loadLinks(){try{const r=await authF('/api/links'),d=await r.json();allLinks=d.links||[];const grid=document.getElementById('linksGrid'),empty=document.getElementById('linksEmpty');if(!allLinks.length){grid.innerHTML='';empty.style.display='block';return}empty.style.display='none';grid.innerHTML=allLinks.map(l=>{const pct=l.limit_bytes?Math.min(100,l.used_bytes/l.limit_bytes*100):0;const lim=l.limit_bytes?fmtB(l.limit_bytes):'∞';return `<div style="background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 14px;margin-bottom:6px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;transition:all 0.25s cubic-bezier(0.16,1,0.3,1)" onmouseenter="this.style.borderColor='var(--card-bh)';this.style.transform='translateY(-2px)';this.style.boxShadow='var(--shadow)'" onmouseleave="this.style.borderColor='';this.style.transform='';this.style.boxShadow=''"><div style="flex:1;min-width:120px"><div style="font-weight:700;font-size:13px;color:var(--t1)">${esc(l.label)}</div><div style="font-size:10px;color:var(--t3)">${l.uuid.slice(0,10)}…</div></div><div style="flex:0 0 100px"><div style="font-size:11px;color:var(--t2)">${fmtB(l.used_bytes)} / ${lim}</div><div style="height:4px;border-radius:3px;background:var(--accent-d);margin-top:3px;overflow:hidden"><div style="height:100%;border-radius:3px;width:${pct}%;background:${pct>90?'var(--red)':pct>70?'var(--amber)':'var(--green)'};transition:width 0.6s"></div></div></div><div style="font-size:10px;color:var(--t3)">${expChip(l.expires_at,l.expired)}</div><div style="display:flex;gap:4px"><button class="btn btn-sm btn-g" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-d" onclick="deleteLink('${l.uuid}')"><i class="ti ti-trash"></i></button></div></div>`}).join('')}catch(e){console.error(e)}}
async function createLink(){const label=document.getElementById('nlLabel').value.trim()||'کانفیگ';const val=document.getElementById('nlVal').value;const exp=document.getElementById('nlExp').value;try{await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:'MB',expires_days:exp||0,protocol:'vless-ws',fingerprint:'chrome'})});toast('کانفیگ ساخته شد ✓','ok');['nlLabel','nlVal','nlExp'].forEach(id=>document.getElementById(id).value='');loadLinks()}catch(e){toast('خطا','err')}}
async function deleteLink(uuid){if(!confirm('حذف؟'))return;try{await authF('/api/links/'+uuid,{method:'DELETE'});toast('حذف شد ✓','ok');loadLinks()}catch(e){toast('خطا','err')}}
async function loadTraffic(){try{const r=await authF('/stats'),d=await r.json();if(d.hourly&&chart3){const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));chart3.data.labels=labels;chart3.data.datasets[0].data=vals;chart3.update()}}catch(e){}}
async function loadConns(){try{const r=await authF('/api/connections'),d=await r.json();const grid=document.getElementById('connsGrid');const conns=d.connections||[];if(!conns.length){grid.innerHTML='<div class="empty"><i class="ti ti-plug-off"></i><p>اتصالی نیست</p></div>';return}grid.innerHTML=conns.slice(0,10).map(c=>`<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(139,92,246,0.04);font-size:12px;animation:fadeUp 0.3s cubic-bezier(0.16,1,0.3,1) backwards"><span style="color:var(--t1)">${esc(c.ip)}</span><span style="color:var(--t3)">${c.bytes_fmt||'0 B'}</span></div>`).join('')}catch(e){}}
async function loadLogs(){try{const r=await authF('/api/activity'),d=await r.json();const list=document.getElementById('logsList');const logs=(d.logs||[]).slice(-10).reverse();if(!logs.length){list.innerHTML='<div class="empty"><i class="ti ti-history-toggle"></i><p>لاگی وجود ندارد</p></div>';return}list.innerHTML=logs.map(l=>`<div style="padding:6px 0;border-bottom:1px solid rgba(139,92,246,0.03);font-size:11.5px;animation:fadeUp 0.3s cubic-bezier(0.16,1,0.3,1) backwards"><span style="color:var(--t2)">${esc(l.message)}</span><span style="color:var(--t3);font-size:9.5px;display:block">${new Date(l.time).toLocaleString('fa-IR')}</span></div>`).join('')}catch(e){}}
async function changePassword(){const cur=document.getElementById('cpCur').value,nw=document.getElementById('cpNew').value,cf=document.getElementById('cpCf').value;if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}if(nw!==cf){toast('تکرار رمز اشتباه','err');return}try{await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});toast('رمز تغییر کرد ✓','ok');['cpCur','cpNew','cpCf'].forEach(id=>document.getElementById(id).value='')}catch(e){toast('خطا','err')}}
function refreshAll(){fetchStats();loadLinks();loadTraffic();loadConns();loadLogs();toast('رفرش شد','ok')}
document.addEventListener('DOMContentLoaded',async()=>{
initCharts();
document.getElementById('setHost').textContent=location.host;
fetchStats();loadLinks();loadTraffic();loadConns();loadLogs();
setInterval(fetchStats,5000);
setInterval(()=>{if(document.getElementById('pg-links').classList.contains('active'))loadLinks()},8000);
});
</script>
</body></html>"""

# حذف تابع get_public_page_html برای جلوگیری از باگ

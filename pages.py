# pages.py - Purple-Panel v1.1
# 🟣 Customized by @AghaBanafshi

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
:root{--bg:#0a0618;--card:rgba(20,10,45,0.85);--accent:#8B5CF6;--accent2:#A78BFA;--text:#F0E8FF;--dim:#6D4A9E;--mid:#A78BFA;--border:rgba(139,92,246,0.25);--glow:rgba(139,92,246,0.15);--glass:rgba(255,255,255,0.03)}
[data-theme="light"]{--bg:#F5F0FF;--card:rgba(255,255,255,0.88);--accent:#7C3AED;--accent2:#6D28D9;--text:#1A0E30;--dim:#7A5DA6;--mid:#4A2D6E;--border:rgba(124,58,237,0.2);--glow:rgba(124,58,237,0.08);--glass:rgba(124,58,237,0.03)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background .6s ease;position:relative}
.bg{position:fixed;inset:0;z-index:0;background:radial-gradient(ellipse 70% 50% at 30% 20%,var(--glow),transparent 65%),radial-gradient(ellipse 50% 40% at 80% 80%,var(--glow),transparent 60%),var(--bg);transition:background .8s ease;animation:bgPulse 12s ease-in-out infinite}
@keyframes bgPulse{0%,100%{opacity:1}50%{opacity:.85}}
.grid{position:fixed;inset:0;z-index:0;background-image:linear-gradient(rgba(139,92,246,0.05) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,0.05) 1px,transparent 1px);background-size:52px 52px;mask-image:radial-gradient(ellipse 60% 50% at 50% 40%,black 20%,transparent 80%);animation:gridMove 25s linear infinite}
@keyframes gridMove{from{transform:translateY(0)}to{transform:translateY(-52px)}}
.particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.particle{position:absolute;border-radius:50%;background:var(--accent);opacity:0;box-shadow:0 0 12px var(--accent);animation:float linear infinite}
@keyframes float{0%{transform:translateY(110vh) translateX(0) scale(0.3);opacity:0}10%{opacity:0.6}90%{opacity:0.4}100%{transform:translateY(-10vh) translateX(var(--drift)) scale(1);opacity:0}}
.orb{position:fixed;border-radius:50%;filter:blur(80px);z-index:0;animation:orbFloat 12s ease-in-out infinite}
.orb1{width:350px;height:350px;background:rgba(139,92,246,0.08);top:-80px;right:-60px;animation-delay:0s}
.orb2{width:250px;height:250px;background:rgba(139,92,246,0.05);bottom:-40px;left:-40px;animation-delay:5s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(-20px,20px) scale(1.1)}66%{transform:translate(20px,-10px) scale(0.9)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px;perspective:1000px;animation:cardIn 0.8s cubic-bezier(0.16,1,0.3,1) forwards}
@keyframes cardIn{from{opacity:0;transform:rotateY(-10deg) translateY(40px) scale(0.95)}to{opacity:1;transform:rotateY(0) translateY(0) scale(1)}}
.card{background:var(--card);border:1px solid var(--border);border-radius:24px;padding:40px 34px 34px;backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);box-shadow:0 40px 100px -20px rgba(0,0,0,0.5),0 0 0 1px var(--glass) inset,0 0 60px var(--glow);position:relative;overflow:hidden;transition:transform 0.4s cubic-bezier(0.16,1,0.3,1),box-shadow 0.4s ease}
.card:hover{transform:translateY(-4px) scale(1.005);box-shadow:0 50px 120px -20px rgba(0,0,0,0.6),0 0 0 1px var(--glass) inset,0 0 80px var(--glow)}
.card::before{content:'';position:absolute;inset:-1px;border-radius:24px;padding:1px;z-index:-1;background:conic-gradient(from var(--ang,0deg),transparent 0%,var(--accent) 10%,transparent 25%,transparent 100%);mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);mask-composite:xor;-webkit-mask-composite:xor;opacity:0.5;animation:spinBorder 6s linear infinite}
@keyframes spinBorder{to{--ang:360deg}}
@property --ang{syntax:'<angle>';inherits:false;initial-value:0deg}
.card::after{content:'';position:absolute;top:0;left:20%;right:20%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.6;animation:shineLine 3s ease-in-out infinite}
@keyframes shineLine{0%,100%{opacity:0.2;transform:scaleX(0.5)}50%{opacity:0.8;transform:scaleX(1)}}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px;position:relative}
.brand-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:24px;flex-shrink:0;box-shadow:0 8px 30px rgba(139,92,246,0.4);animation:iconPulse 3s ease-in-out infinite}
@keyframes iconPulse{0%,100%{box-shadow:0 8px 30px rgba(139,92,246,0.4)}50%{box-shadow:0 8px 50px rgba(139,92,246,0.7)}}
.brand-name{font-size:20px;font-weight:800;color:var(--text);letter-spacing:-0.02em;background:linear-gradient(135deg,var(--text),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.brand-sub{font-size:11px;color:var(--dim);margin-top:2px;display:flex;align-items:center;gap:5px}
.brand-sub .ver{background:var(--accent);color:#fff;padding:1px 8px;border-radius:20px;font-size:9px;font-weight:700;display:inline-block;animation:verPulse 2s ease-in-out infinite}
@keyframes verPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
h1{font-size:22px;font-weight:800;color:var(--text);margin-bottom:5px;letter-spacing:-0.02em;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.1s backwards}
.sub{font-size:12.5px;color:var(--mid);margin-bottom:24px;line-height:1.7;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.2s backwards}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.hint{display:flex;align-items:center;gap:10px;background:var(--glass);border:1px dashed var(--border);border-radius:12px;padding:10px 14px;margin-bottom:22px;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.3s backwards;transition:border-color 0.3s,background 0.3s}
.hint:hover{border-color:var(--accent);background:rgba(139,92,246,0.05)}
.hint i{color:var(--dim);font-size:16px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--accent);background:rgba(139,92,246,0.12);border:1px solid rgba(139,92,246,0.25);padding:4px 12px;border-radius:8px;cursor:pointer;transition:all 0.25s cubic-bezier(0.16,1,0.3,1);letter-spacing:0.06em}
.hint-val:hover{transform:translateY(-2px) scale(1.04);background:rgba(139,92,246,0.2);box-shadow:0 4px 20px rgba(139,92,246,0.2)}
.hint-val:active{transform:scale(0.95)}
.field{margin-bottom:18px;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.35s backwards}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--mid);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.08em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 44px;border-radius:12px;border:1.5px solid var(--border);background:rgba(0,0,0,0.15);color:var(--text);font-family:inherit;font-size:14.5px;outline:none;transition:all 0.3s cubic-bezier(0.16,1,0.3,1)}
[data-theme="light"] input[type=password]{background:rgba(124,58,237,0.04)}
input::placeholder{color:var(--dim)}
input:focus{border-color:var(--accent);background:rgba(139,92,246,0.06);box-shadow:0 0 0 4px rgba(139,92,246,0.08),0 8px 30px rgba(139,92,246,0.05);transform:translateY(-1px)}
.ic-lock{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:all 0.3s}
input:focus~.ic-lock{color:var(--accent);animation:lockWiggle 0.4s ease}
@keyframes lockWiggle{0%,100%{transform:translateY(-50%) rotate(0)}25%{transform:translateY(-50%) rotate(-10deg)}75%{transform:translateY(-50%) rotate(10deg)}}
.ic-eye{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;cursor:pointer;padding:6px;transition:all 0.3s;line-height:0;border-radius:8px}
.ic-eye:hover{color:var(--accent);background:rgba(139,92,246,0.08);transform:translateY(-50%) scale(1.15)}
.err{display:none;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);border-radius:12px;padding:12px 16px;margin-bottom:16px;font-size:12.5px;color:#F87171;align-items:center;gap:10px;animation:shake 0.4s cubic-bezier(0.16,1,0.3,1)}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-8px)}40%{transform:translateX(8px)}60%{transform:translateX(-4px)}80%{transform:translateX(4px)}}
.btn{width:100%;padding:14px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,#8B5CF6,#6D28D9,#5B21B6);background-size:200% 200%;color:#fff;font-family:inherit;font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:9px;box-shadow:0 8px 30px rgba(139,92,246,0.4);transition:all 0.3s cubic-bezier(0.16,1,0.3,1);position:relative;overflow:hidden;animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.4s backwards,gradientMove 4s ease infinite}
@keyframes gradientMove{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,0.15),transparent);width:60%;transform:translateX(-200%);transition:transform 0.6s}
.btn:hover::before{transform:translateX(300%)}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 40px rgba(139,92,246,0.5)}
.btn:active{transform:translateY(0) scale(0.98)}
.btn:disabled{opacity:0.5;cursor:not-allowed;transform:none}
.btn .ripple{position:absolute;border-radius:50%;background:rgba(255,255,255,0.3);transform:scale(0);animation:rippleAnim 0.6s linear}
@keyframes rippleAnim{to{transform:scale(4);opacity:0}}
.footer{margin-top:24px;padding-top:20px;border-top:1px solid var(--border);display:flex;flex-direction:column;align-items:center;gap:6px;font-size:11px;color:var(--dim);animation:fadeUp 0.6s cubic-bezier(0.16,1,0.3,1) 0.5s backwards}
.footer .row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center}
.footer a{color:var(--accent);font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:4px;transition:all 0.3s}
.footer a:hover{filter:brightness(1.2);transform:translateY(-1px)}
.footer .credit{font-size:9px;color:var(--dim);opacity:0.6}
@keyframes spin{to{transform:rotate(360deg)}}
.theme-switch{position:fixed;top:20px;left:20px;z-index:50}
.theme-btn{width:42px;height:42px;border-radius:12px;background:var(--card);border:1px solid var(--border);color:var(--mid);display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;backdrop-filter:blur(16px);transition:all 0.4s cubic-bezier(0.16,1,0.3,1)}
.theme-btn:hover{transform:rotate(30deg) scale(1.1);border-color:var(--accent);color:var(--accent2)}
@media(max-width:420px){.card{padding:30px 22px 24px;border-radius:18px}.hint{flex-wrap:wrap}.footer .row{font-size:10px}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="particles" id="particles"></div>
<div class="orb orb1"></div><div class="orb orb2"></div>
<div class="theme-switch"><button class="theme-btn" id="theme-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon"></i></button></div>
<div class="wrap"><div class="card">
  <div class="brand">
    <div class="brand-icon"><i class="ti ti-brand-azure"></i></div>
    <div><div class="brand-name">Purple-Panel</div><div class="brand-sub">v<span class="ver">1.1</span></div></div>
  </div>
  <h1>ورود به پنل</h1>
  <p class="sub">رمز عبور را برای دسترسی به داشبورد مدیریت وارد کنید</p>
  <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
  <div class="hint"><i class="ti ti-info-circle"></i><span class="hint-label">رمز پیش‌فرض</span><span class="hint-val" onclick="fillDefault()" tabindex="0">PurplePanel</span></div>
  <form id="form">
    <div class="field"><label>رمز عبور</label><div class="inp-wrap">
      <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required autocomplete="current-password">
      <i class="ti ti-lock ic-lock"></i>
      <i class="ti ti-eye ic-eye" id="eye-toggle" onclick="togglePw()"></i>
    </div></div>
    <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
  </form>
  <div class="footer">
    <div class="row">✨ کاستوم‌سازی: <a href="https://t.me/AghaBanafshi" target="_blank">@AghaBanafshi</a></div>
    <div class="row">📱 پشتیبانی: <a href="https://t.me/AghaBanafshiipvbot" target="_blank">@AghaBanafshiipvbot</a></div>
    <div class="row"><span class="credit">کانال: <a href="https://t.me/X4GHUB" target="_blank">@X4GHUB</a></span></div>
  </div>
</div></div>
<script>
let isDark=localStorage.getItem('pp-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon')}
function toggleTheme(){isDark=!isDark;localStorage.setItem('pp-theme',isDark?'dark':'light');applyTheme(isDark);const b=document.getElementById('theme-btn');b.style.transform='rotate(30deg) scale(1.1)';setTimeout(()=>b.style.transform='',400)}
applyTheme(isDark);
function fillDefault(){document.getElementById('pw').value='PurplePanel';document.getElementById('pw').focus()}
function togglePw(){const p=document.getElementById('pw'),e=document.getElementById('eye-toggle');const s=p.type==='password';p.type=s?'text':'password';e.className='ti '+(s?'ti-eye-off':'ti-eye')+' ic-eye'}
(function(){const box=document.getElementById('particles');for(let i=0;i<25;i++){const p=document.createElement('div');p.className='particle';const s=2+Math.random()*4;p.style.width=s+'px';p.style.height=s+'px';p.style.left=Math.random()*100+'vw';p.style.setProperty('--drift',(Math.random()*80-40)+'px');p.style.animationDuration=(12+Math.random()*18)+'s';p.style.animationDelay=(Math.random()*15)+'s';box.appendChild(p)}})();
document.querySelector('.btn')?.addEventListener('click',function(e){if(this.disabled)return;const r=document.createElement('span');r.className='ripple';const rect=this.getBoundingClientRect();const x=e.clientX-rect.left,y=e.clientY-rect.top;r.style.left=x+'px';r.style.top=y+'px';r.style.width='20px';r.style.height='20px';this.appendChild(r);setTimeout(()=>r.remove(),600)});
document.getElementById('form').addEventListener('submit',async e=>{e.preventDefault();const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');err.classList.remove('show');btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';try{const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا')}location.href='/dashboard'}catch(e){et.textContent=e.message;err.classList.add('show');btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد'}});
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
  --card:#1a0d30;--card-b:rgba(139,92,246,0.15);--card-bh:rgba(139,92,246,0.35);
  --accent:#8B5CF6;--accent2:#A78BFA;--accent-d:rgba(139,92,246,0.12);
  --green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FCD34D;
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.12);
  --t1:#F0E8FF;--t2:#9C8ABF;--t3:#6D4A9E;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.45);
  --glow:rgba(139,92,246,0.08);
}
[data-theme="light"]{
  --bg:#F5F0FF;--bg2:#EBE0FF;--bg3:#DFD0FF;
  --card:#FFFFFF;--card-b:rgba(139,92,246,0.18);--card-bh:rgba(139,92,246,0.35);
  --accent:#7C3AED;--accent2:#6D28D9;--accent-d:rgba(124,58,237,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);
  --t1:#1A0E30;--t2:#4A2D6E;--t3:#7A5DA6;
  --shadow:0 4px 20px rgba(80,40,160,0.12);
  --glow:rgba(124,58,237,0.05);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .6s ease,color .6s ease;position:relative}
body::before{content:'';position:fixed;inset:0;z-index:-1;background:radial-gradient(ellipse 60% 40% at 20% 10%,var(--glow),transparent 70%),radial-gradient(ellipse 40% 30% at 90% 90%,var(--glow),transparent 65%),var(--bg);transition:background .8s ease;animation:bodyGlow 15s ease-in-out infinite}
@keyframes bodyGlow{0%,100%{opacity:0.7}50%{opacity:1}}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .6s ease,border-color .6s ease;backdrop-filter:blur(20px)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 0 30px rgba(139,92,246,0.3);animation:logoPulse 3s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 30px rgba(139,92,246,0.3)}50%{box-shadow:0 0 50px rgba(139,92,246,0.5)}}
.logo-name{font-size:14px;font-weight:800;color:var(--t1);letter-spacing:-0.02em;background:linear-gradient(135deg,var(--t1),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px;display:flex;align-items:center;gap:4px}
.logo-sub .ver-badge{background:var(--accent-d);color:var(--accent2);padding:0 6px;border-radius:10px;font-size:8px;font-weight:700}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .25s cubic-bezier(.16,1,.3,1);margin:1px 6px;border-radius:8px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2);transform:translateX(-3px)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:0 0 20px rgba(139,92,246,0.05)}
.nav-badge{margin-right:auto;background:rgba(139,92,246,0.2);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1);transform:scale(1.02)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:all .3s cubic-bezier(.16,1,.3,1);margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1);transform:translateY(-2px)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:all .3s cubic-bezier(.16,1,.3,1);margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2);transform:translateY(-2px)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .6s ease}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;flex-shrink:0}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1)}
.menu-btn:hover,.theme-mob:hover{transform:scale(1.1);background:var(--card-b)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px);animation:fadeIn .3s ease}
.overlay.show{display:block}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none;animation:pageIn .5s cubic-bezier(.16,1,.3,1)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-0.02em}
.tb-title i{color:var(--accent);font-size:20px;animation:titleIconPulse 3s ease-in-out infinite}
@keyframes titleIconPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap;transition:all .3s ease}
.badge:hover{transform:scale(1.05)}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .3s cubic-bezier(.16,1,.3,1);position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.3s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
.metric .m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px;transition:transform .3s ease}
.metric:hover .m-icon{transform:scale(1.1) rotate(-5deg)}
.metric .m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.metric .m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.metric .m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.metric .m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}

.changelog-section{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;margin-bottom:18px;transition:all .3s cubic-bezier(.16,1,.3,1)}
.changelog-section:hover{border-color:var(--card-bh);box-shadow:var(--shadow)}
.changelog-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.changelog-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.changelog-title i{color:var(--accent);font-size:18px}
.changelog-badge{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#fff;padding:2px 12px;border-radius:20px;font-size:9px;font-weight:700;animation:badgeGlow 2s ease-in-out infinite}
@keyframes badgeGlow{0%,100%{box-shadow:0 0 10px rgba(139,92,246,0.3)}50%{box-shadow:0 0 25px rgba(139,92,246,0.6)}}
.cl-item{display:flex;gap:12px;padding:10px 0;border-bottom:1px solid rgba(139,92,246,0.05);animation:clItemIn 0.5s cubic-bezier(.16,1,.3,1) backwards}
.cl-item:last-child{border-bottom:none}
.cl-item:nth-child(1){animation-delay:0.05s}
.cl-item:nth-child(2){animation-delay:0.1s}
.cl-item:nth-child(3){animation-delay:0.15s}
.cl-item:nth-child(4){animation-delay:0.2s}
.cl-item:nth-child(5){animation-delay:0.25s}
@keyframes clItemIn{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}
.cl-icon{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.cl-icon.add{background:var(--green-bg);color:var(--green-t)}
.cl-icon.fix{background:var(--amber-bg);color:var(--amber-t)}
.cl-icon.improve{background:var(--accent-d);color:var(--accent2)}
.cl-icon.remove{background:var(--red-bg);color:var(--red-t)}
.cl-content{flex:1;min-width:0}
.cl-content .cl-title{font-size:12px;font-weight:700;color:var(--t1)}
.cl-content .cl-desc{font-size:10.5px;color:var(--t3);line-height:1.7}
.cl-version{font-size:9px;font-weight:700;color:var(--accent2);background:var(--accent-d);padding:1px 8px;border-radius:10px;white-space:nowrap}

.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(139,92,246,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:all .3s cubic-bezier(.16,1,.3,1)}
.vless-box:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(0,0,0,0.4)}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;animation:glowFloat 8s ease-in-out infinite}
@keyframes glowFloat{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,20px)}}
.vl-code{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em;transition:all .3s ease}
.vl-code:hover{background:rgba(139,92,246,0.05);border-color:var(--card-bh)}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .3s cubic-bezier(.16,1,.3,1);white-space:nowrap}
.btn i{font-size:13px}
.btn:hover{transform:translateY(-2px)}
.btn:active{transform:scale(0.95)}
.btn-p{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#fff;box-shadow:0 4px 20px rgba(139,92,246,0.3)}
.btn-p:hover{box-shadow:0 8px 30px rgba(139,92,246,0.4)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(139,92,246,.15)}
.btn-g:hover{background:rgba(139,92,246,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(139,92,246,.3)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:all .3s cubic-bezier(.16,1,.3,1)}
.card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(139,92,246,0.05);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px;animation:chartIn 0.8s cubic-bezier(.16,1,.3,1)}
@keyframes chartIn{from{opacity:0;transform:scale(0.95)}to{opacity:1;transform:scale(1)}}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600;transition:all .3s ease}
.df-link:hover{color:var(--accent);transform:translateX(-3px)}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s cubic-bezier(.16,1,.3,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option><option value="firefox">firefox</option>
          <option value="safari">safari</option><option value="ios">ios</option>
          <option value="android">android</option><option value="edge">edge</option>
          <option value="360">360</option><option value="qq">qq</option>
          <option value="random">random</option><option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-link-chart">
  <div class="modal" style="max-width:640px">
    <button class="modal-close" onclick="closeModal('modal-link-chart')"><i class="ti ti-x"></i></button>
    <div class="modal-title" id="lc-title"><i class="ti ti-chart-line"></i> نمودار مصرف</div>
    <div style="height:280px;margin-top:10px"><canvas id="lc-canvas"></canvas></div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><i class="ti ti-brand-azure"></i></div>
    <span class="mob-title">Purple-Panel</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-icon"><i class="ti ti-brand-azure"></i></div>
    <div><div class="logo-name">Purple-Panel</div><div class="logo-sub">v<span class="ver-badge">1.1</span></div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="changelog"><i class="ti ti-list-tree"></i> تغییرات</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  
  <div class="changelog-section" id="changelog-section">
    <div class="changelog-header">
      <div class="changelog-title"><i class="ti ti-list-tree"></i> تغییرات نسخه ۱.۱ <span class="changelog-badge">جدید</span></div>
      <span style="font-size:10px;color:var(--t3)">آخرین بروزرسانی: مرداد ۱۴۰۴</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon add"><i class="ti ti-plus"></i></div>
      <div class="cl-content">
        <div class="cl-title">انیمیشن‌های حرفه‌ای</div>
        <div class="cl-desc">افکت‌های ورود، hover، پارتکل‌های پس‌زمینه و انتقال‌های روان به تمام صفحات اضافه شد</div>
      </div>
      <span class="cl-version">v1.1</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon add"><i class="ti ti-plus"></i></div>
      <div class="cl-content">
        <div class="cl-title">بخش تغییرات (Changelog)</div>
        <div class="cl-desc">لیست کامل تغییرات نسخه‌های مختلف پنل به‌صورت گرافیکی نمایش داده می‌شود</div>
      </div>
      <span class="cl-version">v1.1</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon improve"><i class="ti ti-arrow-up"></i></div>
      <div class="cl-content">
        <div class="cl-title">طراحی مدرن و شیشه‌ای</div>
        <div class="cl-desc">استفاده از افکت Glassmorphism، گرادیان‌های روان و هدرهای نئونی برای ظاهری حرفه‌ای‌تر</div>
      </div>
      <span class="cl-version">v1.1</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon improve"><i class="ti ti-arrow-up"></i></div>
      <div class="cl-content">
        <div class="cl-title">حالت شب/روز پیشرفته</div>
        <div class="cl-desc">انتقال رنگ‌ها با انیمیشن روان و حفظ تنظیمات در مرورگر</div>
      </div>
      <span class="cl-version">v1.1</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon fix"><i class="ti ti-bug"></i></div>
      <div class="cl-content">
        <div class="cl-title">بهبود عملکرد و ریسپانسیو</div>
        <div class="cl-desc">بهینه‌سازی برای موبایل و تبلت، رفع باگ‌های جزئی</div>
      </div>
      <span class="cl-version">v1.1</span>
    </div>
  </div>

  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric dan" style="cursor:pointer" onclick="navTo('errors')"><div class="m-icon dan"><i class="ti ti-alert-triangle"></i></div><div class="m-label">خطاها</div><div class="m-val" id="m-errs">—</div><div class="m-sub">از راه‌اندازی</div></div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · mode: auto</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">Purple-Panel v1.1</span>
    <div style="display:flex;gap:6px;font-size:9px;color:var(--t3);align-items:center;flex-wrap:wrap">
      <span>✨ <a href="https://t.me/AghaBanafshi" target="_blank" style="color:#A78BFA">@AghaBanafshi</a></span>
      <span>|</span>
      <span>📱 <a href="https://t.me/AghaBanafshiipvbot" target="_blank" style="color:var(--accent2)">پشتیبانی</a></span>
    </div>
    <div style="font-size:9px;color:var(--t3);margin-top:4px">
      🟣 <a href="https://github.com/TheAghaBanafshi" target="_blank" style="color:var(--accent2)">github.com/TheAghaBanafshi</a>
    </div>
    <a class="df-link" href="https://t.me/X4GHUB" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/X4GHUB</a>
  </div>
</section>

<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه و انقضا</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)"></div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-calendar-due"></i> انقضا</div>
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود"></div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp">XHTTP Ultra · mode: auto</option>
        </select>
        <div class="proto-cards" style="grid-template-columns:repeat(2,1fr)">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp" onclick="selectProto('xhttp',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · mode: auto</div>
            <div class="proto-card-desc">انتخاب خودکار packet-up/stream-up</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option><option value="firefox">firefox</option>
            <option value="safari">safari</option><option value="ios">ios</option>
            <option value="android">android</option><option value="edge">edge</option>
            <option value="360">360</option><option value="qq">qq</option>
            <option value="random">random</option><option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none"></div>
        </div>
      </div>
      <div class="cp-row mb16" style="grid-template-columns:1fr">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر هم‌زمان</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>

<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>

<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth سخت‌گیرانه</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کانفیگ</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک ساب</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>

<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>

<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>

<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>

<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت پیش‌فرض</div><div class="srv-tile-val">443 (TLS) · قابل تغییر در هر کانفیگ</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.1</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>

<section class="pg" id="pg-changelog">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-list-tree"></i> تغییرات نسخه‌ها</div><div class="tb-sub">تاریخچه کامل بروزرسانی‌های Purple-Panel</div></div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-list-tree"></i> لاگ تغییرات</div>
    <div class="cl-item">
      <div class="cl-icon add"><i class="ti ti-plus"></i></div>
      <div class="cl-content">
        <div class="cl-title">نسخه ۱.۱ - انیمیشن‌ها و بخش تغییرات</div>
        <div class="cl-desc">افکت‌های حرفه‌ای، پارتکل‌های پس‌زمینه، بخش Changelog، طراحی شیشه‌ای، حالت شب/روز پیشرفته</div>
      </div>
      <span class="cl-version">مرداد ۱۴۰۴</span>
    </div>
    <div class="cl-item">
      <div class="cl-icon add"><i class="ti ti-plus"></i></div>
      <div class="cl-content">
        <div class="cl-title">نسخه ۱.۰ - انتشار اولیه</div>
        <div class="cl-desc">پنل مدیریت کانفیگ با طراحی بنفش، ربات تلگرام، سیستم ساب‌اسکریپشن و مدیریت کانفیگ‌ها</div>
      </div>
      <span class="cl-version">تیر ۱۴۰۴</span>
    </div>
  </div>
</section>

</main>
<script>
let isDark=localStorage.getItem('pp-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';document.getElementById('theme-icon').className='ti '+icon;document.getElementById('theme-label').textContent=label;const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;}
function toggleTheme(){isDark=!isDark;localStorage.setItem('pp-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400);}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';const d=daysLeft(exp);if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(d<=3)return '<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+toFa(d)+' روز مانده</span>';return '<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+toFa(d)+' روز مانده</span>';}
function protoBadge(p){const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp':['XHTTP · auto','pc-xhttp']};const v=m[p]||m['vless-ws'];return '<span class="proto-chip '+v[1]+'">'+v[0]+'</span>';}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r;}
function setQuota(val,unit,el){document.getElementById('nl-val').value=val===0?'':val;document.getElementById('nl-unit').value=unit;document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setExpiry(days,el){document.getElementById('nl-exp').value=days===0?'':days;document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function selectProto(val,el){document.getElementById('nl-proto').value=val;document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setIpLimit(n,el){document.getElementById('nl-iplimit').value=n;document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setSpeedLimit(n,el){document.getElementById('nl-speed').value=n;document.getElementById('nl-speed-unit').value='MBIT';document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function onAlpnPresetChange(){const p=document.getElementById('nl-alpn-preset').value;const inp=document.getElementById('nl-alpn');if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}else{inp.style.display='none';inp.value=p;}}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,logs:loadActivity};if(loaders[name])loaders[name]();closeSb();window.scrollTo({top:0,behavior:'smooth'});}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){try{const r=await authF('/stats'),d=await r.json();document.getElementById('m-conns').textContent=d.active_connections;document.getElementById('conns-nb').textContent=d.active_connections;document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';document.getElementById('m-alinks').textContent=d.active_links??'—';document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';document.getElementById('m-errs').textContent=d.total_errors??'—';document.getElementById('errs-badge').textContent=d.total_errors+' خطا';document.getElementById('uptime-inline').textContent=d.uptime;document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));document.getElementById('bw-pct').textContent=pct+'%';document.getElementById('bw-bar').style.width=pct+'%';prevTraf=d.total_traffic_mb;if(d.hourly){const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));[ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}}renderErrs(d.recent_errors||[]);}catch(e){console.error(e)}}
function renderErrs(errs){const el=document.getElementById('errs-full');if(!el)return;if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}el.innerHTML=errs.slice().reverse().map(e=>'<div class="erow"><div class="etime"><i class="ti ti-clock"></i>'+new Date(e.time).toLocaleString('fa-IR')+'</div><div class="emsg">'+esc(e.error)+(e.url?' — '+esc(e.url):'')+'</div></div>').join('');}
async function loadActivity(){try{const r=await authF('/api/activity'),d=await r.json();const logs=(d.logs||[]).slice().reverse();const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');if(!logs.length){el.innerHTML='';em.style.display='block';return}em.style.display='none';const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};el.innerHTML=logs.map(l=>'<div class="log-item"><div class="log-ic '+l.level+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="log-body"><div class="log-msg">'+esc(l.message)+'</div><div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('fa-IR')+' <span class="log-kind">'+(kindFa[l.kind]||l.kind)+'</span></div></div></div>').join('');}catch(e){console.error(e)}}
let allLinksList=[];
async function loadLinks(){try{const r=await authF('/api/links');const {links=[]}=await r.json();allLinksList=links;document.getElementById('links-nb').textContent=links.length;document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';document.getElementById('lsummary-badge').textContent=toFa(links.length);document.getElementById('lsummary').innerHTML=links.length?links.slice(0,6).map(l=>'<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:'+(l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)')+'"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div>').join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');if(!links.length){grid.innerHTML='';empty.style.display='block';return}empty.style.display='none';grid.innerHTML=links.map(l=>{const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';const allowed=l.active&&!l.expired;const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');return '<div class="cfg-card '+cardCls+'"><div class="cfg-row"><span class="cfg-status-dot '+(allowed?'pulse':'')+'"></span><div class="cfg-identity"><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-sub-meta"><span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(()=>toast(\'UUID کپی شد\',\'ok\'))" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'…</span><span>'+new Date(l.created_at).toLocaleDateString('fa-IR')+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-usage-col"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+fmtB(l.used_bytes)+'</span><span>از '+lim+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-exp-col">'+expChip(l.expires_at,l.expired)+'</div><div class="cfg-divider-v"></div><div class="cfg-badges-col">'+protoBadge(l.protocol)+'<span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :'+(l.port||443)+'</span><span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> '+esc(l.fingerprint||'chrome')+'</span><span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> '+(l.connected_ips||0)+(l.ip_limit?('/'+l.ip_limit):' (∞)')+'</span><span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> '+(l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود')+'</span></div><div class="cfg-divider-v"></div><div class="cfg-actions"><button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+(!l.active)+')" title="فعال/غیرفعال"></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link)+'\').then(()=>toast(\'لینک کپی شد\',\'ok\'))" title="کپی لینک"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="window.open(\''+esc(l.sub_url)+'\',\'_blank\')" title="باز کردن داشبورد ساب"><i class="ti ti-rss"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="openLinkChart(\''+l.uuid+'\',\''+esc(l.label)+'\')" title="نمودار مصرف ۳۰ روز اخیر"><i class="ti ti-chart-line"></i></button><button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="resetUsage(\''+l.uuid+'\')" title="ریست مصرف"><i class="ti ti-rotate"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button></div></div></div>';}).join('');}catch(e){console.error(e)}}
let linkChart=null;
async function openLinkChart(uuid,label){document.getElementById('lc-title').textContent='نمودار مصرف ۳۰ روز اخیر — '+label;openModal('modal-link-chart');try{const r=await authF('/api/links/'+uuid+'/history'),d=await r.json();const labels=d.days.map(x=>x.date.slice(5));const vals=d.days.map(x=>+(x.bytes/1024**2).toFixed(2));const ctx=document.getElementById('lc-canvas');if(linkChart)linkChart.destroy();linkChart=new Chart(ctx,{type:'bar',data:{labels,datasets:[{label:'مصرف (MB)',data:vals,backgroundColor:'rgba(139,92,246,.55)',borderRadius:5,maxBarThickness:22}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{beginAtZero:true}}}});}catch(e){toast('خطا در دریافت تاریخچه مصرف','err')}}
async function createLink(){const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';const val=document.getElementById('nl-val').value;const unit=document.getElementById('nl-unit').value;const exp=document.getElementById('nl-exp').value;const note=document.getElementById('nl-note').value.trim();const protocol=document.getElementById('nl-proto').value||'vless-ws';const fingerprint=document.getElementById('nl-fp').value||'chrome';const alpn=document.getElementById('nl-alpn').value.trim();const port=443;const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;const speed_limit_unit=document.getElementById('nl-speed-unit').value;try{const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});if(!r.ok)throw new Error('failed');['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');document.getElementById('nl-iplimit').value='0';document.getElementById('nl-speed').value='0';document.getElementById('nl-alpn-preset').value='';document.getElementById('nl-alpn').style.display='none';toast('کانفیگ ساخته شد ✓','ok');loadLinks();}catch(e){toast('خطا در ساخت','err')}}
function openEditLink(uuid){const l=allLinksList.find(x=>x.uuid===uuid);if(!l)return;document.getElementById('el-uuid').value=uuid;document.getElementById('el-label').value=l.label;document.getElementById('el-note').value=l.note||'';if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}document.getElementById('el-exp').value='';document.getElementById('el-fp').value=l.fingerprint||'chrome';document.getElementById('el-alpn').value=l.alpn||'';document.getElementById('el-port').value=l.port||443;document.getElementById('el-iplimit').value=l.ip_limit||0;if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}openModal('modal-edit-link');}
async function saveEditLink(){const uuid=document.getElementById('el-uuid').value;const label=document.getElementById('el-label').value.trim();const note=document.getElementById('el-note').value.trim();const val=document.getElementById('el-val').value;const unit=document.getElementById('el-unit').value;const exp=document.getElementById('el-exp').value;const fingerprint=document.getElementById('el-fp').value||'chrome';const alpn=document.getElementById('el-alpn').value.trim();const port=Number(document.getElementById('el-port').value)||443;const ip_limit=Number(document.getElementById('el-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('el-speed').value)||0;const speed_limit_unit=document.getElementById('el-speed-unit').value;const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};if(exp&&Number(exp)>0)body.expires_days=Number(exp);try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-edit-link');toast('کانفیگ ویرایش شد ✓','ok');loadLinks();}catch(e){toast('خطا در ویرایش','err')}}
async function toggleActive(uuid,newState){try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}}
async function resetUsage(uuid){try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
async function deleteLink(uuid){if(!confirm('حذف این کانفیگ؟'))return;try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
function parseBytesFmt(s){if(!s)return 0;const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);if(!m)return 0;const n=parseFloat(m[1]),u=m[2].toUpperCase();const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};return n*(mult[u]||1);}
let connsExpanded=new Set();
function toggleConnCard(uuid){if(connsExpanded.has(uuid))connsExpanded.delete(uuid);else connsExpanded.add(uuid);renderConnsGrid(window.__lastConfigs||[]);}
function renderConnsGrid(configs){const grid=document.getElementById('conns-grid');grid.innerHTML=configs.map(cfg=>{const open=connsExpanded.has(cfg.uuid);const ipsHtml=(cfg.connections||[]).map(c=>{const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';return '<div style="display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:10px;background:var(--accent-d);border:1px solid var(--card-b);margin-top:7px"><div style="display:flex;align-items:center;gap:8px;min-width:0"><i class="ti ti-device-desktop" style="color:var(--t3)"></i><span style="font-family:ui-monospace,monospace;font-size:12px;color:var(--t1)">'+esc(c.ip)+'</span><button class="conn-ip-copy" onclick="navigator.clipboard.writeText(\''+esc(c.ip)+'\').then(()=>toast(\'IP کپی شد\',\'ok\'))" title="کپی IP"><i class="ti ti-copy"></i></button></div><div style="display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);flex-shrink:0"><span><i class="ti ti-repeat" style="font-size:10px"></i> '+toFa(c.sessions)+' سشن</span><span><i class="ti ti-transfer" style="font-size:10px"></i> '+esc(c.bytes_fmt)+'</span><span><i class="ti ti-clock" style="font-size:10px"></i> '+dur+'</span></div></div>';}).join('')||'<div style="padding:10px;color:var(--t3);font-size:11px">اتصالی نیست</div>';return '<div class="conn-card-v2" style="cursor:pointer" onclick="toggleConnCard(\''+cfg.uuid+'\')"><div class="conn-card-v2-glow"></div><div class="conn-card-v2-top"><div class="conn-avatar"><i class="ti ti-key"></i></div><div class="conn-card-v2-id"><div class="conn-ip-v2">'+esc(cfg.label)+'</div><div class="conn-label-v2">'+toFa(cfg.ip_count)+' آی‌پی · '+toFa(cfg.sessions)+' سشن</div></div><span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span></div><div class="conn-card-v2-divider"></div><div class="conn-card-v2-body"><div class="conn-proto-row">'+protoBadge(cfg.protocol)+'</div><div class="conn-stat-row"><div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">ترافیک</div><div class="conn-stat-text-val">'+esc(cfg.bytes_fmt)+'</div></div></div><div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-users"></i></div><div><div class="conn-stat-text-label">آی‌پی‌های متصل</div><div class="conn-stat-text-val">'+toFa(cfg.ip_count)+'</div></div></div></div><div style="text-align:center;font-size:10.5px;color:var(--accent2);margin-top:8px"><i class="ti ti-chevron-'+(open?'up':'down')+'"></i> '+(open?'بستن':'نمایش اتصالات')+'</div>'+(open?'<div onclick="event.stopPropagation()">'+ipsHtml+'</div>':'')+'</div></div>';}).join('');}
async function loadConns(){try{const r=await authF('/api/connections'),d=await r.json();const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.raw_count+' اتصال';document.getElementById('ch-count').textContent=toFa(d.raw_count);const configs=d.configs||[];window.__lastConfigs=configs;if(!configs.length){grid.innerHTML='';ce.style.display='block';document.getElementById('ch-traffic').textContent='—';document.getElementById('ch-avgdur').textContent='—';document.getElementById('ch-uniq').textContent='—';return;}ce.style.display='none';const totalBytes=configs.reduce((s,c)=>s+(c.bytes||0),0);document.getElementById('ch-traffic').textContent=fmtB(totalBytes);const uniqIps=configs.reduce((s,c)=>s+c.ip_count,0);document.getElementById('ch-uniq').textContent=toFa(uniqIps);const allDurs=[];configs.forEach(c=>(c.connections||[]).forEach(ip=>allDurs.push(ip.connected_at?Math.max(0,Math.floor((Date.now()-new Date(ip.connected_at).getTime())/1000)):0)));const avgSec=allDurs.length?Math.floor(allDurs.reduce((a,b)=>a+b,0)/allDurs.length):0;document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';renderConnsGrid(configs);}catch(e){console.error(e)}}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();loadLinks();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}
async function changePw(){const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}if(nw!==cf){toast('تکرار رمز اشتباه','err');return}try{const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.detail||'خطا');toast('رمز تغییر کرد ✓','ok');['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');}catch(e){toast('✗ '+e.message,'err')}}
function togglePwField(id,btn){const inp=document.getElementById(id);const icon=btn.querySelector('i');const toText=inp.type==='password';inp.type=toText?'text':'password';icon.className='ti '+(toText?'ti-eye-off':'ti-eye');}
function checkPwStrength(val){const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');const label=document.getElementById('pw-strength-label');const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;reqLen.classList.toggle('met',hasLen);reqNum.classList.toggle('met',hasNum);reqCase.classList.toggle('met',hasCase);let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;const colors=['#EF4444','#F59E0B','#8B5CF6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}label.innerHTML='<i class="ti ti-shield-check" style="color:'+colors[Math.max(0,score-1)]+'"></i> '+labels[Math.max(0,score-1)];}
function makeGradient(ctx,color1,color2){const g=ctx.createLinearGradient(0,0,0,260);g.addColorStop(0,color1);g.addColorStop(1,color2);return g;}
function initCharts(){const c1=document.getElementById('ch1').getContext('2d');const grad1=makeGradient(c1,'rgba(139,92,246,.38)','rgba(139,92,246,0)');const opts={responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(20,10,40,.96)',borderColor:'rgba(139,92,246,.3)',borderWidth:1,titleColor:'#F0E8FF',bodyColor:'#9C8ABF',padding:11,cornerRadius:10,displayColors:false,titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:v=>v.parsed.y.toFixed(2)+' مگابایت'}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6D4A9E',font:{size:9,family:'Vazirmatn'}}},y:{grid:{color:'rgba(139,92,246,.06)'},border:{display:false},ticks:{color:'#6D4A9E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}},elements:{line:{capBezierPoints:true}}};const ds1={label:'MB',data:[],borderColor:'#8B5CF6',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#8B5CF6',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});function makeGradientV2(ctx,c1,c2,c3){const g=ctx.createLinearGradient(0,0,0,320);g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);return g;}const c3ctx=document.getElementById('ch3').getContext('2d');const gradFill3=makeGradientV2(c3ctx,'rgba(139,92,246,.45)','rgba(139,92,246,.08)','rgba(139,92,246,0)');ch3=new Chart(document.getElementById('ch3'),{type:'line',data:{labels:[],datasets:[{label:'مصرف',data:[],borderColor:'#8B5CF6',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#8B5CF6',pointHoverBorderWidth:3,borderWidth:3,order:2},{label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(20,10,40,.97)',borderColor:'rgba(139,92,246,.35)',borderWidth:1,titleColor:'#F0E8FF',bodyColor:'#B8A6D8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:v=>' '+v.dataset.label+': '+v.parsed.y.toFixed(2)+' MB'}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6D4A9E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},y:{grid:{color:'rgba(139,92,246,.05)'},border:{display:false},ticks:{color:'#6D4A9E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}}});ch2=new Chart(document.getElementById('ch2'),{type:'doughnut',data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{data:[55,35,10],backgroundColor:['#8B5CF6','#10B981','#6D28D9'],borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#1a0d30',borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:'72%',plugins:{legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},tooltip:{backgroundColor:'rgba(20,10,40,.96)',borderColor:'rgba(139,92,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}}});}
let ws;function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#9C8ABF',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{await checkAuth();initCharts();document.getElementById('set-host').textContent=location.host;fetchStats();loadLinks();setInterval(fetchStats,4000);setInterval(()=>{if(document.getElementById('pg-links').classList.contains('on'))loadLinks();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();},5000);});
</script>
</body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Purple-Panel Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0a0618;--bg2:#140a2a;--bg3:#1e0f3a;--card:#1a0d30;--card-b:rgba(139,92,246,0.15);--card-bh:rgba(139,92,246,0.35);--accent:#8B5CF6;--accent2:#A78BFA;--accent-d:rgba(139,92,246,0.1);--green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FCD34D;--purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.12);--t1:#F0E8FF;--t2:#9C8ABF;--t3:#6D4A9E;--radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);--serif:'Vazirmatn',sans-serif;}}
[data-theme="light"]{{--bg:#F5F0FF;--bg2:#EBE0FF;--bg3:#DFD0FF;--card:#FFFFFF;--card-b:rgba(139,92,246,0.18);--card-bh:rgba(139,92,246,0.35);--accent:#7C3AED;--accent2:#6D28D9;--accent-d:rgba(124,58,237,0.08);--green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;--red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;--amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;--purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);--t1:#1A0E30;--t2:#4A2D6E;--t3:#7A5DA6;--shadow:0 12px 36px rgba(80,40,160,0.12);}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(139,92,246,0.12),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(139,92,246,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,0.025) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-icon{{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 0 20px rgba(139,92,246,.35)}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;background:linear-gradient(135deg,var(--t1),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}
.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(139,92,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}
.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,#8B5CF6 0%,#6D28D9 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(139,92,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#6D28D9;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}
.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(139,92,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}
.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(124,58,237,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#fff;box-shadow:0 3px 14px rgba(139,92,246,.35)}}
.btn-p:hover{{background:var(--accent2)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(139,92,246,.16)}}
.btn-g:hover{{background:rgba(139,92,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(139,92,246,.16),rgba(139,92,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(124,58,237,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}
.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}
.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}
.footer .credit{{font-size:9px;color:var(--t3);opacity:0.6}}
@media(max-width:520px){{.stats-bar{{grid-template-columns:1fr 1fr}}.stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}.sub-name{{font-size:19px}}.copy-all-bar{{flex-direction:column;align-items:stretch}}.copy-all-btn{{justify-content:center}}.wrap{{padding:16px 12px 50px}}.lock-banner{{padding:32px 22px 22px}}.lock-form{{padding:20px 22px 26px}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-icon"><i class="ti ti-brand-azure"></i></div>
      <div><div class="brand-name">Purple-Panel</div><div class="brand-sub">v1.1</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
      <a class="icon-btn" href="https://t.me/X4GHUB" target="_blank" title="کانال تلگرام"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">
    <span>✨ کاستوم‌سازی: <a href="https://t.me/AghaBanafshi" target="_blank">@AghaBanafshi</a></span>
    <div class="credit">🟣 <a href="https://github.com/TheAghaBanafshi" target="_blank">github.com/TheAghaBanafshi</a></div>
    <span>پشتیبانی: <a href="https://t.me/AghaBanafshiipvbot" target="_blank">@AghaBanafshiipvbot</a> · <a href="https://t.me/X4GHUB" target="_blank">@X4GHUB</a></span>
  </div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';
let isDark=localStorage.getItem('pp-pub-theme')!=='light';
function applyTheme(dark){{document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('pp-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(msg,type=''){{const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400);}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp"><i class="ti ti-bolt"></i> XHTTP · auto</span>';return '<span class="proto-chip pc-ws">VLESS · WS</span>';}}
function showQR(label,link){{document.getElementById('qr-label').textContent=label;document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);document.getElementById('qr-modal').classList.add('open');}}
function toggleLink(i){{const wrap=document.getElementById('vw-'+i);const btn=document.getElementById('vt-'+i);const open=wrap.classList.toggle('open');btn.classList.toggle('open',open);btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';}}
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json();}}
function renderLock(name,errMsg=''){{document.getElementById('root').innerHTML=`<div class="lock-stage"><div class="lock-card"><div class="lock-banner"><div class="lock-shield"><i class="ti ti-shield-lock"></i></div><div class="lock-title">${{esc(name)}}</div><div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div></div><div class="lock-form"><div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div><div class="lock-field"><i class="ti ti-lock lock-lockicon"></i><input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus><button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button></div><button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button></div><div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div></div></div>`;const inp=document.getElementById('lock-pw');inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});}}
function togglePwVis(){{const inp=document.getElementById('lock-pw');const icon=document.getElementById('lock-eye-icon');const toText = inp.type==='password';inp.type = toText ? 'text' : 'password';icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');}}
async function submitLock(){{const pw=document.getElementById('lock-pw').value;const data=await loadData(pw);if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}savedPw=pw;renderContent(data);}}
function renderContent(d){{const activeCount=d.links.filter(l=>l.active).length;const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/p/' + UUID_KEY);const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');window._ppSubUrl = subUrl;window._ppSubName = d.name;window._ppLinks = d.links.map(l => ({{vless:l.vless_link,sub:l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),label:l.label,used_fmt:l.used_fmt||fmtB(l.used_bytes||0),limit_bytes:l.limit_bytes||0,active:l.active,protocol:l.protocol,connections:l.connections||0,expiry_date:l.expiry_date||null,used_bytes:l.used_bytes||0}}));let totalUsed=0,totalLimit=0,hasUnlimited=false,expiryDate=null;d.links.forEach(l=>{{totalUsed += (l.used_bytes||0);if(l.limit_bytes&&l.limit_bytes>0){{totalLimit += l.limit_bytes;}}else{{hasUnlimited=true;}}if(l.expiry_date&&(!expiryDate||new Date(l.expiry_date)<new Date(expiryDate))){{expiryDate=l.expiry_date;}}}});const tuPct=totalLimit>0?Math.min(100,(totalUsed/totalLimit)*100):0;const tuColor=tuPct>90?'var(--red)':tuPct>70?'var(--amber)':'var(--green)';const tuLimitTxt=totalLimit>0?fmtB(totalLimit)+(hasUnlimited?' + نامحدود':''):'نامحدود';const totalUsageHtml=`<div class="total-usage-box" style="background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:14px 16px;margin-top:12px"><div class="tu-head" style="display:flex;align-items:center;justify-content:space-between;margin-bottom:9px;gap:8px;flex-wrap:wrap"><span class="tu-label" style="font-size:10.5px;color:var(--t2);font-weight:700;display:flex;align-items:center;gap:6px"><i class="ti ti-chart-donut-2" style="color:var(--accent2);font-size:14px"></i>مصرف کل گروه</span><span class="tu-val" style="font-size:11.5px;font-weight:800;color:var(--t1);font-family:ui-monospace,monospace">${{fmtB(totalUsed)}} <span style="color:var(--t3);font-weight:600"> / ${{tuLimitTxt}}</span></span></div><div class="tu-bar" style="height:9px;border-radius:6px;background:rgba(139,92,246,0.12);overflow:hidden;position:relative"><div class="tu-bar-f" style="width:${{totalLimit>0?tuPct:100}}%;height:100%;border-radius:6px;background:${{totalLimit>0?tuColor:'var(--accent)'}};transition:width .6s ease;position:relative;overflow:hidden"></div></div><div class="tu-foot" style="display:flex;justify-content:space-between;margin-top:7px;font-size:9.5px;color:var(--t3)"><span>${{totalLimit>0?('<span style=\\"font-weight:800\\">'+tuPct.toFixed(1)+'%</span> مصرف‌شده'):'بدون سقف کل (شامل کانفیگ نامحدود)'}}</span><span>${{toFa(d.links.length)}} کانفیگ</span></div></div>`;document.getElementById('root').innerHTML=`<div class="sub-info"><div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div><div class="sub-name">${{esc(d.name)}}</div>${{d.desc?`<div class="sub-desc">${{esc(d.desc)}}</div>`:''}}<div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div><div class="sub-sub-box"><span class="sub-sub-url">${{esc(subUrl)}}</span><button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px" onclick="navigator.clipboard.writeText(window._ppSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک ساب</button><button class="btn btn-g" style="padding:7px 12px;font-size:10.5px" onclick="showQR(window._ppSubName + ' — کل گروه', window._ppSubUrl)"><i class="ti ti-qrcode"></i> QR کل</button></div>${{totalUsageHtml}}</div><div class="copy-all-bar"><div class="copy-all-text"><div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div><div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div></div><button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button></div><div class="stats-bar"><div class="stat-card"><div class="stat-label">کانفیگ‌های فعال</div><div class="stat-val">${{toFa(activeCount)}}</div><div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div></div><div class="stat-card"><div class="stat-label">اتصالات زنده</div><div class="stat-val">${{toFa(d.active_connections)}}</div><div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div></div><div class="stat-card"><div class="stat-label">کل مصرف</div><div class="stat-val" style="font-size:17px;margin-top:3px">${{totalLimit>0?fmtB(totalUsed)+' / '+fmtB(totalLimit):fmtB(totalUsed)}}</div><div class="stat-sub">${{expiryDate?'انقضا: '+new Date(expiryDate).toLocaleDateString('fa-IR'):'نامحدود'}}</div></div></div><div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div><div class="cfg-grid">${{d.links.map((l,i)=>{{const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--green)';const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);const usedFmt=l.used_fmt||fmtB(l.used_bytes);const exp=l.expiry_date?new Date(l.expiry_date).toLocaleDateString('fa-IR'):'نامحدود';return `<div class="cfg-card${l.active?'':' inactive'}"><div class="cfg-top"><div class="cfg-head"><div><div class="cfg-label">${esc(l.label)}</div><div class="cfg-badges">${protoChip(l.protocol)}${l.connections>0?`<span class="conn-chip"><span class="dot"></span> ${toFa(l.connections)} اتصال</span>`:''}${l.expiry_date?`<span class="conn-chip" style="background:var(--amber-bg);color:var(--amber-t)"><i class="ti ti-calendar"></i> ${exp}</span>`:''}</div></div><span class="cfg-status ${l.active?'ok':'no'}">${l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال'}</span></div><div class="cfg-usage"><div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div><div class="utxt"><span>${esc(usedFmt)} مصرف شده</span><span>سهمیه: ${lim}</span></div></div></div><div class="cfg-tear"></div><div class="cfg-bottom"><button class="cfg-link-toggle" id="vt-${i}" onclick="toggleLink(${i})"><span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span><i class="ti ti-chevron-down"></i></button><div class="cfg-vless-wrap" id="vw-${i}"><div class="cfg-vless-inner"><div class="cfg-vless">${esc(l.vless_link)}</div></div></div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(window._ppLinks[${i}].vless).then(()=>toast('لینک کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-g" onclick="showQR(window._ppLinks[${i}].label, window._ppLinks[${i}].vless)"><i class="ti ti-qrcode"></i> QR</button></div></div></div>`}}).join('')}}</div>`;setTimeout(()=>autoRefresh(),30000);}}
function copyAllConfigs(){{const links=window._ppLinks||[];if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}const text=links.map(l=>l.vless).join('\\n');navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));}}
async function autoRefresh(){{try{{const data=await loadData(savedPw);if(!data.locked)renderContent(data);}}catch(e){{}}}}
async function init(){{try{{const data=await loadData();if(data.locked){{renderLock(data.name);return}}renderContent(data);}}catch(e){{document.getElementById('root').innerHTML='<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';}}}}
init();
</script>
</body></html>"""

import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio Prestige", page_icon="🏛️")

# --- 2. FONCTIONS ROBUSTES ---
def get_base64_image(image_filename):
    possible_paths = [os.path.join("assets", image_filename), image_filename]
    found_path = None
    for path in possible_paths:
        if os.path.exists(path):
            found_path = path
            break
    if not found_path: return None
    try:
        _, ext = os.path.splitext(found_path)
        ext = ext.replace('.', '').lower()
        if ext == 'jpg': ext = 'jpeg'
        with open(found_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/{ext};base64,{encoded}"
    except Exception:
        return None

# --- 3. CHARGEMENT DES ASSETS ---
IMG_INTRO1 = "marble.jpg"
IMG_INTRO2 = "marble.jpg"
IMG_FINAL  = "background2.jpg"
IMG_MARBLE = "marble.jpg"

b64_intro1 = get_base64_image(IMG_INTRO1)
b64_intro2 = get_base64_image(IMG_INTRO2)
b64_final  = get_base64_image(IMG_FINAL)
b64_marble = get_base64_image(IMG_MARBLE)

# CSS Backgrounds
css_bg1 = f"url('{b64_intro1}')" if b64_intro1 else "#000000"
css_bg2 = f"url('{b64_intro2}')" if b64_intro2 else "#111111"
css_bg3 = f"url('{b64_final}')"  if b64_final  else "#222222"
css_marble = f"url('{b64_marble}')" if b64_marble else "#cccccc"

projects = [
    {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
     {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Bot Trading",
        "image": "projet_bourse.jpg",
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    }
]

## --- 4. CSS GLOBAL STREAMLIT ---
st.markdown("""
    <style>
        #MainMenu, header, footer, [data-testid="stToolbar"] {visibility: hidden; display: none;}
        .block-container {padding: 0 !important; margin: 0 !important;}
        iframe {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            border: none; margin: 0; padding: 0; overflow: hidden; z-index: 99999; display: block;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 5. GÉNÉRATION HTML (CARTE REFERENCE) ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 

for i, project in enumerate(projects):
    # Contenu interne (Identique à votre référence)
    card_inner = f"""
        <div class="face front">
            <a href="{project['link']}" target="_blank" draggable="false">
                <div class="command-content">
                    <div class="icon"></div> 
                    <h3>{project['title']}</h3>
                    <div class="separator"></div>
                    <p>{project['desc']}</p>
                </div>
            </a>
        </div>
        <div class="face back">
        </div>
        <div class="face right"></div>
        <div class="face left"></div>
    """

    # Double Fantôme
    html_cards += f"""
    <div class="card-container" style="--angle: {i * angle}deg; --tz: {tz}px;">
        <div class="card main-card">
            {card_inner}
        </div>
        <div class="card reflection-card">
            {card_inner}
        </div>
    </div>
    """

# --- 6. VISUEL FINAL (FUSION EXACTE) ---
carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    /* Polices : On garde Great Vibes pour les cartes (comme votre ref) et Cinzel pour l'intro */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Helvetica+Neue:wght@300;700&display=swap');

    :root {{
        --w: 260px;
        --h: 360px;
        --d: 20px; 
    }}

    body {{ 
        margin: 0; padding: 0; width: 100vw; 
        height: 400vh; /* HAUTEUR POUR SCROLL */
        background-color: #000;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
        -webkit-user-select: none; user-select: none;
    }}

    /* --- LAYERS BACKGROUND --- */
    .bg-layer {{
        position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
        background-size: cover; background-position: center; background-repeat: no-repeat;
        transition: opacity 0.1s linear;
    }}
    #bg1 {{ background: {css_bg1}; z-index: 1; opacity: 1; }}
    #bg2 {{ background: {css_bg2}; z-index: 2; opacity: 0; }}
    #bg3 {{ background: {css_bg3}; z-index: 3; opacity: 0; }}

    /* --- TEXTES INTRO --- */
    .intro-text {{
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        text-align: center; width: 100%; z-index: 10; pointer-events: none;
    }}

    #intro1 {{ opacity: 1; }} /* FORCE VISIBLE AU DÉBUT */
    #intro2 {{ opacity: 0; }}

    /* TITRE PRINCIPAL (Effet Métal Doré) */
    .intro-text h1 {{
        font-family: 'Great Vibes', cursive; font-size: 3.5rem; margin: 0;
        color: #001A57; /* Couleur bleu nuit */
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.4), 0 0 20px rgba(0,0,0,0.8);
    }}
    
    /* SOUS-TITRE (Cursive Or Brillant) */
    .intro-text h2 {{
        font-family: 'Great Vibes', cursive; font-size: 3.5rem; margin: 0;
        color: #001A57;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.4), 0 0 20px rgba(0,0,0,0.8);
    }}

    /* --- CONTENEUR CARROUSEL --- */
    .scene-wrapper {{
        position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
        opacity: 0; z-index: 20; pointer-events: none; 
        transition: opacity 0.5s ease;
    }}
    .scene-wrapper.active {{ pointer-events: auto; cursor: grab; }}
    .scene-wrapper.active:active {{ cursor: grabbing; }}


    /* ================================================= */
    /* ===  VOTRE CSS DE REFERENCE EXACT (RESTAURÉ)  === */
    /* ================================================= */

    .scene {{ width: 100%; height: 100vh; perspective: 1200px; display: flex; justify-content: center; align-items: center; }}
    .carousel {{ width: var(--w); height: var(--h); position: relative; transform-style: preserve-3d; }}

    .card-container {{
        position: absolute; width: var(--w); height: var(--h); left: 0; top: 0;
        transform-style: preserve-3d;
        transform: rotateY(var(--angle)) translateZ(var(--tz));
    }}

    .card {{ width: 100%; height: 100%; position: absolute; transform-style: preserve-3d; }}

    /* Double Fantôme */
    .main-card {{ z-index: 2; }}
    .reflection-card {{
        transform: translateY(calc(100% + 10px)) scaleY(-1);
        opacity: 0.4; pointer-events: none;
        -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 60%);
        mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 60%);
        z-index: 1;
    }}

    .face {{ position: absolute; box-shadow: inset 0 0 20px rgba(0,0,0,0.3); }}

    /* FRONT (RESTAURÉ : OR & CURSIVE) */
    .front {{
        width: var(--w); height: var(--h);
        background: {css_marble}; background-size: cover; background-position: center;
        display: flex; justify-content: center; align-items: center;
        transform: translateZ(calc(var(--d) / 2)); 
        
    }}

    /* BACK */
    .back {{
        width: var(--w); height: var(--h);
        background: {css_marble}; background-size: cover; background-position: center;
        filter: brightness(0.6);
        display: flex; justify-content: center; align-items: center;
        transform: rotateY(180deg) translateZ(calc(var(--d) / 2));
    }}

    /* SIDES */
    .right {{
        width: var(--d); height: var(--h);
        background: {css_marble}; background-size: cover; background-position: center;
        filter: brightness(0.8); 
        left: calc((var(--w) - var(--d)) / 2);
        transform: translateX(calc(var(--w) / 2)) rotateY(90deg);
    }}
    .left {{
        width: var(--d); height: var(--h);
        background: {css_marble}; background-size: cover; background-position: center;
        filter: brightness(0.6); 
        left: calc((var(--w) - var(--d)) / 2);
        transform: translateX(calc(var(--w) / -2)) rotateY(-90deg);
    }}

    /* TYPO (RESTAURÉE : Great Vibes & Couleurs Chaudes) */
    .command-content {{ text-align: center; padding: 15px; width: 100%; cursor: inherit; }}
    
    .icon {{ 
        font-size: 1.5rem; margin-bottom: 5px; 
        color: #001A57; /* bleu nuit */
        text-shadow: 1px 1px 0px rgba(255,255,255,0.8);
    }}
    
    .command-content h3 {{ 
        margin: 0; 
        font-family: 'Great Vibes', cursive; /* RESTAURATION CURSIVE */
        font-size: 2.8rem; line-height: 1.1; 
        color: #001A57; /* bleu nuit */
        text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.8), 0px 0px 1px rgba(0,0,0,0.2); 
        font-weight: normal;
    }}
    
    .separator {{ 
        width: 50px; height: 1px; 
        background: #B8860B; /* OR */
        margin: 10px auto; opacity: 0.6; 
    }}
    
    .command-content p {{ 
        margin: 0; 
        font-family: 'Great Vibes', cursive; /* RESTAURATION CURSIVE */
        font-size: 1.6rem; 
        color: #010203; /* noir */
        text-shadow: 0px 1px 0px rgba(255,255,255,0.6); 
    }}
    
    .back-design {{ text-align: center; opacity: 0.6; }}
    .back-design .logo {{ font-size: 3rem; color: #333; }}
    .back-design .text {{ font-size: 0.6rem; letter-spacing: 3px; color: #333; font-weight: bold; }}
    
    a {{ text-decoration: none; color: inherit; display: block; height: 100%; display: flex; align-items: center; justify-content: center; -webkit-user-drag: none; }}
</style>
</head>
<body>

    <div id="bg1" class="bg-layer"></div>
    <div id="bg2" class="bg-layer"></div>
    <div id="bg3" class="bg-layer"></div>

    <div id="intro1" class="intro-text">
        <h1>Alexei Caminade</h1>
        <h1>Presents :</h1>
    </div>
    <div id="intro2" class="intro-text">
        <h2>My Project Portfolio</h2>
    </div>

    <div id="scene-wrapper" class="scene-wrapper">
        <div class="scene">
            <div class="carousel" id="carousel">
                {html_cards}
            </div>
        </div>
    </div>

<script>
    const carousel = document.getElementById('carousel');
    const sceneWrapper = document.getElementById('scene-wrapper');
    const bg1 = document.getElementById('bg1');
    const bg2 = document.getElementById('bg2');
    const bg3 = document.getElementById('bg3');
    const intro1 = document.getElementById('intro1');
    const intro2 = document.getElementById('intro2');

    let autoSpeed = -0.025; 
    let isDragging = false, startX = 0, currentRotation = 0, velocity = 0, lastX = 0;

    // --- LOGIQUE SCROLL ---
    window.addEventListener('scroll', () => {{
        const scrollY = window.scrollY;
        const h = window.innerHeight;

        // Intro 1
        let op1 = 1 - (scrollY / (h * 0.6));
        if (scrollY < h * 0.2) op1 = scrollY / (h * 0.2);
        else if (scrollY < h * 0.8) op1 = 1;
        else op1 = 1 - (scrollY - h * 0.8) / (h * 0.2);
        intro1.style.opacity = Math.max(0, op1);
        intro1.style.transform = `translate(-50%, -50%) scale(${{1 + scrollY * 0.0005}})`;

        // Intro 2
        let op2 = 0;
        if (scrollY > h * 0.8 && scrollY < h * 2.2) {{
            if (scrollY < h * 1.2) op2 = (scrollY - h * 0.8) / (h * 0.4);
            else if (scrollY < h * 1.8) op2 = 1;
            else op2 = 1 - (scrollY - h * 1.8) / (h * 0.4);
        }}
        intro2.style.opacity = Math.max(0, op2);
        intro2.style.transform = `translate(-50%, -50%) scale(${{0.8 + (scrollY - h) * 0.0005}})`;

        // Backgrounds Cross-fade
        let bg2Op = (scrollY > h * 0.5) ? (scrollY - h * 0.5) / (h * 0.7) : 0;
        bg2.style.opacity = Math.min(1, Math.max(0, bg2Op));

        let bg3Op = (scrollY > h * 1.8) ? (scrollY - h * 1.8) / (h * 0.7) : 0;
        bg3.style.opacity = Math.min(1, Math.max(0, bg3Op));

        // Carrousel Apparition
        let sceneOp = (scrollY > h * 2.0) ? (scrollY - h * 2.0) / (h * 0.5) : 0;
        sceneWrapper.style.opacity = Math.min(1, Math.max(0, sceneOp));

        if (sceneOp > 0.9) sceneWrapper.classList.add('active');
        else sceneWrapper.classList.remove('active');
    }});

    // --- INTERACTION ---
    window.addEventListener('mousedown', (e) => {{ 
        if (!sceneWrapper.classList.contains('active')) return;
        isDragging = true; startX = e.clientX; lastX = e.clientX; velocity = 0; 
        document.body.style.cursor = "grabbing"; 
    }});
    window.addEventListener('mousemove', (e) => {{ 
        if (!isDragging) return; 
        const x = e.clientX; velocity = (x - lastX) * 0.3; currentRotation += velocity; 
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; 
    }});
    window.addEventListener('mouseup', () => {{ isDragging = false; if (sceneWrapper.classList.contains('active')) document.body.style.cursor = "grab"; }});
    window.addEventListener('touchstart', (e) => {{ if (!sceneWrapper.classList.contains('active')) return; isDragging = true; startX = e.touches[0].clientX; lastX = e.touches[0].clientX; velocity = 0; }});
    window.addEventListener('touchmove', (e) => {{ if (!isDragging) return; const x = e.touches[0].clientX; velocity = (x - lastX) * 0.5; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; }});
    window.addEventListener('touchend', () => {{ isDragging = false; }});

    function animate() {{
        requestAnimationFrame(animate);
        if (!isDragging) {{
            velocity *= 0.95;
            currentRotation += velocity + autoSpeed;
            carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        }}
    }}
    animate();
    window.dispatchEvent(new Event('scroll'));
</script>
</body>
</html>
"""

components.html(carousel_html, height=2000, scrolling=True)
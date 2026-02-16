import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio Prestige", page_icon="🏛️")

# Texture Marbre Blanc (Image libre de droits)
MARBLE_TEXTURE = "https://unsplash.com/fr/photos/gros-plan-dune-surface-de-marbre-blanc-li0iC0rjvvg"

# --- 2. FONCTIONS (Déplacée en haut pour être utilisée partout) ---
def get_base64_image(image_filename):
    """Charge une image locale et la convertit en chaîne Base64"""
    image_path = os.path.join("assets", image_filename)
    if not os.path.exists(image_path):
        return "" 
    
    # On détecte l'extension pour le bon format MIME (png ou jpg)
    _, ext = os.path.splitext(image_filename)
    ext = ext.replace('.', '')
    # Si c'est du jpg, on normalise en jpeg
    if ext == 'jpg': ext = 'jpeg'
    
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/{ext};base64,{encoded}"

# --- 3. PARAMÈTRES ET DONNÉES ---

# ⚠️ MODIFIEZ ICI LE NOM DE VOTRE IMAGE DE FOND ⚠️
# Assurez-vous que ce fichier existe dans le dossier 'assets'
BACKGROUND_IMAGE_NAME = "background2.jpg" 

# On charge l'image de fond tout de suite
background_b64 = get_base64_image(BACKGROUND_IMAGE_NAME)

projects = [
    {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
     {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    },
    {
        "title": "Trading Bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Trading Automatique et Signaux"
    }
]

# --- 4. CSS GLOBAL (Plein écran forcé) ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden;}
        .stApp > header {display: none;}
        
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 99999;
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 4. GÉNÉRATION HTML 3D ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 

for i, project in enumerate(projects):
    img_src = get_base64_image(project["image"])
    
    html_cards += f"""
    <div class="card-container" style="--angle: {i * angle}deg; --tz: {tz}px;">
        <div class="card">
            <div class="face front">
                <a href="{project['link']}" target="_blank" draggable="false">
                    <div class="card-content">
                        <img src="{img_src}" alt="{project['title']}">
                        <div class="info">
                            <h3>{project['title']}</h3>
                            <p>{project['desc']}</p>
                        </div>
                    </div>
                </a>
            </div>
            
            <div class="face right"></div>
            <div class="face left"></div>
            
            <div class="face back">
                <div class="back-design">
                    <div class="logo">🏛️</div>
                    <div class="text">CONFIDENTIAL</div>
                </div>
            </div>
        </div>
    </div>
    """

# On vérifie si l'image de fond a été trouvée, sinon on met un fallback sombre
bg_css_rule = f"background: url('{background_b64}') no-repeat center center fixed;" if background_b64 else "background: #1a1a1a;"

carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ 
        margin: 0; padding: 0;
        width: 100vw; height: 100vh;
        overflow: hidden; 
        {bg_css_rule}
        background-size: cover;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    }}
    
    /* Filtre sombre sur le fond (réglé à 0.3 pour laisser passer la lumière) */
    body::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.3);
        z-index: -1;
    }}

    .scene {{
        width: 100%; height: 100vh;
        perspective: 1200px;
        display: flex; justify-content: center; align-items: center;
        cursor: grab; user-select: none;
    }}
    .scene:active {{ cursor: grabbing; }}

    .carousel {{
        width: 260px; height: 360px;
        position: relative;
        transform-style: preserve-3d;
    }}

    .card-container {{
        position: absolute;
        width: 260px; height: 360px;
        left: 0; top: 0;
        transform-style: preserve-3d;
        transform: rotateY(var(--angle)) translateZ(var(--tz));
        
        /* Reflet sous la carte */
        -webkit-box-reflect: below 10px linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.3));
        
        animation: float 6s ease-in-out infinite;
    }}
    
    .card-container:nth-child(1) {{ animation-delay: 0s; }}
    .card-container:nth-child(2) {{ animation-delay: 1s; }}
    .card-container:nth-child(3) {{ animation-delay: 2s; }}
    .card-container:nth-child(4) {{ animation-delay: 3s; }}
    .card-container:nth-child(5) {{ animation-delay: 4s; }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        50% {{ transform: translateY(-15px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        100% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
    }}

    .card {{
        width: 100%; height: 100%;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.3s;
    }}

    /* --- GESTION DES FACES ET DE L'ÉPAISSEUR --- */
    .face {{
        position: absolute;
        border-radius: 4px; /* Un peu moins arrondi pour faire "Bloc de pierre" */
        backface-visibility: visible; /* Important pour voir les côtés */
    }}

    /* Face AVANT */
    .front {{
        width: 260px; height: 360px;
        background: rgba(20, 20, 30, 0.9);
        border: 1px solid rgba(255, 215, 0, 0.3);
        transform: translateZ(15px); /* On avance de la moitié de l'épaisseur */
        box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
    }}

    /* Face ARRIÈRE (Le Marbre Blanc) */
    .back {{
        width: 260px; height: 360px;
        transform: rotateY(180deg) translateZ(15px); /* On recule de la moitié */
        background: url('{MARBLE_TEXTURE}');
        background-size: cover;
        border: 1px solid #ccc;
        display: flex; justify-content: center; align-items: center;
        box-shadow: inset 0 0 30px rgba(0,0,0,0.1); /* Ombre interne pour le réalisme */
    }}

    /* Côté DROIT */
    .right {{
        width: 30px; height: 360px; /* Largeur = épaisseur de la carte */
        right: 0; /* Collé à droite */
        transform-origin: right;
        transform: rotateY(90deg) translateZ(0px); /* Le pivot fait tout le travail */
        background: url('{MARBLE_TEXTURE}');
        background-size: cover;
        filter: brightness(0.9); /* Un peu plus sombre pour simuler l'ombre */
    }}

    /* Côté GAUCHE */
    .left {{
        width: 30px; height: 360px;
        left: 0;
        transform-origin: left;
        transform: rotateY(-90deg) translateZ(0px);
        background: url('{MARBLE_TEXTURE}');
        background-size: cover;
        filter: brightness(0.9);
    }}
    
    /* --- CONTENU --- */

    .front:hover {{
        border-color: #ffd700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
    }}

    .card-content img {{
        width: 100%; height: 220px; object-fit: cover;
        border-bottom: 1px solid rgba(255,215,0,0.2);
        pointer-events: none;
        border-radius: 4px 4px 0 0;
    }}

    .info {{
        padding: 20px; color: white; text-align: center; pointer-events: none;
    }}
    .info h3 {{ margin: 0 0 8px 0; font-size: 1.3rem; color: #fff; text-transform: uppercase; letter-spacing: 1px; }}
    .info p {{ margin: 0; font-size: 0.9rem; color: #bbb; font-style: italic; }}

    /* Design du dos (Marbre) */
    .back-design {{ text-align: center; opacity: 0.7; }}
    .back-design .logo {{ font-size: 4rem; margin-bottom: 10px; color: #333; }} /* Logo gris foncé */
    .back-design .text {{ 
        font-size: 0.8rem; letter-spacing: 3px; 
        color: #111; /* Texte noir */
        font-weight: bold; 
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }}

    a {{ text-decoration: none; color: inherit; display: block; height: 100%; }}

</style>
</head>
<body>

<div class="scene">
    <div class="carousel" id="carousel">
        {html_cards}
    </div>
</div>

<script>
    const carousel = document.getElementById('carousel');
    const scene = document.querySelector('.scene');
    
    let isDragging = false;
    let startX = 0;
    let currentRotation = 0;
    let previousRotation = 0;
    let velocity = 0;
    let lastX = 0;
    let animationId = null;

    scene.addEventListener('mousedown', (e) => {{
        isDragging = true; startX = e.clientX; lastX = e.clientX;
        velocity = 0; if (animationId) cancelAnimationFrame(animationId);
    }});
    window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        const x = e.clientX; const delta = x - lastX;
        velocity = delta * 0.3; currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        lastX = x;
    }});
    window.addEventListener('mouseup', () => {{
        if (isDragging) {{ isDragging = false; inertiaLoop(); }}
    }});
    
    function inertiaLoop() {{
        if (Math.abs(velocity) < 0.05) return;
        velocity *= 0.95; currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        animationId = requestAnimationFrame(inertiaLoop);
    }}
    
    scene.addEventListener('touchstart', (e) => {{
        isDragging = true; startX = e.touches[0].clientX; lastX = e.touches[0].clientX;
        if (animationId) cancelAnimationFrame(animationId);
    }});
    window.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        const x = e.touches[0].clientX; const delta = x - lastX;
        velocity = delta * 0.5; currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        lastX = x;
    }});
    window.addEventListener('touchend', () => {{
        isDragging = false; inertiaLoop();
    }});
</script>
</body>
</html>
"""

components.html(carousel_html, height=1000, scrolling=False)
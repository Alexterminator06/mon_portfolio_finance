import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio Prestige", page_icon="🏛️")

# --- 2. FONCTIONS ROBUSTES ---
def get_base64_image(image_filename):
    """Charge une image locale et la convertit en chaîne Base64."""
    # On cherche dans le dossier courant ET dans assets pour être sûr
    possible_paths = [
        os.path.join("assets", image_filename),
        image_filename
    ]
    
    found_path = None
    for path in possible_paths:
        if os.path.exists(path):
            found_path = path
            break
            
    if not found_path:
        # On ne renvoie pas d'erreur bloquante pour ne pas casser le layout, 
        # mais on retourne None pour gérer le fallback en CSS
        return None
    
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

# ⚠️ VÉRIFIEZ BIEN CES NOMS ⚠️
BACKGROUND_IMAGE_NAME = "background2.jpg"
MARBLE_IMAGE_NAME = "marble.jpg" 

background_b64 = get_base64_image(BACKGROUND_IMAGE_NAME)
marble_b64 = get_base64_image(MARBLE_IMAGE_NAME)

# Logique de secours (Fallback) pour le CSS
# Si l'image est trouvée, on met l'URL. Sinon, on met une couleur (Gris Pierre #cccccc)
bg_css = f"url('{background_b64}')" if background_b64 else "#111111"
marble_css = f"url('{marble_b64}')" if marble_b64 else "#cccccc" # Gris clair si pas de marbre

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

## --- 4. CSS GLOBAL ---
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

# --- 4. GÉNÉRATION HTML ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 

for i, project in enumerate(projects):
    img_data = get_base64_image(project["image"])
    img_tag = f"<img src='{img_data}' alt='{project['title']}'>" if img_data else "<div style='height:220px; background:#222;'></div>"

    html_cards += f"""
    <div class="card-container" style="--angle: {i * angle}deg; --tz: {tz}px;">
        <div class="card">
            <div class="face front">
                <a href="{project['link']}" target="_blank" draggable="false">
                    <div class="card-content">
                        {img_tag}
                        <div class="info">
                            <h3>{project['title']}</h3>
                            <p>{project['desc']}</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="face back">
                <div class="back-design">
                    <div class="logo">🏛️</div>
                    <div class="text">CONFIDENTIAL</div>
                </div>
            </div>
        </div>
    </div>
    """

carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ 
        margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden; 
        background: {bg_css} no-repeat center center fixed; background-size: cover;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    }}
    body::before {{
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0); z-index: -1;
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
        position: relative; transform-style: preserve-3d;
    }}

    .card-container {{
        position: absolute; width: 260px; height: 360px; left: 0; top: 0;
        transform-style: preserve-3d;
        transform: rotateY(var(--angle)) translateZ(var(--tz));
        -webkit-box-reflect: below 10px linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.3));
        animation: float 6s ease-in-out infinite;
    }}
    
    .card-container:nth-child(1) {{ animation-delay: 0s; }}
    .card-container:nth-child(2) {{ animation-delay: 1s; }}
    .card-container:nth-child(3) {{ animation-delay: 2s; }}
    .card-container:nth-child(4) {{ animation-delay: 3s; }}
    .card-container:nth-child(5) {{ animation-delay: 4s; }}

    @keyframes float {{
        0%, 100% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        50% {{ transform: translateY(-15px) rotateY(var(--angle)) translateZ(var(--tz)); }}
    }}

    .card {{
        width: 100%; height: 100%;
        position: relative; 
        transform-style: preserve-3d;
        transition: transform 0.3s;
    }}

    .face {{
        position: absolute; width: 100%; height: 100%;
        backface-visibility: hidden; /* Cache le dos quand on regarde devant */
        border-radius: 8px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.8);
    }}

    /* --- FACE AVANT --- */
    .front {{
        background: rgba(20, 20, 30, 0.95);
        border: 1px solid rgba(255, 215, 0, 0.3);
        /* Pas de rotation, c'est la face par défaut */
    }}
    .front:hover {{ border-color: #ffd700; box-shadow: 0 0 25px rgba(255, 215, 0, 0.5); }}

    /* --- FACE ARRIÈRE (MARBRE) --- */
    .back {{
        transform: rotateY(180deg); /* On la retourne pour qu'elle soit au dos */
        background: {marble_css};
        background-size: cover;
        border: 1px solid #888;
        display: flex; justify-content: center; align-items: center;
    }}

    /* Contenu */
    .card-content img {{ width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(255,215,0,0.2); }}
    .info {{ padding: 20px; color: white; text-align: center; }}
    .info h3 {{ margin: 0 0 5px 0; font-size: 1.2rem; color: #fff; text-transform: uppercase; }}
    .info p {{ margin: 0; font-size: 0.85rem; color: #aaa; }}

    .back-design {{ text-align: center; opacity: 0.8; }}
    .back-design .logo {{ font-size: 4rem; margin-bottom: 10px; color: #333; }}
    .back-design .text {{ font-size: 0.8rem; letter-spacing: 3px; color: #111; font-weight: bold; text-shadow: 1px 1px 0px rgba(255,255,255,0.4); }}

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
    let isDragging = false, startX = 0, currentRotation = 0, velocity = 0, lastX = 0, animationId = null;

    scene.addEventListener('mousedown', (e) => {{ isDragging = true; startX = e.clientX; lastX = e.clientX; velocity = 0; if (animationId) cancelAnimationFrame(animationId); }});
    window.addEventListener('mousemove', (e) => {{ if (!isDragging) return; const x = e.clientX; velocity = (x - lastX) * 0.3; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; }});
    window.addEventListener('mouseup', () => {{ if (isDragging) {{ isDragging = false; inertiaLoop(); }} }});
    
    function inertiaLoop() {{ if (Math.abs(velocity) < 0.05) return; velocity *= 0.95; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; animationId = requestAnimationFrame(inertiaLoop); }}
    
    scene.addEventListener('touchstart', (e) => {{ isDragging = true; startX = e.touches[0].clientX; lastX = e.touches[0].clientX; if (animationId) cancelAnimationFrame(animationId); }});
    window.addEventListener('touchmove', (e) => {{ if (!isDragging) return; const x = e.touches[0].clientX; velocity = (x - lastX) * 0.5; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; }});
    window.addEventListener('touchend', () => {{ isDragging = false; inertiaLoop(); }});
</script>
</body>
</html>
"""

components.html(carousel_html, height=1000, scrolling=False)
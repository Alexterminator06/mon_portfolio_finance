import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio Prestige", page_icon="🏛️")

# --- 2. CSS "FORCE BRUTE" POUR LE CLOUD ---
st.markdown("""
    <style>
        /* 1. On cache tous les éléments d'interface de Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden;} /* Cache le menu développeur en haut */
        .stApp > header {display: none;}
        
        /* 2. On supprime le padding du conteneur principal */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        
        /* 3. L'ARME SECRÈTE : On force l'iframe du composant à passer en PLEIN ÉCRAN par-dessus tout */
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
            z-index: 99999; /* Passe au-dessus de tout, y compris la barre du bas Streamlit Cloud */
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)

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
    
BACKGROUND_IMAGE_NAME = "background.jpg"
    
# (Assurez-vous que vos images sont bien dans le dossier 'assets')
projects = [
    {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    },
    {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    },
    {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    },
    {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    },
     {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    },
    {
        "title": "Trading bot",
        "image": "projet_bourse.jpg", 
        "link": "https://bitcoin-trading-bot.streamlit.app/",
        "desc": "Visualisation de marché & KPIs"
    }
]

def get_base64_image(image_filename):
    image_path = os.path.join("assets", image_filename)
    if not os.path.exists(image_path):
        return "" 
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 4. HTML GENERATION ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 

for i, project in enumerate(projects):
    img_b64 = get_base64_image(project["image"])
    
    html_cards += f"""
    <div class="card-container" style="--angle: {i * angle}deg; --tz: {tz}px;">
        <div class="card">
            <div class="face front">
                <a href="{project['link']}" target="_blank" draggable="false">
                    <div class="card-content">
                        <img src="data:image/jpeg;base64,{img_b64}" alt="{project['title']}">
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
                    <div class="text">ASSET MANAGED</div>
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
    /* CSS INTERNE DU COMPOSANT */
    body {{ 
        margin: 0; 
        padding: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden; 
        background: BACKGROUND_URL; 
        background-size: cover;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    }}
    
    body::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.6);
        z-index: -1;
    }}

    .scene {{
        width: 100%;
        height: 100vh;
        perspective: 1200px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: grab;
        user-select: none;
    }}
    
    .scene:active {{ cursor: grabbing; }}

    .carousel {{
        width: 260px; 
        height: 360px;
        position: relative;
        transform-style: preserve-3d;
    }}

    .card-container {{
        position: absolute;
        width: 260px;
        height: 360px;
        left: 0;
        top: 0;
        transform-style: preserve-3d;
        transform: rotateY(var(--angle)) translateZ(var(--tz));
        -webkit-box-reflect: below 20px linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.4));
        animation: float 6s ease-in-out infinite;
    }}
    
    .card-container:nth-child(1) {{ animation-delay: 0s; }}
    .card-container:nth-child(2) {{ animation-delay: 1s; }}
    .card-container:nth-child(3) {{ animation-delay: 2s; }}
    .card-container:nth-child(4) {{ animation-delay: 3s; }}
    .card-container:nth-child(5) {{ animation-delay: 4s; }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        50% {{ transform: translateY(-20px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        100% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
    }}

    .card {{
        width: 100%;
        height: 100%;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.3s;
    }}

    .face {{
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8); 
    }}

    .front {{
        background: rgba(20, 20, 30, 0.85);
        border: 1px solid rgba(255, 215, 0, 0.3);
        backdrop-filter: blur(8px);
    }}
    
    .front:hover {{
        border-color: #ffd700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
    }}

    .card-content img {{
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-bottom: 1px solid rgba(255,215,0,0.2);
        pointer-events: none;
    }}

    .info {{
        padding: 20px;
        color: white;
        text-align: center;
        pointer-events: none;
    }}
    
    .info h3 {{ margin: 0 0 8px 0; font-size: 1.3rem; color: #fff; text-transform: uppercase; letter-spacing: 1px; }}
    .info p {{ margin: 0; font-size: 0.9rem; color: #bbb; font-style: italic; }}

    .back {{
        transform: rotateY(180deg);
        background: linear-gradient(135deg, #000 0%, #1a1a1a 100%);
        border: 1px solid #444;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .back-design {{ text-align: center; opacity: 0.5; }}
    .back-design .logo {{ font-size: 5rem; margin-bottom: 10px; }}
    .back-design .text {{ font-size: 0.8rem; letter-spacing: 3px; color: #ffd700; font-weight: bold; }}

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
        isDragging = true;
        startX = e.clientX;
        lastX = e.clientX;
        velocity = 0;
        if (animationId) cancelAnimationFrame(animationId);
    }});

    window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        const x = e.clientX;
        const delta = x - lastX;
        velocity = delta * 0.3;
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        lastX = x;
    }});

    window.addEventListener('mouseup', () => {{
        if (isDragging) {{
            isDragging = false;
            inertiaLoop();
        }}
    }});
    
    function inertiaLoop() {{
        if (Math.abs(velocity) < 0.05) return;
        velocity *= 0.95;
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        animationId = requestAnimationFrame(inertiaLoop);
    }}
    
    scene.addEventListener('touchstart', (e) => {{
        isDragging = true;
        startX = e.touches[0].clientX;
        lastX = e.touches[0].clientX;
        if (animationId) cancelAnimationFrame(animationId);
    }});
    window.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        const x = e.touches[0].clientX;
        const delta = x - lastX;
        velocity = delta * 0.5;
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        lastX = x;
    }});
    window.addEventListener('touchend', () => {{
        isDragging = false;
        inertiaLoop();
    }});

</script>
</body>
</html>
"""

# --- 5. RENDU FINAL ---
# Le paramètre height ici n'importe plus vraiment car le CSS force 100vh, 
# mais on le laisse pour éviter les erreurs.
components.html(carousel_html, height=1000, scrolling=False)
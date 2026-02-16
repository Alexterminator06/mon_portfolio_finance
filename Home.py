import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuration de la page
st.set_page_config(layout="wide", page_title="Portfolio Finance 3D", page_icon="🏦")

# --- 1. CONFIGURATION DES PROJETS ---
BACKGROUND_URL = "https://unsplash.com/fr/photos/batiment-en-beton-gris-pendant-la-journee-WgUHuGSWPVM"
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

# --- 2. FONCTIONS ---
def get_base64_image(image_filename):
    """Charge une image locale pour les cartes"""
    image_path = os.path.join("assets", image_filename)
    if not os.path.exists(image_path):
        return "" 
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 3. GÉNÉRATION DU CARROUSEL ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 # J'ai augmenté un peu l'écartement pour l'effet "Hall"

for i, project in enumerate(projects):
    img_b64 = get_base64_image(project["image"])
    
    html_cards += f"""
    <div class="card-container" style="transform: rotateY({i * angle}deg) translateZ({tz}px);">
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
    /* FOND D'ÉCRAN IMMERSIF */
    body {{ 
        margin: 0; 
        overflow: hidden; 
        background: url('{BACKGROUND_URL}') no-repeat center center fixed; 
        background-size: cover;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    }}
    
    /* On assombrit l'image de fond pour que les cartes ressortent bien */
    body::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.6); /* Filtre sombre */
        z-index: -1;
    }}

    .scene {{
        width: 100%;
        height: 700px; /* Plus haut pour bien voir le sol */
        perspective: 1200px; /* Perspective augmentée pour la profondeur du hall */
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
        margin-top: -50px; /* On remonte un peu le carrousel par rapport au sol */
    }}

    .card-container {{
        position: absolute;
        width: 260px;
        height: 360px;
        left: 0;
        top: 0;
        transform-style: preserve-3d;
        
        /* C'EST ICI QUE SE JOUE L'EFFET MIROIR / SOL EN MARBRE */
        /* Note: Fonctionne sur Chrome/Safari/Edge. Firefox a un support limité. */
        -webkit-box-reflect: below 20px linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.4));
        
        /* Animation de lévitation */
        animation: float 6s ease-in-out infinite;
    }}
    
    /* Décalage de l'animation pour chaque carte pour qu'elles ne bougent pas toutes en même temps */
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
        /* Ombre portée plus forte pour le réalisme 3D */
        box-shadow: 0 10px 30px rgba(0,0,0,0.8); 
    }}

    .front {{
        background: rgba(20, 20, 30, 0.85); /* Fond sombre semi-transparent */
        border: 1px solid rgba(255, 215, 0, 0.3); /* Bordure dorée subtile */
        backdrop-filter: blur(8px);
    }}
    
    .front:hover {{
        border-color: #ffd700; /* Or vif au survol */
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

    // --- GESTION DU MOUVEMENT (Identique à avant) ---
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
        velocity *= 0.95; // Friction
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        animationId = requestAnimationFrame(inertiaLoop);
    }}
    
    // Support Mobile
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

# --- AFFICHAGE ---
# On utilise components.html avec une hauteur suffisante pour l'effet miroir
st.title("🏛️ Mon Portfolio")
st.markdown("**Analysez. Cliquez. Investissez.**")
components.html(carousel_html, height=750)
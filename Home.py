import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuration de la page
st.set_page_config(layout="wide", page_title="Portfolio Finance 3D", page_icon="🏦")

# --- 1. CONFIGURATION DES PROJETS ---
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

# --- 2. FONCTION IMAGE ---
def get_base64_image(image_filename):
    image_path = os.path.join("assets", image_filename)
    if not os.path.exists(image_path):
        return "" 
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 3. GÉNÉRATION HTML/CSS/JS ---
html_cards = ""
angle = 360 / len(projects)
tz = 400 

for i, project in enumerate(projects):
    img_b64 = get_base64_image(project["image"])
    
    # Structure 3D complexe : Un conteneur qui contient le devant (front) et le derrière (back)
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
                    <div class="logo">🏦</div>
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
    /* FOND D'ÉCRAN : Dégradé radial sombre et classe */
    body {{ 
        margin: 0; 
        overflow: hidden; 
        background: radial-gradient(circle at center, #2b303b 0%, #0e1117 100%);
        font-family: 'Segoe UI', sans-serif; 
    }}
    
    .scene {{
        width: 100%;
        height: 600px;
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: grab;
        user-select: none;
    }}
    
    .scene:active {{ cursor: grabbing; }}

    .carousel {{
        width: 250px; 
        height: 350px;
        position: relative;
        transform-style: preserve-3d;
        /* Pas de transition ici car le JS gère l'animation fluide */
    }}

    .card-container {{
        position: absolute;
        width: 240px;
        height: 340px;
        left: 5px;
        top: 5px;
        transform-style: preserve-3d; /* Permet aux faces d'être en 3D */
    }}

    .card {{
        width: 100%;
        height: 100%;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.3s;
    }}

    /* DESIGN COMMUN DES FACES */
    .face {{
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden; /* Cache l'arrière quand on est devant */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        overflow: hidden;
    }}

    /* --- FACE AVANT --- */
    .front {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
    }}
    
    .front:hover {{
        border-color: #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
    }}

    .card-content img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        pointer-events: none;
    }}

    .info {{
        padding: 15px;
        color: white;
        text-align: center;
        pointer-events: none;
    }}
    
    .info h3 {{ margin: 0 0 5px 0; font-size: 1.1rem; color: #fff; }}
    .info p {{ margin: 0; font-size: 0.85rem; color: #a0a0a0; }}

    /* --- FACE ARRIÈRE (Design Sobre) --- */
    .back {{
        transform: rotateY(180deg); /* La retourne par défaut */
        background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
        border: 1px solid #333;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .back-design {{
        text-align: center;
        opacity: 0.3; /* Discret */
    }}

    .back-design .logo {{ font-size: 4rem; margin-bottom: 10px; }}
    .back-design .text {{ 
        font-size: 0.8rem; 
        letter-spacing: 2px; 
        color: #d4af37; /* Or métallique */
        font-weight: bold;
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
    
    // Variables physiques
    let isDragging = false;
    let startX = 0;
    let currentRotation = 0;
    let previousRotation = 0;
    
    let velocity = 0;       // Vitesse actuelle
    let lastX = 0;          // Position précédente pour calculer la vitesse
    let isInertia = false;  // Est-ce qu'on est en phase d'inertie ?
    let animationId = null;

    // 1. DÉBUT DU DRAG
    scene.addEventListener('mousedown', (e) => {{
        isDragging = true;
        isInertia = false;
        startX = e.clientX;
        lastX = e.clientX;
        velocity = 0;
        
        // Annule l'animation en cours s'il y en a une
        if (animationId) cancelAnimationFrame(animationId);
    }});

    // 2. MOUVEMENT
    window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        
        const x = e.clientX;
        const delta = x - lastX;
        
        // Calcul de la vitesse instantanée
        velocity = delta * 0.3; // 0.3 = sensibilité
        
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        
        lastX = x;
    }});

    // 3. FIN DU DRAG (LANCEMENT INERTIE)
    window.addEventListener('mouseup', () => {{
        if (isDragging) {{
            isDragging = false;
            inertiaLoop(); // On lance la boucle d'inertie
        }}
    }});
    
    // --- BOUCLE D'ANIMATION (INERTIE) ---
    function inertiaLoop() {{
        // Si la vitesse est très faible, on arrête tout pour économiser le CPU
        if (Math.abs(velocity) < 0.05) {{
            return;
        }}

        // Friction : on réduit la vitesse à chaque image (0.95 = 5% de perte)
        velocity *= 0.95;
        
        currentRotation += velocity;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;

        // On demande la prochaine frame
        animationId = requestAnimationFrame(inertiaLoop);
    }}
    
    // --- SUPPORT MOBILE (Touch) ---
    scene.addEventListener('touchstart', (e) => {{
        isDragging = true;
        isInertia = false;
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

st.title("🏦 Mon Hub Finance")
st.markdown("Faites tourner le carrousel. Observez l'inertie et le design au dos des cartes.")
components.html(carousel_html, height=650)
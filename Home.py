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

# --- 2. FONCTION UTILITAIRE : CHARGEMENT IMAGES ---
def get_base64_image(image_filename):
    """Transforme une image locale en code pour le HTML"""
    # On gère le cas où l'image n'existe pas pour éviter les erreurs
    image_path = os.path.join("assets", image_filename)
    if not os.path.exists(image_path):
        return "" # Retourne vide si pas d'image
        
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 3. GÉNÉRATION DU CODE HTML/CSS/JS ---
html_cards = ""
angle = 360 / len(projects)
tz = 400 # Rayon du carrousel (Eloignement du centre)

for i, project in enumerate(projects):
    img_b64 = get_base64_image(project["image"])
    
    # Création de chaque carte HTML
    html_cards += f"""
    <div class="card" style="transform: rotateY({i * angle}deg) translateZ({tz}px);">
        <a href="{project['link']}" target="_blank" draggable="false"> <div class="card-content">
                <img src="data:image/jpeg;base64,{img_b64}" alt="{project['title']}">
                <div class="info">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                </div>
            </div>
        </a>
    </div>
    """

# Le bloc complet HTML/CSS/JS
carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ margin: 0; overflow: hidden; background-color: #0e1117; font-family: sans-serif; }}
    
    .scene {{
        width: 100%;
        height: 600px;
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        cursor: grab; /* Curseur main ouverte par défaut */
        user-select: none; /* Empêche de sélectionner le texte pendant qu'on glisse */
    }}

    .scene:active {{
        cursor: grabbing; /* Curseur main fermée quand on clique */
    }}

    .carousel {{
        width: 250px; 
        height: 350px;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.1s; /* Transition très courte pour réactivité immédiate au drag */
    }}

    .card {{
        position: absolute;
        width: 240px;
        height: 340px;
        left: 5px;
        top: 5px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        transition: border 0.3s, box-shadow 0.3s; /* On garde l'effet hover */
        /* Pas de transition sur transform ici pour éviter les conflits avec le carrousel global */
    }}

    .card:hover {{
        border: 2px solid #00f2ff;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.6);
        z-index: 10; /* Met la carte survolée au premier plan */
    }}

    .card-content img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        pointer-events: none; /* Important: empêche l'image de bloquer le drag */
    }}

    .info {{
        padding: 15px;
        color: white;
        text-align: center;
        pointer-events: none; /* Le texte ne bloque pas le drag */
    }}
    
    .info h3 {{ margin: 0 0 5px 0; font-size: 1.2rem; }}
    .info p {{ margin: 0; font-size: 0.9rem; color: #ccc; }}

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

    // 1. Quand on appuie sur la souris
    scene.addEventListener('mousedown', (e) => {{
        isDragging = true;
        startX = e.clientX;
        // On désactive la transition longue pour que le mouvement colle à la souris
        carousel.style.transition = 'none'; 
    }});

    // 2. Quand on bouge la souris
    window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        
        const x = e.clientX;
        // Calcul de la distance parcourue
        const walk = (x - startX) * 0.5; // 0.5 est la sensibilité (vitesse)
        
        currentRotation = previousRotation + walk;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
    }});

    // 3. Quand on relâche la souris
    window.addEventListener('mouseup', () => {{
        if (isDragging) {{
            isDragging = false;
            previousRotation = currentRotation;
            // On remet une petite transition pour l'inertie ou les clics futurs
            carousel.style.transition = 'transform 0.5s ease-out';
        }}
    }});
    
    // Support tactile (Mobile)
    scene.addEventListener('touchstart', (e) => {{
        isDragging = true;
        startX = e.touches[0].clientX;
        carousel.style.transition = 'none';
    }});

    window.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        const x = e.touches[0].clientX;
        const walk = (x - startX) * 0.8; 
        currentRotation = previousRotation + walk;
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
    }});

    window.addEventListener('touchend', () => {{
        isDragging = false;
        previousRotation = currentRotation;
        carousel.style.transition = 'transform 0.5s ease-out';
    }});

</script>
</body>
</html>
"""

# --- AFFICHAGE DANS STREAMLIT ---
st.title("🏦 Mes Projets Finance")
st.markdown("👈 **Cliquez et glissez** horizontalement pour faire tourner le carrousel.")

# Injection du HTML
components.html(carousel_html, height=650)
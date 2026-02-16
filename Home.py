import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="Mon Portfolio 3D", page_icon="🏦")

# --- CONFIGURATION DES PROJETS ---
# Ajoutez vos projets ici. 
# image: le nom du fichier dans le dossier 'assets'
# link: le lien vers l'app streamlit déployée
projects = [
    {
        "title": "Analyse Bourse",
        "image": "bourse.jpg", 
        "link": "https://mon-projet-bourse.streamlit.app",
        "desc": "Visualisation de marché & KPIs"
    },
    {
        "title": "Bot Trading",
        "image": "crypto.jpg",
        "link": "https://mon-bot-bitcoin.streamlit.app",
        "desc": "Stratégie Golden Cross BTC"
    },
    {
        "title": "Pricing Options",
        "image": "option.jpg",
        "link": "https://mon-pricing.streamlit.app",
        "desc": "Modèle Black-Scholes"
    },
    # Vous pouvez dupliquer des projets pour tester l'effet carrousel si vous n'en avez que 3
    {
        "title": "Optimisation Markowitz",
        "image": "bourse.jpg", # Image temporaire
        "link": "#",
        "desc": "Allocation d'actifs"
    },
     {
        "title": "Analyse Sentiment",
        "image": "crypto.jpg", # Image temporaire
        "link": "#",
        "desc": "NLP sur news financières"
    }
]

# --- FONCTION UTILITAIRE : CHARGEMENT IMAGES ---
def get_base64_image(image_filename):
    """Transforme une image locale en code pour le HTML"""
    image_path = os.path.join("assets", image_filename)
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        # Retourne une image vide grise si fichier pas trouvé
        return "" 

# --- GÉNÉRATION DU CODE HTML/CSS/JS ---
html_cards = ""
angle = 360 / len(projects)
tz = 400 # Distance du centre (Profondeur) - Augmentez si les cartes se chevauchent

for i, project in enumerate(projects):
    img_b64 = get_base64_image(project["image"])
    
    # Création de chaque carte (HTML)
    html_cards += f"""
    <div class="card" style="transform: rotateY({i * angle}deg) translateZ({tz}px);">
        <a href="{project['link']}" target="_blank">
            <div class="card-content">
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
    }}

    .carousel {{
        width: 250px; 
        height: 350px;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.5s; /* Fluidité du mouvement */
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
        transition: all 0.3s;
        cursor: pointer;
        overflow: hidden;
    }}

    .card:hover {{
        border: 2px solid #00f2ff;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.6);
    }}

    .card-content img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .info {{
        padding: 15px;
        color: white;
        text-align: center;
    }}
    
    .info h3 {{ margin: 0 0 5px 0; font-size: 1.2rem; }}
    .info p {{ margin: 0; font-size: 0.9rem; color: #ccc; }}

    a {{ text-decoration: none; }}

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
    
    // Variables pour la gestion de la souris
    let currentAngle = 0;
    let targetAngle = 0;

    // Écoute le mouvement de la souris sur toute la scène
    scene.addEventListener('mousemove', (e) => {{
        // Calcul de la position de la souris en % de la largeur (0 à 1)
        const x = e.clientX / window.innerWidth;
        
        // On mappe cette position sur une rotation (ex: de -180 à +180 degrés)
        // Inversez le signe pour changer le sens de rotation
        targetAngle = (x - 0.5) * 360 * 1.5; 
        
        carousel.style.transform = `rotateY(${{targetAngle}}deg)`;
    }});
    
    // Ajout pour le tactile (Mobile)
    scene.addEventListener('touchmove', (e) => {{
        const x = e.touches[0].clientX / window.innerWidth;
        targetAngle = (x - 0.5) * 360 * 2;
        carousel.style.transform = `rotateY(${{targetAngle}}deg)`;
    }});

</script>
</body>
</html>
"""

# --- AFFICHAGE DANS STREAMLIT ---
st.title("🏦 Mes Projets Finance 3D")
st.markdown("Baladez votre souris de gauche à droite pour faire tourner le carrousel 👇")

# On injecte le code HTML avec une hauteur suffisante
components.html(carousel_html, height=650)
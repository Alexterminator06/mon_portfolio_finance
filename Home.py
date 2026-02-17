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

# --- 5. GÉNÉRATION HTML (TECHNIQUE DU DOUBLE FANTÔME) ---
html_cards = ""
angle = 360 / len(projects)
tz = 450 

for i, project in enumerate(projects):
    # On définit le contenu interne d'une carte (les faces)
    # pour pouvoir l'injecter deux fois (la carte réelle + son reflet)
    card_inner_html = f"""
        <div class="face front">
            <a href="{project['link']}" target="_blank" draggable="false">
                <div class="command-content">
                    <div class="icon"></div> <h3>{project['title']}</h3>
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

    html_cards += f"""
    <div class="card-container" style="--angle: {i * angle}deg; --tz: {tz}px;">
        <div class="card main-card">
            {card_inner_html}
        </div>
        
        <div class="card reflection-card">
            {card_inner_html}
        </div>
    </div>
    """

# --- 6. CSS FINAL ---
carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    :root {{
        --w: 260px;
        --h: 360px;
        --d: 20px; /* Épaisseur maintenue */
    }}

    body {{ 
        margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden; 
        background: {bg_css} no-repeat center center fixed; 
        background-size: cover;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
        -webkit-user-select: none; user-select: none;
        cursor: grab;
    }}

    body:active {{ cursor: grabbing; }}

    .scene {{
        width: 100%; height: 100vh;
        perspective: 1200px;
        display: flex; justify-content: center; align-items: center;
    }}

    .carousel {{
        width: var(--w); height: var(--h);
        position: relative; transform-style: preserve-3d;
    }}

    .card-container {{
        position: absolute; 
        width: var(--w); height: var(--h);
        left: 0; top: 0;
        transform-style: preserve-3d;
        transform: rotateY(var(--angle)) translateZ(var(--tz));
        animation: float 6s ease-in-out infinite;
        /* PAS DE REFLECT ICI, C'EST GÉRÉ PAR LA CLASSE .reflection-card */
    }}
    
    .card-container:nth-child(1) {{ animation-delay: 0s; }}
    .card-container:nth-child(2) {{ animation-delay: 1s; }}
    .card-container:nth-child(3) {{ animation-delay: 2s; }}
    .card-container:nth-child(4) {{ animation-delay: 3s; }}
    .card-container:nth-child(5) {{ animation-delay: 4s; }}
    .card-container:nth-child(6) {{ animation-delay: 5s; }}

    @keyframes float {{
        0%, 100% {{ transform: translateY(0px) rotateY(var(--angle)) translateZ(var(--tz)); }}
        50% {{ transform: translateY(-20px) rotateY(var(--angle)) translateZ(var(--tz)); }}
    }}

    /* --- STRUCTURE 3D --- */
    .card {{
        width: 100%; height: 100%;
        position: absolute; /* Important pour superposer reflet et carte */
        transform-style: preserve-3d;
        /* Pas de transition ici, c'est le container qui bouge */
    }}

    /* --- GESTION DU REFLET (LE SECRET) --- */
    .main-card {{
        /* La carte principale est en position normale */
        z-index: 2;
    }}

    .reflection-card {{
        /* On inverse la carte verticalement et on la descend */
        /* translateY(100%) = descend de sa propre hauteur */
        /* + 10px = le petit espace entre la carte et le sol */
        /* scaleY(-1) = effet miroir */
        transform: translateY(calc(100% + 10px)) scaleY(-1);
        
        opacity: 0.4; /* Transparence du reflet */
        pointer-events: none; /* On ne peut pas cliquer sur le reflet */
        
        /* Masque pour effacer le reflet progressivement vers le bas */
        -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 60%);
        mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 60%);
        
        z-index: 1;
    }}

    .face {{
        position: absolute; 
        box-shadow: inset 0 0 20px rgba(0,0,0,0.3);
    }}

    /* 1. DEVANT */
    .front {{
        width: var(--w); height: var(--h);
        background: {marble_css}; background-size: cover; background-position: center;
        display: flex; justify-content: center; align-items: center;
        transform: translateZ(calc(var(--d) / 2)); 
 
    }}


    /* 2. DERRIÈRE */
    .back {{
        width: var(--w); height: var(--h);
        background: {marble_css}; background-size: cover; background-position: center;
        filter: brightness(0.6);
        display: flex; justify-content: center; align-items: center;
        transform: rotateY(180deg) translateZ(calc(var(--d) / 2));
    }}

    /* 3. DROITE */
    .right {{
        width: var(--d); height: var(--h);
        background: {marble_css}; background-size: cover; background-position: center;
        filter: brightness(0.8); 
        left: calc((var(--w) - var(--d)) / 2);
        transform: translateX(calc(var(--w) / 2)) rotateY(90deg);
    }}

    /* 4. GAUCHE */
    .left {{
        width: var(--d); height: var(--h);
        background: {marble_css}; background-size: cover; background-position: center;
        filter: brightness(0.6); 
        left: calc((var(--w) - var(--d)) / 2);
        transform: translateX(calc(var(--w) / -2)) rotateY(-90deg);
    }}

    /* --- CONTENU --- */
    .command-content {{ text-align: center; padding: 15px; width: 100%; }}
    .icon {{ font-size: 1.5rem; margin-bottom: 5px; color: #B8860B; text-shadow: 1px 1px 0px rgba(255,255,255,0.8); }}
    .command-content h3 {{ margin: 0; font-family: 'Great Vibes', cursive; font-size: 2.8rem; line-height: 1.1; color: #B8860B; text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.8), 0px 0px 1px rgba(0,0,0,0.2); font-weight: normal; }}
    .separator {{ width: 50px; height: 1px; background: #B8860B; margin: 10px auto; opacity: 0.6; }}
    .command-content p {{ margin: 0; font-family: 'Great Vibes', cursive; font-size: 1.6rem; color: #5c4033; text-shadow: 0px 1px 0px rgba(255,255,255,0.6); }}
    
    .back-design {{ text-align: center; opacity: 0.6; }}
    .back-design .logo {{ font-size: 3rem; color: #333; }}
    .back-design .text {{ font-size: 0.6rem; letter-spacing: 3px; color: #333; font-weight: bold; }}
    
    a {{ text-decoration: none; color: inherit; display: block; height: 100%; display: flex; align-items: center; justify-content: center; -webkit-user-drag: none; }}
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
    
    // --- VITESSE DE ROTATION AUTO ---
    let autoSpeed = -0.025; // Ajuste ici pour accélérer/ralentir
    
    let isDragging = false, startX = 0, currentRotation = 0, velocity = 0, lastX = 0;

    // Souris
    scene.addEventListener('mousedown', (e) => {{ isDragging = true; startX = e.clientX; lastX = e.clientX; velocity = 0; document.body.style.cursor = "grabbing"; }});
    window.addEventListener('mousemove', (e) => {{ 
        if (!isDragging) return; 
        const x = e.clientX; velocity = (x - lastX) * 0.3; currentRotation += velocity; 
        // Note: Doubles accolades pour ${{ }} dans f-string Python pour générer JS template literal
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`; 
        lastX = x; 
    }});
    window.addEventListener('mouseup', () => {{ isDragging = false; document.body.style.cursor = "grab"; }});

    // Tactile
    scene.addEventListener('touchstart', (e) => {{ isDragging = true; startX = e.touches[0].clientX; lastX = e.touches[0].clientX; velocity = 0; }});
    window.addEventListener('touchmove', (e) => {{ 
        if (!isDragging) return; 
        const x = e.touches[0].clientX; velocity = (x - lastX) * 0.5; currentRotation += velocity; 
        carousel.style.transform = `rotateY(${{currentRotation}}deg)`; 
        lastX = x; 
    }});
    window.addEventListener('touchend', () => {{ isDragging = false; }});

    // Boucle d'animation (Inertie + Auto-rotation)
    function animate() {{
        requestAnimationFrame(animate);

        if (!isDragging) {{
            // Frottement
            velocity *= 0.95;
            // On ajoute la vélocité (élan) ET la vitesse auto
            currentRotation += velocity + autoSpeed;
            
            carousel.style.transform = `rotateY(${{currentRotation}}deg)`;
        }}
    }}
    animate();
</script>
</body>
</html>
"""

components.html(carousel_html, height=1000, scrolling=False)
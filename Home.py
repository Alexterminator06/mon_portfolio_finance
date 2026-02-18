import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import json

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio Prestige", page_icon="🏛️")

# --- 2. FONCTIONS ROBUSTES ---
def get_base64_image(image_filename):
    # Liste de tous les dossiers où vous rangez vos images
    folders_to_search = [
        os.path.join("assets", "portfolio hedge"),
        os.path.join("assets", "bitcoin option"),
        "assets", # Dossier racine des assets
        "."       # Dossier racine du projet
    ]
    
    for folder in folders_to_search:
        path = os.path.join(folder, image_filename)
        
        if os.path.exists(path):
            try:
                with open(path, "rb") as img_file:
                    encoded = base64.b64encode(img_file.read()).decode()
                
                ext = os.path.splitext(path)[1].lower().replace('.', '')
                if ext == 'jpg': ext = 'jpeg'
                return f"data:image/{ext};base64,{encoded}"
            except Exception as e:
                print(f"Erreur sur {path}: {e}")
                return None
                
    print(f"⚠️ Image non trouvée : {image_filename}")
    return None
    
def load_report_with_images(filename, image_map={}):
    file_path = os.path.join("reports", filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        for placeholder, img_name in image_map.items():
            img_b64 = get_base64_image(img_name)
            if img_b64:
                # On cherche {MON_MARQUEUR} et on remplace par le code base64
                content = content.replace(f"{{{placeholder}}}", img_b64)
            else:
                print(f"Echec remplacement pour {placeholder}")
        return content
    return "<p>Rapport introuvable.</p>"

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
        "id": 0,
        "title": "Hedging a Portfolio",
        "desc_short": "Greek Constraints",
        "desc_long": "This project implements a machine learning strategy to hedge a portfolio of derivatives, aiming to predict optimal hedge ratios while minimizing Greek risks (Delta, Gamma, Vega). By training a Hybrid/Ensemble model on synthetic data from Monte Carlo simulations, the approach outperforms traditional Black-Scholes models in adhering to strict risk constraints.",
        "tech": ["Python", "Derivatives Pricing","Risk Management", "Machine Learning","Model Optimization"],
        "link_github": "https://github.com/TeoBourscheidt/Machine_learning",
        "report_html": load_report_with_images("rapport_machine_learning.html", image_map={
                "IMG_DATA_ANALYSIS": "data analysis.jpg",
                "IMG_CORR": "correlation matrix.jpg",
                "IMG_COMPA": "value comparison.jpg",
                "IMG_COMPA2": "value comparison 2.jpg"
            })
    },
    {
       "id": 1,
        "title": "Option Pricing",
        "desc_short": "Bitcoin",
        "desc_long": "This project analyzes Bitcoin's price volatility over a one-year period to test the applicability of the Black-Scholes model for pricing European options. Using daily data from Yahoo Finance, the study calculates key risk metrics like annualized volatility and excess kurtosis to highlight Bitcoin's fat-tail distribution, which challenges traditional model assumptions . The tool was implemented in both Excel and VBA to ensure mathematical accuracy through cross-verification.",
        "tech": ["VBA", "Excel", "Statistics", "Data Engineering", "Quantitative Finance"],
        "report_html": load_report_with_images("rapport_VBA.html", image_map={
                "IMG_BTC": "bitcoin price.jpg",
                "IMG_LOG": "log return.jpg",
                "IMG_CP": "call put.jpg",
            })
    },
    {
        "id": 2,
        "title": "Financial Dashboard",
        "desc_short": "Single Asset / Portfolio Not ready yet",
        "desc_long": "Not ready yet",



    },
    {
        "id": 3,
        "title": "Trading Bot",
        "desc_short": "Trading Automatique Not ready yet",
        "desc_long": "Not ready yet",



    },
     {
        "id": 4,
        "title": "Bank Solvency",
        "desc_short": "Indice Computing",
        "desc_long": "Not ready yet Not ready yet",


    },
    {
        "id": 5,
        "title": "Commoditiy Trading",
        "desc_short": "Brent Crude",
        "desc_long": "Not ready yet Not ready yet",

    }
]


projects_json = json.dumps(projects)

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
        <div class="face front" onclick="openModal({i})">
            <div class="command-content">
                <div class="icon"></div> 
                <h3>{project['title']}</h3>
                <div class="separator"></div>
                <p>{project['desc_short']}</p>
            </div>
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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<script>
  window.MathJax = {{
    tex: {{
      inlineMath: [['$', '$']], 
      displayMath: [['$$', '$$']]
    }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
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
        background-repeat: no-repeat !important; /* Empêche la répétition */
        background-size: cover !important;       /* Force l'image à couvrir l'écran */
        background-position: center center !important; /* Centre l'image */
        z-index: 0;
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
    /* --- CARROUSEL WRAPPER (MOBILE FIX) --- */
    .scene-wrapper {{
        position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
        opacity: 0; z-index: 20; pointer-events: none; transition: opacity 0.5s ease;
    }}
    
    .scene-wrapper.active {{ 
        pointer-events: auto; 
        cursor: grab;
        
        /* LA CLEF POUR MOBILE : Empêche le navigateur de scroller quand on touche cette zone */
        touch-action: none; 
    }}
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
        font-size: 2rem; line-height: 1.1; 
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

    /* ========================================= */
    /* ===  MODALE DE LUXE (POP-UP)          === */
    /* ========================================= */
    .modal-overlay {{
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.85); /* Fond noir très opaque */
        backdrop-filter: blur(8px); /* Effet verre flouté */
        z-index: 1000;
        opacity: 0; pointer-events: none;
        transition: opacity 0.4s ease;
        display: flex; justify-content: center; align-items: center;
    }}
    
    .modal-overlay.open {{ opacity: 1; pointer-events: auto; }}

    .modal-card {{
        max-width: 90%;
        max-height: 90%;
        background: #F8F3E6;
        border: 1px solid #D4AF37; /* Bordure Or */
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.2);
        padding: 40px;
        text-align: center;
        position: relative;
        transform: translateY(50px);
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .modal-overlay.open .modal-card {{ transform: translateY(0); }}

    .modal-title {{
        font-family: 'Cinzel', serif; color: #1a1a1a; font-size: 2rem; margin-bottom: 20px;
        text-transform: uppercase; letter-spacing: 2px;
        border-bottom: 1px solid #333; padding-bottom: 15px;
    }}

    .modal-desc {{
        font-family: 'Helvetica Neue', sans-serif; color: #1a1a1a; font-size: 1rem; line-height: 1.6;
        margin-bottom: 30px; font-weight: 300;
    }}

    .tech-stack {{ margin-bottom: 30px; }}
    .tech-tag {{
        display: inline-block; padding: 5px 10px; margin: 3px;
        border: 1px solid #1a1a1a; color: #1a1a1a; font-size: 0.8rem;
        border-radius: 4px; text-transform: uppercase; letter-spacing: 1px;
    }}

    #view-report {{ display: none; text-align: left; overflow-y: auto; padding-right: 10px; animation: fadeIn 0.5s; max-height: 60vh; }}
    #report-content {{ color: #1a1a1a; font-family: 'Helvetica Neue', sans-serif; line-height: 1.8; }}
    /* STYLE DES MATHS */
    #report-content h3 {{ color: #D4AF37; font-family: 'Cinzel', serif; border-bottom: 1px solid #333; padding-bottom: 5px; margin-top: 20px; }}
    #report-content p {{ margin-bottom: 15px; }}

    #report-content strong {{ color: #1a1a1a; }}
    .modal-buttons {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }}

    .btn {{
        padding: 12px 25px; text-decoration: none; font-family: 'Cinzel', serif; font-weight: bold;
        transition: all 0.3s ease; cursor: pointer; text-transform: uppercase; letter-spacing: 1px;
        font-size: 0.9rem;
    }}

    .btn-gold {{
        background: #D4AF37; color: #000; border: 1px solid #D4AF37;
    }}
    .btn-gold:hover {{ background: #fff; border-color: #fff; }}

    .btn-outline {{
        background: transparent; color: #D4AF37; border: 1px solid #D4AF37;
    }}
    .btn-outline:hover {{ background: rgba(212, 175, 55, 0.1); }}

    .btn-back {{
        color: #000; border: 1px solid #D4AF37;
    }}
    

    .close-modal {{
        position: absolute; top: 15px; right: 20px;
        color: #555; font-size: 2rem; cursor: pointer; transition: color 0.3s;
    }}
    .close-modal:hover {{ color: #D4AF37; }}

/* ========================================= */
    /* ===  MEDIA QUERIES (MODE MOBILE)      === */
    /* ========================================= */
    @media only screen and (max-width: 768px) {{
        
        /* 1. On réduit la taille des titres */
        .intro-text h1 {{
            font-size: 1.8rem; /* Beaucoup plus petit */
            letter-spacing: 2px;
        }}
        .intro-text h2 {{
            font-size: 2.5rem; /* Adapté à l'écran vertical */
        }}

        /* 2. On réduit la taille TOTALE de la scène 3D */
        /* C'est l'astuce magique : on zoome arrière de 45% */
        .scene {{
            transform: scale(0.45); 
        }}

        /* 3. On ajuste la hauteur de scroll pour mobile */
        body {{
            height: 350vh;
        }}
        
        /* 4. On remonte un peu le carrousel car le scale le fait descendre visuellement */
        .carousel {{
            top: -50px;
        }}
    }}

    
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
    <div class="modal-overlay" id="modal-overlay">
        <div class="modal-card">
            <div class="close-modal" onclick="closeModal()">×</div>
            
            <div id="view-summary">
                <h2 class="modal-title" id="m-title"></h2>
                <p class="modal-desc" id="m-desc"></p>
                <div id="m-tech"></div>
                
                <div class="modal-buttons">
                    <a href="#" target="_blank" class="btn btn-outline" id="m-code">See Code</a>
                    <div class="btn btn-gold" onclick="showReport()">Read Report</div>
                </div>
            </div>

            <div id="view-report">
                <div class="btn-back" onclick="hideReport()">← Back</div>
                <div id="report-content">
                    </div>
            </div>

        </div>
    </div>

<script>
    const projectsData = {projects_json};
    const sceneWrapper = document.getElementById('scene-wrapper');
    const intro1 = document.getElementById('intro1'); const intro2 = document.getElementById('intro2');
    const bg1 = document.getElementById('bg1'); const bg2 = document.getElementById('bg2'); const bg3 = document.getElementById('bg3');
    const scene3d = document.getElementById('scene-3d');
    const carousel = document.getElementById('carousel');
    const modalOverlay = document.getElementById('modal-overlay');
    
    const mTitle = document.getElementById('m-title'); 
    const mDesc = document.getElementById('m-desc');
    const mTech = document.getElementById('m-tech'); 
    const mCode = document.getElementById('m-code');
    
    const viewSummary = document.getElementById('view-summary');
    const viewReport = document.getElementById('view-report');
    const reportContent = document.getElementById('report-content');
    
    let currentProject = null;

    function openModal(index) {{
        currentProject = projectsData[index];
        
        // Remplissage des textes
        mTitle.innerText = currentProject.title;
        mDesc.innerText = currentProject.desc_long;
        
        // Gestion des tags techniques
        mTech.innerHTML = "";
        currentProject.tech.forEach(t => mTech.innerHTML += `<span class="tech-tag">${{t}}</span>`);

        // --- GESTION DU BOUTON GITHUB (CODE) ---
        // On considère que si le lien est "#" ou vide, il n'y a pas de code dispo
        if (currentProject.link_github && currentProject.link_github !== "#" && currentProject.link_github !== "") {{
            mCode.href = currentProject.link_github;
            mCode.style.display = "inline-block"; // On affiche le bouton
        }} else {{
            mCode.style.display = "none"; // On cache le bouton
        }}

        // Réinitialisation des vues de la modale
        viewSummary.style.display = "block";
        viewReport.style.display = "none";

        modalOverlay.classList.add('open');
        scene3d.style.filter = "blur(10px) brightness(0.5)";
    }}

    function closeModal() {{
        modalOverlay.classList.remove('open');
        scene3d.style.filter = "none";
    }}
    
    function showReport() {{
        if (currentProject.report_html) {{
            reportContent.innerHTML = currentProject.report_html;
            
            // --- MAGIE MATHJAX ---
            // On demande à MathJax de "re-scanner" la zone du rapport pour afficher les formules
            if (window.MathJax) {{
                MathJax.typesetPromise([reportContent]).then(() => {{
                    console.log('Mathématiques affichées !');
                }}).catch((err) => console.log('Erreur MathJax: ' + err.message));
            }}
            
        }} else {{
            reportContent.innerHTML = "<p>Rapport détaillé non disponible.</p>";
        }}
        
        viewSummary.style.display = "none";
        viewReport.style.display = "block";
    }}

    function hideReport() {{
        viewReport.style.display = "none";
        viewSummary.style.display = "block";
    }}

    modalOverlay.addEventListener('click', (e) => {{ if (e.target === modalOverlay) closeModal(); }});

    // SCROLL
    let autoSpeed = -0.025; let isDragging = false, startX = 0, currentRotation = 0, velocity = 0, lastX = 0;
    window.addEventListener('scroll', () => {{
        const scrollY = window.scrollY; const h = window.innerHeight;
        let op1 = 1 - (scrollY / (h * 0.6)); intro1.style.opacity = Math.max(0, op1); intro1.style.transform = `translate(-50%, -50%) scale(${{1 - scrollY * 0.0002}})`;
        let op2 = 0; if (scrollY > h * 0.8 && scrollY < h * 2.2) {{ if (scrollY < h * 1.2) op2 = (scrollY - h * 0.8) / (h * 0.4); else if (scrollY < h * 1.8) op2 = 1; else op2 = 1 - (scrollY - h * 1.8) / (h * 0.4); }} intro2.style.opacity = Math.max(0, op2); intro2.style.transform = `translate(-50%, -50%) scale(${{0.8 + (scrollY - h) * 0.0005}})`;
        let bg2Op = (scrollY > h * 0.5) ? (scrollY - h * 0.5) / (h * 0.7) : 0; bg2.style.opacity = Math.min(1, Math.max(0, bg2Op));
        let bg3Op = (scrollY > h * 1.8) ? (scrollY - h * 1.8) / (h * 0.7) : 0; bg3.style.opacity = Math.min(1, Math.max(0, bg3Op));
        let sceneOp = (scrollY > h * 2.0) ? (scrollY - h * 2.0) / (h * 0.5) : 0; sceneWrapper.style.opacity = Math.min(1, Math.max(0, sceneOp));
        if (sceneOp > 0.9) sceneWrapper.classList.add('active'); else sceneWrapper.classList.remove('active');
    }});

    window.addEventListener('touchstart', (e) => {{ if (modalOverlay.classList.contains('open')) return; if (!sceneWrapper.classList.contains('active')) return; isDragging = true; startX = e.touches[0].clientX; lastX = e.touches[0].clientX; velocity = 0; }}, {{ passive: false }});
    window.addEventListener('touchmove', (e) => {{ if (modalOverlay.classList.contains('open')) return; if (!isDragging) return; if(e.cancelable) e.preventDefault(); const x = e.touches[0].clientX; velocity = (x - lastX) * 0.5; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; }}, {{ passive: false }});
    window.addEventListener('touchend', () => {{ isDragging = false; }});
    window.addEventListener('mousedown', (e) => {{ if (modalOverlay.classList.contains('open')) return; if (!sceneWrapper.classList.contains('active')) return; isDragging = true; startX = e.clientX; lastX = e.clientX; velocity = 0; document.body.style.cursor = "grabbing"; }});
    window.addEventListener('mousemove', (e) => {{ if (!isDragging) return; const x = e.clientX; velocity = (x - lastX) * 0.3; currentRotation += velocity; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; lastX = x; }});
    window.addEventListener('mouseup', () => {{ isDragging = false; if (sceneWrapper.classList.contains('active')) document.body.style.cursor = "grab"; }});
    function animate() {{ requestAnimationFrame(animate); if (!isDragging && !modalOverlay.classList.contains('open')) {{ velocity *= 0.95; currentRotation += velocity + autoSpeed; carousel.style.transform = `rotateY(${{currentRotation}}deg)`; }} }}
    animate();
    window.dispatchEvent(new Event('scroll'));
</script>
</body>
</html>
"""
components.html(carousel_html, height=2000, scrolling=True)
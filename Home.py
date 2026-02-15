import streamlit as st
import base64

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Portfolio Finance",
    page_icon="🏦",
    layout="wide"
)

# --- FONCTION POUR LES IMAGES CLIQUABLES ---
# Cette fonction permet de transformer une image locale en lien HTML
def clickable_image(image_path, link_url, title, height="200px"):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        # Code HTML/CSS pour l'effet "carte"
        html_code = f"""
        <div style="
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 10px; 
            margin-bottom: 20px;
            transition: transform 0.2s; 
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
            <a href="{link_url}" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="data:image/jpeg;base64,{encoded_string}" 
                     style="width: 100%; height: {height}; object-fit: cover; border-radius: 5px;">
                <h3 style="text-align: center; margin-top: 10px; font-family: sans-serif;">{title}</h3>
            </a>
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Image introuvable : {image_path}")

# --- EN-TÊTE ---
st.title("🏦 Mon Hub de Projets Finance")
st.markdown("""
Bienvenue sur mon portfolio. Cliquez sur une image ci-dessous pour lancer 
l'application interactive correspondante (hébergée sur le cloud).
""")
st.write("---")

# --- GRILLE DES PROJETS ---
# On crée 3 colonnes pour afficher les projets côte à côte
col1, col2, col3 = st.columns(3)

# PROJET 1 : trading bot
with col1:
    clickable_image(
        image_path="assets/projet_bourse.jpg",  # Assurez-vous d'avoir cette image
        link_url="https://bitcoin-trading-bot.streamlit.app/", # Mettez le vrai lien ici
        title="🤖 Bot de Trading"
    )

# PROJET 2 : Bot Trading
with col2:
    clickable_image(
        image_path="assets/projet_crypto.jpg", 
        link_url="https://mon-bot-bitcoin.streamlit.app", 
        title="🤖 Bot Trading Bitcoin"
    )

# PROJET 3 : Pricing Options
with col3:
    clickable_image(
        image_path="assets/projet_option.jpg", 
        link_url="https://mon-pricing-options.streamlit.app", 
        title="🧮 Pricing Black-Scholes"
    )

# --- PIED DE PAGE ---
st.write("---")
st.markdown("Codé en Python | Hébergé sur Streamlit Community Cloud")
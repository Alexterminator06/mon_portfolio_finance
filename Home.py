import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Portfolio Finance",
    page_icon="🏦",
    layout="wide"
)

# Sidebar (Menu latéral)
st.sidebar.success("Sélectionnez un projet ci-dessus ☝️")

# En-tête
st.title("🏦 Mon Portfolio de Projets Finance")
st.markdown("### Bienvenue ! Je suis [Votre Nom], Analyste Financier / Data Scientist.")
st.write("---")

# Section Présentation
col1, col2 = st.columns([1, 2])

with col1:
    # Vous pourrez ajouter une photo plus tard
    st.info("👋 **À propos de moi**\n\nPassionné par la modélisation financière et Python.\n\nCe site regroupe mes projets interactifs.")

with col2:
    st.markdown("""
    ### 🎯 Objectif du site
    Ce portfolio est **entièrement interactif**. Contrairement à un site statique, 
    vous pouvez ici manipuler les données, changer les paramètres des modèles 
    et voir les résultats en temps réel.
    
    ### 🛠 Technologies utilisées
    * **Python** (Cœur des calculs)
    * **Streamlit** (Interface Web)
    * **Pandas & NumPy** (Traitement de données)
    * **Yahoo Finance API** (Données de marché)
    """)

st.write("---")

# Liste des projets (Aperçu)
st.header("🗂 Mes Projets")

st.markdown("""
* **📈 Analyse Boursière & Technique :** Visualisation de cours et indicateurs (RSI, Bollinger).
* **💰 Optimisation de Portefeuille :** Frontière efficiente de Markowitz.
* **🧮 Pricing d'Options :** Modèle Black-Scholes interactif.
""")

st.info("👈 **Utilisez le menu à gauche pour naviguer vers les projets et tester les interfaces.**")
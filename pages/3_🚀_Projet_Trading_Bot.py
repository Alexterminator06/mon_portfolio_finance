import streamlit as st
import sys
import os

# --- CONFIGURATION DU CHEMIN ---
# On récupère le chemin absolu du dossier actuel
current_dir = os.path.dirname(os.path.abspath(__file__))
# On remonte d'un cran pour aller à la racine du portfolio
root_dir = os.path.dirname(current_dir)
# On construit le chemin vers votre dossier projet
project_path = os.path.join(root_dir, "Bitcoin-Trading-Bot")

# On ajoute ce dossier au "path" de Python pour qu'il puisse trouver 'utils.py' etc.
if project_path not in sys.path:
    sys.path.append(project_path)

# --- IMPORTATION DU PROJET ---
# Maintenant on peut importer le fichier principal de votre projet
# (Assurez-vous que le fichier s'appelle bien main_interface.py ou changez le nom ici)
try:
    import app as bot_app
except ImportError as e:
    st.error(f"Erreur d'importation : {e}")
    st.stop()

# --- LANCEMENT ---
# On configure la page (optionnel si déjà fait dans le bot)
# st.set_page_config(...) # Attention : set_page_config ne peut être appelé qu'une fois par chargement

# On appelle la fonction principale qu'on a créée à l'étape 2
bot_app.app()
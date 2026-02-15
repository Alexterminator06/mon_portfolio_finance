import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="Analyse Boursière", page_icon="📈")

st.title("📈 Analyse Boursière Interactive")
st.markdown("Récupérez les données de marché en temps réel et visualisez les prix.")

# --- INTERACTIVITÉ ---
# L'utilisateur choisit ses paramètres ici
col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Symbole Ticker (ex: AAPL, MSFT, ^CAC40)", "AAPL")
with col2:
    start_date = st.date_input("Date de début", pd.to_datetime("2023-01-01"))
with col3:
    end_date = st.date_input("Date de fin", pd.to_datetime("today"))

# Bouton pour lancer l'analyse
if st.button("🔍 Analyser"):
    with st.spinner('Récupération des données...'):
        try:
            # Téléchargement des données
            df = yf.download(ticker, start=start_date, end=end_date)
            
            if df.empty:
                st.error("Aucune donnée trouvée. Vérifiez le symbole.")
            else:
                # Affichage des stats
                st.subheader(f"Données pour {ticker}")
                st.write(df.tail())
                
                # Graphique Interactif (Plotly)
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'],
                                close=df['Close'],
                                name='market data'))
                
                fig.update_layout(title=f'Cours de {ticker}', yaxis_title='Prix Stock ($)')
                st.plotly_chart(fig, use_container_width=True)
                
                # Exemple de téléchargement (feature pro)
                csv = df.to_csv().encode('utf-8')
                st.download_button(
                    label="📥 Télécharger les données en CSV",
                    data=csv,
                    file_name=f'{ticker}_data.csv',
                    mime='text/csv',
                )
                
        except Exception as e:
            st.error(f"Une erreur est survenue: {e}")
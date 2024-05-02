import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Titre de l'application
st.title('Ma première application Streamlit')

# Sélecteur de texte
option = st.selectbox('Choisissez une option', ['Option 1', 'Option 2', 'Option 3'])
st.write('Vous avez sélectionné :', option)
# Curseur
valeur = st.slider('Sélectionnez une valeur', 0, 100, 50)
st.write('Valeur sélectionnée :', valeur)
 # Affichage de données tabulaires

df = pd.DataFrame({
 'Nom': ['Alice', 'Bob', 'Charlie'],
 'Âge': [30, 35, 40]
 })
st.write(df)

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique de sin(x)')
st.pyplot()
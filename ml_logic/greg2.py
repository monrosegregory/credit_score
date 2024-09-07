import pandas as pd

# Lire le fichier CSV dans un DataFrame
df_static_values = pd.read_csv('raw_data/df_cleaned_31082024.csv')

# Afficher les noms des colonnes
print(df_static_values.columns)

import pandas as pd

# 1. Cargar el archivo original
nombre_archivo = 'Top 1000 games of all time.csv.xlsx'
df = pd.read_excel(nombre_archivo)

# 2. Limpiar el año (dejar únicamente los 4 dígitos)
df['Year'] = df['Year'].str.extract(r'(\d{4})').astype('Int64')

# 3. Separar los géneros en 3 columnas independientes (Genre_1, Genre_2, Genre_3)
generos = df['Genre'].str.split(',', expand=True)
for i in range(generos.shape[1]):
    df[f'Genre_{i+1}'] = generos[i].str.strip()

# 4. Eliminar la columna Genre original
df = df.drop(columns=['Genre'])

# 5. Guardar los resultados procesados
df.to_csv('Top_1000_Games_Procesado.csv', index=False)
df.to_json('games_data.json', orient='records')

print("¡Listo! Se crearon los archivos Top_1000_Games_Procesado.csv y games_data.json en tu carpeta.")
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conexión
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jesp2684@",
    database="curso_sql"
)

# Consulta SQL
query = "SELECT * FROM titanic;"
df = pd.read_sql(query, conn)

# Análisis
print(df.head())
print(df['Sobreviviente'].mean() * 100, "% sobrevivieron")

# Agrupar por clase y género
resultados = df.groupby(['Clase', 'Genero'])['Sobreviviente'].mean().reset_index()

# Mostrar
print(resultados)



resultados_pivot = resultados.pivot(index='Clase', columns='Genero', values='Sobreviviente')

resultados_pivot.plot(kind='bar')
plt.title("Tasa de Supervivencia por Clase y Género")
plt.xlabel("Clase")
plt.ylabel("Tasa de Supervivencia")
plt.xticks(rotation=0)
plt.legend(["Hombres", "Mujeres"])
plt.show()

# Ver tipos y valores nulos
print(df.info())
print(df.isnull().sum())

# Renombrar columnas a un formato más legible
df.rename(columns={
    'PassengerId': 'ID',
    'Survived': 'Sobreviviente',
    'Pclass': 'Clase',
    'Sex': 'Genero',
    'Age': 'Edad',
    'SibSp': 'Hermanos_Cónyuge',
    'Parch': 'Padres_Hijos',
    'Fare': 'Tarifa'
}, inplace=True)

# Convertir columnas categóricas
df['Genero'] = df['Genero'].astype('category')
df['Clase'] = df['Clase'].astype('category')

# Tasa global
tasa_global = df['Sobreviviente'].mean() * 100
print(f"Tasa de supervivencia global: {tasa_global:.2f}%")

# Por género
tasa_genero = df.groupby('Genero')['Sobreviviente'].mean() * 100
print("\nTasa de supervivencia por género:\n", tasa_genero)

# Por clase
tasa_clase = df.groupby('Clase')['Sobreviviente'].mean() * 100
print("\nTasa de supervivencia por clase:\n", tasa_clase)

resultados_pivot.plot(
    kind='bar',
    stacked=True,
    color=['steelblue', 'lightcoral']
)
plt.title("Tasa de Supervivencia por Clase y Género", fontsize=14)
plt.xlabel("Clase")
plt.ylabel("Tasa de Supervivencia")
plt.xticks(rotation=0)
plt.legend(["Hombres", "Mujeres"])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8,5))
for sobrevivio in [0, 1]:
    subset = df[df['Sobreviviente'] == sobrevivio]
    plt.hist(subset['Edad'], bins=20, alpha=0.6, label=f"Sobreviviente={sobrevivio}")

plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")
plt.title("Distribución de edades por supervivencia")
plt.legend(["No sobrevivió", "Sobrevivió"])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Exportar resultados a CSV
resultados.to_csv("/Users/ernesto/Desktop/titanic_analysis_mysql/outputs/analisis_supervivencia.csv", index=False)


# Exportar a Excel
resultados.to_excel("/Users/ernesto/Desktop/titanic_analysis_mysql/outputs/analisis_supervivencia.xlsx", index=False)


plt.savefig("/Users/ernesto/Desktop/titanic_analysis_mysql/outputs/grafico_tasa_supervivencia.png")

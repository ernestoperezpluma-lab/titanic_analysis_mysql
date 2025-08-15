# Análisis de Supervivencia en el Titanic usando MySQL y Python

Este proyecto conecta una base de datos MySQL con Python para analizar el famoso dataset del Titanic. 
Se realizan consultas SQL, limpieza de datos, generación de estadísticas y visualizaciones para entender los factores que influyeron en la supervivencia.

## Estructura del proyecto
- **data/** → Datos originales (CSV)
- **src/** → Script principal en Python
- **outputs/** → Gráficas y reportes generados

## Tecnologías usadas
- Python 3
- Pandas
- Matplotlib
- MySQL
- mysql-connector-python

## Principales hallazgos
- Tasa global de supervivencia: 38.38%
- Las mujeres sobrevivieron a una tasa del 74%, frente al 19% de los hombres.
- La Clase 1 tuvo una tasa de supervivencia del 63%, mientras que la Clase 3 fue del 24%.

## Cómo ejecutar el proyecto
1. Clona el repositorio o descarga este proyecto.
2. Asegúrate de tener Python y MySQL configurados.
3. Ejecuta el script principal desde la carpeta `src/`:
```bash
python titanic_analysis.py

{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # An\'e1lisis de Supervivencia en el Titanic usando MySQL y Python\
\
Este proyecto conecta una base de datos MySQL con Python para analizar el famoso dataset del Titanic. \
Se realizan consultas SQL, limpieza de datos, generaci\'f3n de estad\'edsticas y visualizaciones para entender los factores que influyeron en la supervivencia.\
\
## Estructura del proyecto\
- **data/** \uc0\u8594  Datos originales (CSV)\
- **src/** \uc0\u8594  Script principal en Python\
- **outputs/** \uc0\u8594  Gr\'e1ficas y reportes generados\
\
## Tecnolog\'edas usadas\
- Python 3\
- Pandas\
- Matplotlib\
- MySQL\
- mysql-connector-python\
\
## Principales hallazgos\
- Tasa global de supervivencia: 38.38%\
- Las mujeres sobrevivieron a una tasa del 74%, frente al 19% de los hombres.\
- La Clase 1 tuvo una tasa de supervivencia del 63%, mientras que la Clase 3 fue del 24%.\
\
## C\'f3mo ejecutar el proyecto\
1. Clona el repositorio o descarga este proyecto.\
2. Aseg\'farate de tener Python y MySQL configurados.\
3. Ejecuta el script principal desde la carpeta `src/`:\
```bash\
python titanic_analysis.py\
}
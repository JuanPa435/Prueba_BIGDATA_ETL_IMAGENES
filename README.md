# Prueba_BIGDATA_ETL_IMAGENES

Proyecto de ejemplo para un pipeline ETL (Extract, Transform, Load) y visualizaciones sobre un dataset de noticias con análisis de sentimiento.

## Resumen
Este repositorio contiene un flujo ETL sencillo que:
- Extrae datos desde `Data/stock_senti_analysis.csv` (o `RAW_FILE` configurado)
- Transforma/limpia el dataset (normaliza columnas, quita duplicados, corrige comas en comillas)
- Carga los datos en CSV y SQLite
- Genera visualizaciones básicas y un heatmap (proporción de Label=1 por año y mes)

Las gráficas se guardan en la carpeta configurada en `Config/Config_ETL.py` (`PLOTS_DIR`).

## Requisitos
- Python 3.10+
- Paquetes (ver `requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - seaborn (opcional, usado si está disponible para heatmap)
  - scikit-learn (opcional)
  - wordcloud (opcional)
  - sqlalchemy, pymysql, python-dotenv, chardet, requests (según uso)

Si quieres instalar las dependencias recomendadas:

```bash
pip install -r requirements_clean.txt
```

> Nota: `requirements.txt` en el repo puede contener formato original; `requirements_clean.txt` incluye una lista normalizada.

## Estructura del proyecto
```
/ (raíz)
  - Main.py                # Orquestador del ETL y EDA
  - requirements.txt       # Dependencias del proyecto (original)
  - requirements_clean.txt # Lista limpia de dependencias (recomendada)
  - README.md
  - Config/
	  - Config_ETL.py      # Rutas y constantes (RAW_FILE, CLEAN_FILE, PLOTS_DIR...)
  - Extract/
	  - Extract_ETL.py     # Lógica de extracción
  - Transform/
	  - Transform_ETL.py   # Lógica de transformación y función transform_data(df)
	  - Visualize_ETL.py   # Genera las gráficas
  - Load/
	  - Load_ETL.py        # Guardado a CSV y SQLite
  - Data/
	  - stock_senti_analysis.csv  # Dataset de noticias (ejemplo)
	  - plots/             # Directorio donde se guardan imágenes
```

## Cómo usar
1. Clona el repositorio y sitúate en la carpeta raíz.

2. Instala dependencias (recomendado):

```bash
pip install -r requirements.txt
```

3. Ejecutar el pipeline completo:

```bash
python Main.py
```

Esto ejecuta: extracción -> transformación -> carga -> generación de gráficas.

### Ejecutar solo partes (ejemplos)
- Ejecutar solo extracción:
```python
from Extract.Extract_ETL import extract_data
df = extract_data()
```

- Ejecutar solo la transformación en memoria:
```python
from Extract.Extract_ETL import extract_data
from Transform.Transform_ETL import transform_data

df = extract_data()
df_clean = transform_data(df, save=False)
```

- Ejecutar solo visualizaciones (requiere Data ya cargada/limpia):
```python
from Transform.Visualize_ETL import run_visualizations
import pandas as pd

df = pd.read_csv('Data/cleaned_stock_senti.csv', parse_dates=['Date'])
run_visualizations(df)
```

## Visualizaciones generadas
- `basic_1_label_distribution.png` — distribución de etiquetas (0/1)
- `basic_2_news_by_year.png` — número de noticias por año
- `basic_3_label_heatmap.png` — heatmap año×mes con proporción de Label=1
- `basic_4_top1_length_hist.png` — histograma de longitud de `top1` (palabras)
- `basic_5_top10_words_top1.png` — top 10 palabras en `top1`

Las imágenes se guardan en `PLOTS_DIR` (ver `Config/Config_ETL.py`).

## Notas importantes y troubleshooting
- Si `matplotlib` o `seaborn` no están instalados, las visualizaciones saltarán y verás un mensaje indicando que debes instalarlos.
- Si la ejecución falla al importar `transform_data`, asegúrate de que estás ejecutando `Main.py` desde la raíz del proyecto y que no hay problemas de path.
- Para depurar visualizaciones: carga el CSV manualmente en un REPL y llama `run_visualizations(df)`.

## Contribuir
- Crea una rama a partir de `development` para cambios.
- Haz PR dirigidas a `main` o `development` según el flujo del repo.

## Licencia
- Proyecto de ejemplo — añade la licencia que prefieras.

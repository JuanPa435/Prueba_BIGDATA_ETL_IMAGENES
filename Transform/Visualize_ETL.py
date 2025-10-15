import os
import pandas as pd
import matplotlib.pyplot as plt
from Config.Config_ETL import PLOTS_DIR

def run_visualizations(df):
    """
    Genera 5 gráficas de análisis exploratorio del dataset limpio.
    Todas las imágenes se guardan en Data/plots/
    """
    print("📈 Generando gráficas...")

    # Asegurar que las columnas estén en minúsculas
    df.columns = [c.lower() for c in df.columns]

    # 1️⃣ Distribución general del sentimiento (Label)
    plt.figure(figsize=(6,4))
    df['label'].value_counts().plot(kind='bar', color=['#66bb6a','#ef5350'])
    plt.title("Distribución del Sentimiento (Label)")
    plt.xlabel("Sentimiento (1=Positivo, 0=Negativo)")
    plt.ylabel("Número de registros")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "1_distribucion_label.png"))
    plt.close()

    # 2️⃣ Noticias por año
    df["year"] = df["date"].dt.year
    df.groupby("year").size().plot(kind="bar", figsize=(7,4))
    plt.title("Número de noticias por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de registros")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "2_noticias_por_anio.png"))
    plt.close()

    # 3️⃣ Promedio del sentimiento por año
    df.groupby("year")["label"].mean().plot(kind="line", marker='o', figsize=(7,4))
    plt.title("Promedio del Sentimiento por Año")
    plt.xlabel("Año")
    plt.ylabel("Promedio del Label")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "3_promedio_sentimiento_anual.png"))
    plt.close()

    # 4️⃣ Noticias por mes (global)
    df["month"] = df["date"].dt.month
    df.groupby("month").size().plot(kind="bar", figsize=(7,4))
    plt.title("Distribución de noticias por mes (todas las fechas)")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de noticias")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "4_noticias_por_mes.png"))
    plt.close()

    # 5️⃣ Frecuencia de palabras más comunes en Top1
    # (muy útil para ver los temas más recurrentes)
    from collections import Counter
    import re

    words = []
    for text in df["top1"].dropna():
        text = re.sub(r"[^A-Za-z ]", "", str(text))  # quitar signos
        words.extend(text.lower().split())

    counter = Counter(words)
    common = pd.DataFrame(counter.most_common(10), columns=["Palabra", "Frecuencia"])

    plt.figure(figsize=(8,4))
    plt.bar(common["Palabra"], common["Frecuencia"], color="#42a5f5")
    plt.title("Top 10 palabras más comunes en titulares Top1")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "5_palabras_comunes_top1.png"))
    plt.close()

    print("✅ Gráficas guardadas en la carpeta:", PLOTS_DIR)

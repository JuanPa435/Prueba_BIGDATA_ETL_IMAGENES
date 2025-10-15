import os
import pandas as pd
from Config.Config_ETL import PLOTS_DIR


def run_visualizations(df):
    """
    Genera 5 gráficas básicas y las guarda en `PLOTS_DIR`:
      1) Distribución de Labels (barra)
      2) Número de noticias por año (barra)
      3) Promedio de Label por mes (linea)
      4) Histograma de longitud de 'top1' (longitud en palabras)
      5) Top 10 palabras simples en 'top1' (barra)
    """
    print("📈 Generando gráficas básicas...")

    # importar matplotlib localmente y detectar si está disponible
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print("matplotlib no disponible. Instala matplotlib para generar las gráficas (pip install matplotlib). Se detiene la generación de gráficas.")
        return

    os.makedirs(PLOTS_DIR, exist_ok=True)

    # normalizar columnas
    df.columns = [c.lower() for c in df.columns]

    # parsear fecha
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 1) Distribución de Labels
    plt.figure(figsize=(6,4))
    counts = df['label'].value_counts().sort_index()
    plt.bar(counts.index.astype(str), counts.values, color=['#ef5350', '#66bb6a'])
    plt.title('Distribución del Sentimiento (Label)')
    plt.xlabel('Label (0=Neg, 1=Pos)')
    plt.ylabel('Conteo')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'basic_1_label_distribution.png'))
    plt.close()

    # 2) Número de noticias por año
    df['year'] = df['date'].dt.year
    year_counts = df.groupby('year').size()
    plt.figure(figsize=(7,4))
    plt.bar(year_counts.index.astype(str), year_counts.values, color='#42a5f5')
    plt.title('Número de noticias por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'basic_2_news_by_year.png'))
    plt.close()

    # 3) Promedio de Label por mes (agregado sobre todo el periodo)
    df['month'] = df['date'].dt.month
    month_mean = df.groupby('month')['label'].mean()
    plt.figure(figsize=(8,4))
    plt.plot(month_mean.index, month_mean.values, marker='o', color='#ffa726')
    plt.xticks(range(1,13))
    plt.title('Promedio de Label por mes (todas las fechas)')
    plt.xlabel('Mes')
    plt.ylabel('Promedio Label')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'basic_3_label_mean_by_month.png'))
    plt.close()

    # 4) Histograma de longitud de 'top1' en palabras
    if 'top1' in df.columns:
        lengths = df['top1'].fillna('').astype(str).apply(lambda s: len(s.split()))
        plt.figure(figsize=(8,4))
        plt.hist(lengths, bins=20, color='#66bb6a')
        plt.title("Histograma: longitud (palabras) de 'top1'")
        plt.xlabel('Número de palabras')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'basic_4_top1_length_hist.png'))
        plt.close()

        # 5) Top 10 palabras simples en top1
        from collections import Counter
        import re

        words = []
        for t in df['top1'].dropna().astype(str):
            clean = re.sub(r"[^A-Za-z ]", ' ', t).lower()
            words.extend([w for w in clean.split() if len(w) > 2])

        counter = Counter(words)
        common = counter.most_common(10)
        if common:
            words, freqs = zip(*common)
            plt.figure(figsize=(8,4))
            plt.bar(words, freqs, color='#42a5f5')
            plt.title("Top 10 palabras en 'top1'")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(os.path.join(PLOTS_DIR, 'basic_5_top10_words_top1.png'))
            plt.close()

    print('✅ Gráficas básicas guardadas en:', PLOTS_DIR)

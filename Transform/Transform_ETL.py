import pandas as pd

def transform_data(df):
    """
    Limpieza sencilla y adaptada al dataset de sentimiento del DJIA.
    """
    df = df.copy()

    # Normalizar nombres de columnas
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Convertir columna de fecha
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Eliminar filas sin fecha
    df.dropna(subset=["date"], inplace=True)

    # Rellenar nulos en titulares
    for col in df.columns:
        if col.startswith("top"):
            df[col] = df[col].fillna("")

    # Eliminar duplicados (por seguridad)
    df.drop_duplicates(inplace=True)

    print(f"✅ Limpieza completada: {len(df)} filas finales")
    return df

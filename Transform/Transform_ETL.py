import pandas as pd
import re
import os
from Config.Config_ETL import RAW_FILE, CLEAN_FILE

def replace_commas_in_quotes(file_path, output_path):

    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    # Expresión regular: busca cualquier texto entre comillas dobles que contenga comas
    fixed_data = re.sub(
        r'"([^"]*?,[^"]*?)"',
        lambda m: '"' + m.group(1).replace(',', '.') + '"',
        data
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(fixed_data)

    print(f"✅ Comas dentro de comillas reemplazadas por puntos → {output_path}")


def clean_dataset(input_path, output_path):

    # Cargar CSV corregido
    df = pd.read_csv(input_path, encoding='utf-8')

    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # Eliminar filas completamente vacías
    df.dropna(how='all', inplace=True)

    # Reemplazar espacios y normalizar nombres de columnas
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # Intentar convertir columnas numéricas con decimales tipo texto ("1.25")
    for col in df.columns:
        try:
            df[col] = df[col].astype(str).str.replace(',', '.')
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except Exception:
            pass

    # Guardar dataset limpio
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ Dataset limpio guardado en: {output_path}")

    return df


def run_transform():

    # 1️⃣ Reemplazar comas dentro de comillas por puntos
    replace_commas_in_quotes(RAW_FILE, CLEAN_FILE)

    # 2️⃣ Limpiar dataset corregido
    df_clean = clean_dataset(CLEAN_FILE, CLEAN_FILE)

    return df_clean


def transform_data(df, save=True):
    """
    Limpia un DataFrame en memoria y devuelve el DataFrame limpio.
    Si save=True, lo guarda en la ruta CLEAN_FILE definida en Config_ETL.
    Esta función permite que el pipeline en memoria (extract -> transform -> load)
    funcione sin depender de archivos temporales.
    """
    # Trabajar sobre copia
    df_clean = df.copy()

    # Eliminar duplicados y filas vacías
    df_clean.drop_duplicates(inplace=True)
    df_clean.dropna(how='all', inplace=True)

    # Normalizar nombres de columnas
    df_clean.columns = [col.strip().replace(" ", "_").lower() for col in df_clean.columns]

    # Intentar convertir columnas numéricas representadas con coma decimal
    for col in df_clean.columns:
        try:
            df_clean[col] = df_clean[col].astype(str).str.replace(',', '.')
            df_clean[col] = pd.to_numeric(df_clean[col], errors='ignore')
        except Exception:
            pass

    # Guardar si corresponde
    if save:
        try:
            df_clean.to_csv(CLEAN_FILE, index=False, encoding='utf-8')
            print(f"✅ Dataset limpio guardado en: {CLEAN_FILE}")
        except Exception as e:
            print(f"Advertencia: no se pudo guardar CLEAN_FILE: {e}")

    return df_clean


# Permite ejecución independiente del módulo
if __name__ == "__main__":
    run_transform()

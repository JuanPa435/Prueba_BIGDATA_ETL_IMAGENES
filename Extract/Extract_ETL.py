import pandas as pd
import chardet
from Config.Config_ETL import RAW_FILE

def extract_data():
    """Lee el CSV detectando codificación automáticamente"""
    with open(RAW_FILE, 'rb') as f:
        result = chardet.detect(f.read(10000))
    encoding = result['encoding'] or 'utf-8'

    print(f"[EXTRACT] Codificación detectada: {encoding}")
    df = pd.read_csv(RAW_FILE, encoding=encoding)
    print(f"[EXTRACT] Datos leídos correctamente: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df

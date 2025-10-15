import sqlite3
from Config.Config_ETL import CLEAN_FILE, SQLITE_DB


def load_to_csv(df):
    """Guarda el dataset limpio en CSV dentro de la carpeta Data"""
    df.to_csv(CLEAN_FILE, index=False)
    print(f"[LOAD] Archivo limpio guardado en: {CLEAN_FILE}")

def load_to_sqlite(df):
    """Guarda el dataset limpio en una base SQLite dentro de la carpeta Data"""
    conn = sqlite3.connect(SQLITE_DB)
    df.to_sql('cleaned_stock_senti', conn, if_exists='replace', index=False)
    conn.close()
    print(f"[LOAD] Datos cargados en base SQLite: {SQLITE_DB}")

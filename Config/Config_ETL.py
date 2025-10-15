import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta principal donde estarán los datos
DATA_DIR = os.path.join(BASE_DIR, "Data")

# Crear carpeta si no existe
os.makedirs(DATA_DIR, exist_ok=True)

# Archivos principales
RAW_FILE = os.path.join(DATA_DIR, "stock_senti_analysis.csv")           
CLEAN_FILE = os.path.join(DATA_DIR, "cleaned_stock_senti.csv")         
SQLITE_DB = os.path.join(DATA_DIR, "cleaned_stock_senti.sqlite")        
PLOTS_DIR = os.path.join(DATA_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DBNAME = os.getenv("DBNAME")

ENV = os.getenv("ENV", "development")

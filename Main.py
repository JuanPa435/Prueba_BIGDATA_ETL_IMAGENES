from Extract.Extract_ETL import extract_data
from Transform.Transform_ETL import transform_data
from Load.Load_ETL import load_to_csv, load_to_sqlite
from Transform.Visualize_ETL import run_visualizations

def main():
    print("===== INICIO DEL ETL =====")

    # ETL
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_to_csv(df_clean)
    load_to_sqlite(df_clean)

    # EDA
    run_visualizations(df_clean)

    print("=====COMPLETADO CON ÉXITO =====")

if __name__ == "__main__":
    main()

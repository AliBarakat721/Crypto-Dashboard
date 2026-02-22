import pandas as pd
from sqlalchemy import create_engine

def load_to_postgresql(df: pd.DataFrame, table_name="crypto_data"):
    """
    Load a DataFrame to PostgreSQL table
    """
    if df is None or df.empty:
        raise ValueError("DataFrame is empty")

    # 1️⃣ إعداد الاتصال
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/crypto_pipeline")
    # 2️⃣ رفع البيانات للجدول
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data loaded successfully into table '{table_name}' ✅")

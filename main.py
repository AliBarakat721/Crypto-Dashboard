from src.extract import fetch_crypto_data
from src.transfrom import transform_crypto_data
from src.load import load_to_postgresql  # 👈 استيراد الدالة

def main():
    raw_df = fetch_crypto_data(per_page=250)
    clean_df = transform_crypto_data(raw_df)

    print("Transformed Data ✅")
    print(clean_df.head())
    print("\nColumns:\n", clean_df.columns)

    # 🔥 رفع البيانات على PostgreSQL
    load_to_postgresql(clean_df)

if __name__ == "__main__":
    main()
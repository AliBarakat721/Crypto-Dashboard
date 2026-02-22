import pandas as pd

def transform_crypto_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform crypto data for dashboard & database storage
    """

    # 1️⃣ التأكد إن البيانات موجودة
    if df is None or df.empty:
        raise ValueError("Input DataFrame is empty")

    # 2️⃣ اختيار الأعمدة المهمة فقط
    selected_columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h",
        "extracted_at"
    ]
    df = df[selected_columns].copy()

    # 3️⃣ تحويل الأعمدة الرقمية لـ float
    numeric_columns = [
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]
    df[numeric_columns] = df[numeric_columns].astype(float)

    # 4️⃣ حذف الصفوف اللي فيها Missing Values في السعر
    df.dropna(subset=["current_price"], inplace=True)

    # 5️⃣ ترتيب الأعمدة بشكل منطقي (مش ضروري إعادة تسمية)
    df = df[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h",
            "extracted_at"
        ]
    ]

    # 6️⃣ إرجاع الـ DataFrame النهائي
    return df
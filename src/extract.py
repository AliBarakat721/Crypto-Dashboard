import requests
import pandas as pd
from datetime import datetime , timezone


def fetch_crypto_data(vs_currency="usd", per_page=250, page=1):
    """
    Fetch cryptocurrency market data from CoinGecko API
    """

    url = "https://api.coingecko.com/api/v3/coins/markets"


    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": False
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # لو فيه Error يطلع Exception

        data = response.json()

        # تحويل البيانات لـ DataFrame
        df = pd.DataFrame(data)

        # إضافة وقت الاستخراج (مهم جدًا في الـ Data Engineering)
        df["extracted_at"] = datetime.now(timezone.utc)

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == "__main__":
    df = fetch_crypto_data()

    if df is not None:
        print("Data extracted successfully ✅")
        print(df.head())
        print("\nColumns:\n", df.columns)
        print('\nShape : ', df.shape)
    else:
        print("Extraction failed ❌")
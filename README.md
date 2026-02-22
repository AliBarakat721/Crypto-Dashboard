# 🚀 Crypto Dashboard

A professional **Crypto Dashboard** that visualizes cryptocurrency data using **PostgreSQL**, **Pandas**, **SQLAlchemy**, **Streamlit**, and **Plotly**. The project follows an **ETL (Extract → Transform → Load)** pipeline to fetch, process, and store cryptocurrency data before visualizing it in an interactive dashboard.

---

## 📦 Project Structure


- Crypto-Dashboard/
- ├── main.py # ETL script: fetch, transform & load crypto data into PostgreSQL
- ├── dashboard.py # Streamlit dashboard: interactive visualizations
- ├── requirements.txt # Python dependencies
- ├── .gitignore # Ignore sensitive files, databases, and cache
- └── README.md # Project documentation


---

## ⚙️ Features

- Fetches and transforms cryptocurrency data (price, market cap, volume, 24h change)
- Loads data into **PostgreSQL** for persistent storage
- Interactive **Streamlit dashboard** with:
  - Real-time price, market cap, and volume charts
  - Top cryptocurrencies by market cap
  - 24h price change comparison
  - Selectable coins via dropdown menu
  - Beautiful **Plotly visualizations** with hover info
- Fully configurable and modular ETL and dashboard

---

## 🛠 Requirements

- Python ≥ 3.10  
- PostgreSQL (local or remote)
- Python packages:

```txt
pandas
sqlalchemy
psycopg2-binary
streamlit
plotly

Install dependencies:

pip install -r requirements.txt
📝 Setup Instructions

Clone the repository:

git clone https://github.com/username/Crypto-Dashboard.git
cd Crypto-Dashboard

Create PostgreSQL database (example):

CREATE DATABASE crypto_pipeline;

Run the ETL script to populate your database:

python main.py

Launch the Streamlit dashboard:

python -m streamlit run dashboard.py

Open your browser and enjoy the interactive dashboard.

🔧 Customization

Change the database connection in main.py and dashboard.py:

DB_USER = "postgres"
DB_PASS = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_pipeline"

Add new cryptocurrencies by modifying the ETL source

Customize charts, layout, and themes directly in dashboard.py


📂 Notes

Do not upload database files to GitHub. The repository only contains scripts and instructions to populate your own database.

The ETL pipeline is modular, so you can extend it to include more metrics, APIs, or coins.

📖 License

MIT License © 2026

Made with ❤️ by [ِAli Barakat]
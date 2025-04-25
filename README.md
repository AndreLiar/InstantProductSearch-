

```markdown
# 🛒 Instant Product Search – Flask + HTMX

This project is a simple e-commerce product search interface using **Flask**, **HTMX**, and **SQLite**. It allows real-time, client-friendly search of product data rendered in a dynamic HTML table using HTMX.

---

## 🚀 Features

- 🔎 Instant search powered by HTMX (no JS required)
- 📦 SQLite database of products (name, quantity, rate, supplier, origin)
- 💾 Flask-Migrate for DB schema handling
- 📁 Clean project structure for easy extensibility

---

## 🧰 Tech Stack

- Python 3.11 (via Conda)
- Flask 3
- Flask-SQLAlchemy
- Flask-Migrate
- HTMX 1.9 (via CDN)

---

## 📂 Project Structure

```
flask_htmx_search/
│
├── app.py
├── models.py
├── extensions.py
├── requirements.txt
├── migrations/
├── templates/
│   ├── index.html
│   └── search_results.html
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone and activate Conda environment

```bash
git clone https://github.com/AndreLiar/InstantProductSearch-.git
cd flask_htmx_search
conda create -n flask_htmx python=3.11
conda activate flask_htmx
pip install -r requirements.txt
```

### 2. Initialize the database

```bash
flask db init
flask db migrate -m "Create product table"
flask db upgrade
```

### 3. Seed the database

```bash
flask seed
```

### 4. Run the server

```bash
export FLASK_APP=app.py
flask run
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ✨ Example Search UI

You can search for products instantly using the input field:

- Type `"Laptop"`, `"China"`, or `"GadgetHub"` to see dynamic filtering
- Results update live using `hx-get="/search"`

---

## 📌 Notes

- This project uses HTMX for real-time partial rendering – no JavaScript required!
- All models use UUID for unique product IDs

---

## ✅ Example Products Seeded

| Product Name    | Quantity | Rate (€) | Supplier    | Origin      |
|----------------|----------|----------|-------------|-------------|
| Laptop         | 10       | 999.99   | TechStore   | USA         |
| Smartphone     | 25       | 499.49   | GadgetHub   | South Korea |
| Coffee Machine | 5        | 149.95   | HomePlus    | Italy       |
| Desk Lamp      | 30       | 19.99    | OfficeDepot | China       |
| Gaming Chair   | 8        | 299.90   | FurniMax    | Germany     |

---


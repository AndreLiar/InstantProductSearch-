from flask import Flask, render_template, request
from extensions import db, migrate
from models import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///search.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = Product.query.filter(Product.name.ilike(f"%{q}%")).all()
    return render_template("search_results.html", results=results)

@app.cli.command("seed")
def seed():
    sample_products = [
        Product(name="Laptop", quantity=10, rate=999.99, supplier="TechStore", origin="USA"),
        Product(name="Smartphone", quantity=25, rate=499.49, supplier="GadgetHub", origin="South Korea"),
        Product(name="Coffee Machine", quantity=5, rate=149.95, supplier="HomePlus", origin="Italy"),
        Product(name="Desk Lamp", quantity=30, rate=19.99, supplier="OfficeDepot", origin="China"),
        Product(name="Gaming Chair", quantity=8, rate=299.90, supplier="FurniMax", origin="Germany"),
    ]
    db.session.bulk_save_objects(sample_products)
    db.session.commit()
    print("Seeded product database.")

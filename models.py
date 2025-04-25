import uuid
from extensions import db

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    supplier = db.Column(db.String(120), nullable=False)
    origin = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

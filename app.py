from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# @app.route("/photos.json")
# def photos_index():
#     return db.photos_all()

@app.route("/products.json")
def products_index():
    return db.products_all()

@app.route("/products.json", methods=["POST"])
def create():
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    return db.products_create(name, category, price)

@app.route("/products/<id>.json")
def show(id):
    return db.products_find_by_id(id)

@app.route("/products/<id>.json", methods=["PATCH"])
def update(id):
    if request.form.get("name") is not None:
        name = request.form.get("name")
    if request.form.get("category") is not None:
        category = request.form.get("category")
    if request.form.get("price") is not None:
        price = request.form.get("price")
    return db.products_update_by_id(id, name, category, price)

# @app.route("/products/<id>.json", methods=["PATCH"])
# def update(id):
#     # Get data from JSON request body
#     data = request.json or {}

#     # Retrieve each field from the data if it exists
#     name = data.get("name")
#     category = data.get("category")
#     price = data.get("price")

#     # Call the update function with optional params
#     return db.products_update_by_id(id, name=name, category=category, price=price)
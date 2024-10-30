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
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
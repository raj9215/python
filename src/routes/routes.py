
from src.controller.controller import add_product, get_products, update_product, delete_product
from flask import Flask, request, jsonify
from src.config.database import app

@app.route('/add_product', methods=['POST'] )
def add_product_route():
    result = add_product()
    return result

# READ - Get all products
@app.route('/products', methods=['GET'])
def get_products_route():
    return get_products()

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.json
    name = data.get('name')
    type = data.get('type')
    author_name = data.get('author_name')
    status = data.get('status')
    return update_product(product_id, name, type, author_name, status)

# DELETE - Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return delete_product(product_id)

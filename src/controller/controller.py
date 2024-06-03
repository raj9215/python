from src.config.database import mycursor, mydb
from flask import Flask, request, jsonify

def add_product():
    # Get product data from the request
    name = request.form.get('name')
    type = request.form.get('type')
    author_name = request.form.get('author_name')
    status = request.form.get('status')

    # Insert the product into the database
    sql = "INSERT INTO products (name, type, author_name, status) VALUES (%s, %s, %s, %s)"
    values = (name, type, author_name, status)
    mycursor.execute(sql, values)
    mydb.commit()

    return jsonify({'message': 'Product added successfully'})

def get_products():
    mycursor.execute("SELECT * FROM products")
    products = mycursor.fetchall()
    print(products)
    product_list = []
    for product in products:
        product_dict = {
            "product_id": product[0],
            "name": product[1],
            "type": product[2],
            "author_name": product[2],
            "status": product[4],     
        }
        product_list.append(product_dict)
    return jsonify({'products': product_list})

# UPDATE - Update a product
def update_product(product_id, name, type, author_name, status):
    sql = "UPDATE products SET name = %s, type = %s, author_name = %s, status = %s WHERE id = %s"
    values = (name, type, author_name, status, product_id)
    mycursor.execute(sql, values)
    mydb.commit()
    return jsonify({'message': 'Product updated successfully'})

# DELETE - Delete a product
def delete_product(product_id):
    sql = "DELETE FROM products WHERE id = %s"
    value = (product_id,)
    mycursor.execute(sql, value)
    mydb.commit()
    return jsonify({'message': 'Product deleted successfully'})

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données JSON
def read_json():
    with open('products.json') as f:
        return json.load(f)

# Fonction pour lire les données CSV
def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Fonction pour lire les données SQLite
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            error = "Wrong source"
    except Exception as e:
        error = f"Error loading data: {str(e)}"

    if product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if item['id'] == product_id]
            if not data:
                error = "Product not found"
        except:
            error = "Invalid product ID"

    return render_template('product_display.html', products=data, error=error)

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to load JSON data
def load_json(filename):
    with open(filename) as f:
        return json.load(f)

# Function to load CSV data
def load_csv(filename):
    products = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            products = load_json('products.json')
        except Exception as e:
            error = "Failed to read JSON data."
    elif source == 'csv':
        try:
            products = load_csv('products.csv')
        except Exception as e:
            error = "Failed to read CSV data."
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if product_id and not error:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin/python3
"""
Flask app that serves product data from JSON, CSV, or SQLite database.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_from_json():
    """Load product data from a JSON file"""
    with open("products.json", encoding="utf-8") as f:
        return json.load(f)

def load_from_csv():
    """Load product data from a CSV file"""
    with open("products.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def load_from_sql():
    """Load product data from the SQLite database"""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except sqlite3.Error as e:
        raise Exception("Database error: " + str(e))

@app.route('/')
def index():
    """Main route that displays products based on source parameter"""
    source = request.args.get("source", "json")
    try:
        if source == "json":
            products = load_from_json()
        elif source == "csv":
            products = load_from_csv()
        elif source == "sql":
            products = load_from_sql()
        else:
            return render_template("product_display.html", error="Wrong source")
    except Exception as e:
        return render_template("product_display.html", error=str(e))

    return render_template("product_display.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)

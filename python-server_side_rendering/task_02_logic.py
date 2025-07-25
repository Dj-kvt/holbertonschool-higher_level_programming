#!/usr/bin/python3
"""Flask app that dynamically renders a list of items from a JSON file"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    items_list = []
    json_file = os.path.join(os.path.dirname(__file__), 'items.json')

    # Load items from JSON file
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading items.json: {e}")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

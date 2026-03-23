from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# =========================
# Utility functions
# =========================
def read_items_file():
    """Read items from items.json and return a list."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_json_products():
    """Read products from products.json and return a list of dictionaries."""
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    """Read products from products.csv and return a list of dictionaries."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return []


# =========================
# Routes
# =========================
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
    items_list = read_items_file()
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Check source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Read products from correct source
    if source == 'json':
        products_list = read_json_products()
    else:
        products_list = read_csv_products()

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        filtered_products = [product for product in products_list if product['id'] == product_id]

        if not filtered_products:
            return render_template('product_display.html', error="Product not found")

        return render_template('product_display.html', products=filtered_products)

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

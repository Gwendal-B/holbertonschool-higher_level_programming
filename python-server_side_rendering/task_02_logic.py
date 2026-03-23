from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    try:
        # Ouvre le fichier JSON
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except FileNotFoundError:
        # Si le fichier n'existe pas, on met une liste vide
        items_list = []

    # Passe la liste à la template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

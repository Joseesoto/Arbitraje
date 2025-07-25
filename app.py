from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/precios')
def precios_binance():
    url = 'https://api.binance.com/api/v3/ticker/price'
    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

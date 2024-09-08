import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MONGO_URL = os.getenv("MONGO_URL", "MONGO_URL")


# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type"]}})

# Establish the MongoDB client
client = MongoClient(MONGO_URL)
db = client['_stocks']  # Use 'stocks_db' database
stocks_collection = db['stock-details']  # 'stocks' collection

# Helper function to format stock data for JSON response
def format_stock(stock):
    return {
        'id': str(stock['_id']),
        'name': stock['name'],
        'price': stock['price']
    }

# GET - Fetch all stocks
@app.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = stocks_collection.find()
    return jsonify([format_stock(stock) for stock in stocks])

@app.route('/', methods=['GET'])
def konichiwa():
    return jsonify({'message': 'Welcome to Stocks API!'})

# POST - Add a new stock
@app.route('/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    new_stock = {
        'name': data['name'],
        'price': data['price']
    }
    stocks_collection.insert_one(new_stock)
    return jsonify({'message': 'Stock added successfully!'}), 201

# PUT - Update an existing stock
@app.route('/stocks/<id>', methods=['PUT'])
def update_stock(id):
    data = request.get_json()
    updated_stock = {
        'name': data['name'],
        'price': data['price']
    }
    result = stocks_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_stock})
    
    if result.modified_count == 0:
        return jsonify({'message': 'Stock not found or no changes made.'}), 404

    return jsonify({'message': 'Stock updated successfully!'})

# DELETE - Delete a stock
@app.route('/stocks/<id>', methods=['DELETE'])
def delete_stock(id):
    stock = stocks_collection.find_one({"_id": ObjectId(id)})
    if stock:
        stocks_collection.delete_one({"_id": ObjectId(id)})
        return jsonify({"message": "Stock deleted successfully"}), 200
    else:
        return jsonify({"error": "Stock not found"}), 404


if __name__ == "__main__":
    # Get the port from environment variables or use 5000 as the default
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
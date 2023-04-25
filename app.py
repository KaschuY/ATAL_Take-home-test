from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['locations']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def save_locations():
    # Get the JSON data from the request body
    data = request.get_json()

    # Save the data to the MongoDB collection
    collection.insert_one(data)

    # Return a success message to the client
    return {'message': 'Locations saved to MongoDB!'}
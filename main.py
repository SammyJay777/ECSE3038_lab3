from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://User620119624:Student_620119624@cluster-620119624.gb5bm.mongodb.net/Monday?retryWrites=true&w=majority"
mongo = PyMongo(app)

if __name__ == "__main__":
  app.run(debug=True)
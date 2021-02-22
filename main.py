from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo
from marshmallow import Schema, fields, ValidationError
from bson.json_util import dumps
from json import loads

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://User620119624:Student_620119624@cluster-620119624.gb5bm.mongodb.net/Tank?retryWrites=true&w=majority"
mongo = PyMongo(app)

class TankSchema(Schema):
  location = fields.String(required=True)
  lat = fields.String(required=True)
  long = fields.String(required=True)
  percentage_full = fields.Integer(required=True)

@app.route("/tank")
def get_tanks():
  Tank01 = mongo.db.Tank01.find()
  return jsonify(loads(dumps(Tank01)))

@app.route("/tank", methods=["POST"])
def add_tank():
  try:
    newTank = TankSchema().load(request.json)
    tank_id = mongo.db.Tank01.insert_one(newTank).inserted_id
    retTank = mongo.db.Tank01.find_one(tank_id)
    return loads(dumps(retTank))
  except ValidationError as ve:
    return ve.messages, 400

@app.route("/tank/<ObjectId:id>", methods=["PATCH"])
def update_tank(id):
  mongo.db.Tank01.update_one({"_id": id},{ "$set": request.json})

  tank = mongo.db.Tank01.find_one(id)

  return loads(dumps(tank))

@app.route("/tank/<ObjectId:id>", methods=["DELETE"])
def delete_tank(id):
  result = mongo.db.Tank01.delete_one({"_id": id})

  if result.deleted_count == 1:
    return {
      "success": True
    }
  else:
    return {
      "success": False
    }, 400

if __name__ == "__main__":
  app.run(debug=True)

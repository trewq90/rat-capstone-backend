from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://flesidptqgxfyd:2237d9ae9c3a8430f0a3cceea9ca1d4f0445dc2e001ac56ef576469713fda3ec@ec2-174-129-254-238.compute-1.amazonaws.com:5432/d4ecgq6o7d8d1m"

heroku = Heroku(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    

    def __init__(self, item, value):
        self.item = item
        self.value = value
@app.route("/item/create", methods=["POST"])
def create_user():
    if request.content_type == "application/json":
        post_data = request.get_json()
        item = post_data.get("item")
        value = post_data.get("value")

        record = User(item, value)

        db.session.add(record)
        db.session.commit()

        return jsonify("Item Created.")

    return jsonify("Error: request must be sent as JSON")

@app.route("/item/get", methods=["GET"])
def get_all_users():
    all_items = db.session.query(User.id, User.item, User.value).all()
    return jsonify(result)

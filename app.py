from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://flesidptqgxfyd:2237d9ae9c3a8430f0a3cceea9ca1d4f0445dc2e001ac56ef576469713fda3ec@ec2-174-129-254-238.compute-1.amazonaws.com:5432/d4ecgq6o7d8d1m"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
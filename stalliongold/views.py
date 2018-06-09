from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from stalliongold import app

app.config['MONGO_DBNAME'] = 'stalliongold'
app.config['MONGO_URI'] = 'mongodb://<stalliongoldadmin>:<icantputithere>@ds237660.mlab.com:37660/stalliongold'

#mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login')
def login():
    return 'Logged in'


@app.route('/signup')
def signup():
    return 'signed up'


@app.route('/admin')
def admin():
    return 'admin dashboard'


@app.route('/investor')
def investor():
    return 'Welcome investor'



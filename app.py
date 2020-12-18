#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__) # Initalize flask 

#mongo
app.config["MONGO_URI"] = "mongodb://192.168.56.223:27017/temperature" # Configure mongo url
mongo = PyMongo(app) # initialize pymongo with mongo url

# functions will run based on which route is called (function below route declaration runs)
@app.route('/') # allow base route
@app.route('/index/')
def index():
    return render_template('index.html')
@app.route("/get_one_temp_api") # get one temperature reading
def temp1():
    one_temp = mongo.db.temperature.find_one()
    #print(temp_reading)
    return str(one_temp)

@app.route("/get_ten_temps_api")
def temp10(): # query db to get temperature readings
    temps = ""
    ten_temps = mongo.db.temperature.find().limit(10)
    for temp in ten_temps:
        temps=temps+str(temp)
        print(temps)
    return temps 

@app.route("/recent_temps")
def recent():
    temps = mongo.db.temperature.find().limit(10)
    
    return render_template('temps.html',temps=temps) # Render template with temps list as variable

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyonepy
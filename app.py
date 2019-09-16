from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import JTscrap_mars

#create an instance of Flask App
app = Flask(__name__)

#Use flask_pymongo to set up mongo connections
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#set the route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#scrape
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = JTscrap_mars.scrape()
    mars.update({}, mars_data,upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)
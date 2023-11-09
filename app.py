from flask import Flask, render_template,request
import pymysql
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Adventure")
def Adventure():
    return render_template("Adventure.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Destination")
def Destination():
    return render_template("Destination.html")

@app.route("/usa")
def usa():
    return render_template("usa.html")

@app.route("/uk")
def uk():
    return render_template("uk.html")

@app.route("/canada")
def canada():
    return render_template("canada.html")

@app.route("/chile")
def chile():
    return render_template("chile.html")

@app.route("/cuba")
def cuba():
    return render_template("cuba.html")

@app.route("/Denmark")
def Denmark():
    return render_template("Denmark.html")

@app.route("/Greenland")
def Greenland():
    return render_template("Greenland.html")

@app.route("/Mexico")
def Mexico():
    return render_template("Mexico.html")

if __name__ == '__main__':
    app.run(debug=True)

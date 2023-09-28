from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/home")
def home_html():
    artists = ["Lil Nas X", "Fetty Wap", "Kali Uchis", "Dhruv", "Takayan"]
    return render_template("home.html", red = True , artists = artists )

@app.route("/Favorite_5")
def favorite_5(): 
    return render_template("index.html")


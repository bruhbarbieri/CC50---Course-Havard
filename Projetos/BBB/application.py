import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///bbb.db")

SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html", sports=SPORTS)

@app.route("/login", methods=["GET", "POST"])
def login():
   if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
   return render_template("login.html")

@app.route("/logout")
def logout():
   session["name"] = None
   return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid SportS")

    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)



import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///bbb.db")

EDICOES = ["Todas", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

@app.route("/")
def index():
    return render_template("index.html", edicoes=EDICOES)

@app.route("/search", methods=["GET"])
def search():
    #nome = request.args.get("nome")
    #if not nome:
    #    return render_template("error.html", message="Missing name")
    edicao = request.args.get("edicao")
    nome = request.args.get("nome")
    if not edicao:
        return render_template("error.html", message="Missing editions")
    if edicao not in EDICOES:
        return render_template("error.html", message="Invalid Editions")
    if edicao == "Todas":
        if not nome:
            participantes = db.execute("SELECT * FROM participantes")
            return render_template("participantes.html", participantes=participantes)

        participantes = db.execute("SELECT * FROM participantes WHERE nome LIKE ?", "%" + nome + "%")
        return render_template("participantes.html", participantes=participantes)


    participantes = db.execute("SELECT * FROM participantes WHERE edicoes_id = ?", edicao)
    return render_template("participantes.html", participantes=participantes)

#@app.route("/participantes", methods=["GET", "POST"])
#def participantes(edicao):
#    edicao = edicao
#    participantes = db.execute("SELECT * FROM participantes WHERE edicoes_id = ?", edicao)
#    return render_template("participantes.html", participantes=participantes)



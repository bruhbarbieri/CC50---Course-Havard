import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///bbb.db")

EDICOES = db.execute("SELECT edicoes_id FROM participantes GROUP BY edicoes_id")

SEXOS = db.execute("SELECT sexo FROM participantes GROUP BY sexo")

COLOCACOES = db.execute("SELECT colocacao FROM participantes GROUP BY colocacao")

ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RR", "RO", "RJ", "RN", "RS", "SC", "SP", "SE", "TO", "EXTERIOR"]

SIGNOS = db.execute("SELECT signo FROM participantes GROUP BY signo")

@app.route("/", methods=["GET", "POST"])
def index():
    #participantes=request.args.get("participantes")
    return render_template("index.html")

@app.route("/searchparticipantes", methods=["GET", "POST"])
def searchparticipantes():
        return render_template("participantesearch.html", edicoes=EDICOES, sexos=SEXOS, colocacoes=COLOCACOES, estados=ESTADOS, signos=SIGNOS)

@app.route("/search", methods=["GET", "POST"])
def search():
    edicao = request.args.get("edicao")
    nome = request.args.get("nome")
    sexo = request.args.get("sexo")
    profissao = request.args.get("profissao")
    cidade = request.args.get("cidade")
    colocacao = request.args.get("colocacao")
    estado = request.args.get("estado")
    signo = request.args.get("signo")

    participantes = db.execute("SELECT * FROM participantes WHERE edicoes_id LIKE ? AND nome LIKE ? AND sexo LIKE ? AND profissao LIKE ? AND cidade LIKE ? AND colocacao LIKE ? AND estado LIKE ? AND signo LIKE ?", edicao, "%" + nome + "%", sexo, "%" + profissao + "%", "%" + cidade + "%", colocacao, estado, signo)
    return render_template("participantes.html", participantes=participantes)




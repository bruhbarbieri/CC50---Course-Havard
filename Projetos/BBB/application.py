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

EDICOES2 = db.execute("SELECT edicao FROM edicoes GROUP BY edicao")

ANOS = db.execute("SELECT ano FROM edicoes GROUP BY ano")

APRESENTADORES = db.execute("SELECT apresentador FROM edicoes GROUP BY apresentador")

NUMEROS = db.execute("SELECT numero FROM paredoes GROUP BY numero ORDER BY numero")

RESULTADOS = db.execute("SELECT resultado FROM paredoes_participantes GROUP BY resultado")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/searchparticipantes", methods=["GET", "POST"])
def searchparticipantes():
        return render_template("participantesearch.html", edicoes=EDICOES, sexos=SEXOS, colocacoes=COLOCACOES, estados=ESTADOS, signos=SIGNOS)

@app.route("/searchedicoes", methods=["GET", "POST"])
def searchedicoes():
        return render_template("edicoessearch.html", edicoes=EDICOES2, anos=ANOS, apresentadores=APRESENTADORES)

@app.route("/searchparedoes", methods=["GET", "POST"])
def searchparedoes():
        return render_template("paredoessearch.html", edicoes=EDICOES2, numeros=NUMEROS, resultados=RESULTADOS)

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

    participantess = db.execute("SELECT COUNT(nome) FROM participantes WHERE edicoes_id LIKE ? AND nome LIKE ? AND sexo LIKE ? AND profissao LIKE ? AND cidade LIKE ? AND colocacao LIKE ? AND estado LIKE ? AND signo LIKE ?", edicao, "%" + nome + "%", sexo, "%" + profissao + "%", "%" + cidade + "%", colocacao, estado, signo)

    contagem1 = participantess[0]

    contagemparticipante = list(contagem1.values())[0]

    return render_template("participantes.html", participantes=participantes, participantess=participantess, contagemparticipante=contagemparticipante)


@app.route("/search2", methods=["GET", "POST"])
def search2():
    edicao = request.args.get("edicao")
    ano = request.args.get("ano")
    apresentador = request.args.get("apresentador")
    vencedor = request.args.get("vencedor")

    edicoess = db.execute("SELECT * FROM edicoes WHERE edicao LIKE ? AND ano LIKE ? AND apresentador LIKE ? AND vencedor LIKE ?", edicao, ano, apresentador, "%" + vencedor + "%")
    return render_template("edicoes.html", edicoess=edicoess)

@app.route("/search3", methods=["GET", "POST"])
def search3():
    edicao = request.args.get("edicao")
    numero = request.args.get("numero")
    nome = request.args.get("nome")
    resultado = request.args.get("resultado")

    paredoes = db.execute('''SELECT numero, nome, porcentagem, metodoindicacao, resultado FROM participantes
                            JOIN paredoes_participantes ON participantes.id = paredoes_participantes.participantes_id
                            JOIN paredoes ON paredoes_participantes.paredoes_id = paredoes.id
                            JOIN edicoes ON paredoes.edicoes_id = edicoes.id
                            WHERE edicao LIKE ? AND numero LIKE ? AND nome LIKE ? AND resultado LIKE ?''', edicao, numero, "%" + nome + "%", resultado)

    paredoess = db.execute('''SELECT edicao, numero, quantidadevotos, dataparedao, paredoes_id FROM participantes
                            JOIN paredoes_participantes ON participantes.id = paredoes_participantes.participantes_id
                            JOIN paredoes ON paredoes_participantes.paredoes_id = paredoes.id
                            JOIN edicoes ON paredoes.edicoes_id = edicoes.id
                            WHERE edicao LIKE ? AND numero LIKE ? AND nome LIKE ? AND resultado LIKE ? GROUP BY dataparedao ORDER BY paredoes_id''', edicao, numero, "%" + nome + "%", resultado)

    paredoesss = db.execute('''SELECT COUNT(dataparedao) FROM paredoes WHERE id IN (SELECT paredoes_id FROM paredoes_participantes
                            JOIN participantes ON paredoes_participantes.participantes_id = participantes.id
                            JOIN paredoes ON paredoes_participantes.paredoes_id = paredoes.id
                            JOIN edicoes ON paredoes.edicoes_id = edicoes.id
                            WHERE edicao LIKE ? AND numero LIKE ? AND nome LIKE ? AND resultado LIKE ? GROUP BY dataparedao)''', edicao, numero, "%" + nome + "%", resultado)

    contagem = paredoesss[0]

    contagemparedao = list(contagem.values())[0]

    return render_template("paredoes.html", paredoes=paredoes, paredoess=paredoess, paredoesss=paredoesss, contagemparedao=contagemparedao)






import csv
from cs50 import get_string

filmes = {}

def f(filme):
    return filmes[filme]

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    #search = get_string("Search: ")
    for row in reader:
        filme = row["Filme"].strip().upper()
        if filme not in filmes:
            filmes[filme] = 0
        filmes[filme] += 1

for filme in sorted(filmes, key=f, reverse=True):
   print(filme, filmes[filme])

import csv
from cs50 import get_string

filmes = set()

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    #search = get_string("Search: ")
    for row in reader:
        filmes.add(row["Filme"].strip().upper())

for filme in sorted(filmes):
   print(filme)


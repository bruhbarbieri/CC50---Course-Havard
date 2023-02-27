import csv

names = {
    "Bruna": 0,
    "Giovane": 0,
    "Olivia": 0,
    "Mariana": 0,
    "Ana": 0,
    "Milton": 0
}

with open("phonebook.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        names[name] += 1

for name in names:
    print(name, ":", names[name])



from cs50 import get_string

people = {
    "Bruna": "32",
    "Giovane": "29"
}

name = get_string("Name: ")
if name in people:
    print("Age:", people[name])
else:
    print("Name not found")
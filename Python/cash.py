from cs50 import get_float

valor = 0

while(valor <= 0):
    valor = get_float("Valor: ")

centavos = round(valor * 100)

c25 = centavos // 25
c10 = (centavos - (c25 * 25)) // 10
c5 = (centavos - (c25 * 25) - (c10 * 10)) // 5
c1 = centavos - (c25 * 25) - (c10 * 10) - (c5 * 5)

print("25cents: ", c25)
print("10cents: ", c10)
print("5cents: ", c5)
print("1cents: ", c1)
print("Total de moedas: ", c25 + c10 + c5 + c1)
from cs50 import get_int

altura = 0

while(altura < 1 or altura > 8):
    altura = get_int("Altura: ")

bloco = 1

espaco = altura - bloco

for i in range(altura):
    print(" " * espaco, end="")
    print("#" * bloco, end="")
    print(" ", end="")
    print("#" * bloco)
    bloco = bloco + 1
    espaco = altura - bloco
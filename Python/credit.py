from cs50 import get_string

def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

def multiplica(number):
    newNumber = []
    digito = len(number) - 1
    for i in range((digito-1), -1, -2):
        multiplicacao1 = int(number[i]) * 2
        multiplicacao = str(multiplicacao1)
        if(len(multiplicacao) >= 2):
            digitoNew = len(multiplicacao)
            for i in range(digitoNew):
                newNumber.extend([int(multiplicacao[i])])
        else:
            newNumber.extend([int(multiplicacao[0])])
    return soma(newNumber)

def repete(number):
    newNumber = []
    digito = len(number) - 1
    for i in range(digito, -1, -2):
        repeticao = int(number[i])
        newNumber.extend([repeticao])
    return soma(newNumber)

def validaCartao():
    somaTotal = multiplica(myNumber) + repete(myNumber)
    print("A soma dos digitos do cartão é:", somaTotal)
    somaTotal2 = str(somaTotal)
    digitoFinal = len(somaTotal2) - 1

    if somaTotal2[digitoFinal] == "0" :
        print("Cartão de Crédito Válido")
    else:
        print("Cartão de Crédito Inválido")

def validaBandeira():
    if myNumber[0] == "3":
        if myNumber[1] == "4" or myNumber[1] == "7":
            print("Bandeira: AMEX")
        else:
            print("Bandeira INVÁLIDA")
    elif myNumber[0] == "5":
        if myNumber[1] == "1" or myNumber[1] == "2" or myNumber[1] == "3" or myNumber[1] == "4" or myNumber[1] == "5":
            print("Bandeira: MASTERCARD")
        else:
            print("Bandeira INVÁLIDA")
    elif myNumber[0] == "4":
        print("Bandeira: VISA")
    else:
        print("Bandeira INVÁLIDA")

myNumber = get_string("Digite o número do cartão de crédito: ")

validaCartao()

validaBandeira()



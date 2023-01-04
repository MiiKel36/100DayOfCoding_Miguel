


def calcAnos(ano):
    return ano * 365

anos = int(input('Escreva sua idade'))
while anos < 0:
    anos = int(input('Escreva apenas numeros positivos\nEscreva sua idade novamente'))

print(calcAnos(anos))
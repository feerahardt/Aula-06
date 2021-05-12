# Escreva uma função que recebe dois parâmetros (números) e imprime o
# menor dos dois. Se eles forem iguais, imprima que são valores idênticos

def numero(a, b):
    if a == b:
        print(f'Número {a} é igual ao número {b}')
    elif a < b:
        print(f'Número {a} é menor que número {b}')
    else:
        print(f'Número {b} é menor que número {a} ')


numero(1, 3)

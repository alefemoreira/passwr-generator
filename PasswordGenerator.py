from random import randint

def presencaDeRequerimentos(lowers, uppers, symbols, numbers, comprimento):
    pont = 0
    if lowers:
        pont += 1
    if upper:
        pont += 1
    if symbols:
        pont += 1
    if numbers:
        pont += 1
    if comprimento > 8:
        pont += 1

    return pont*2

def pontuacaoMaiuscula(uppers, comprimento):
    return (comprimento - uppers) * 2

def pontuacaoMinuscula(lowers, comprimento):
    return (comprimento - lowers) * 2

def pontuacaoSimbolos(symbols):
    return symbols * 6

def pontuacaoNumeros(numbers):
    return numbers * 4

def calculaComplexidade(senha, qtd):
    comprimentoDaSenha = len(senha)
    pontuacao = comprimentoDaSenha*4
    pontuacao += pontuacaoMaiuscula(qtd['uppers'], comprimentoDaSenha)
    pontuacao += pontuacaoMinuscula(qtd['lowers'], comprimentoDaSenha)
    pontuacao += pontuacaoSimbolos(qtd['symbols'])
    pontuacao += pontuacaoNumeros(qtd['numbers'])

    return pontuacao

def verificaComplexidade(senha):
    global lower, upper, symbols, numbers
    l = u = s = n = False
    qtd = {'lowers': 0, 'uppers': 0, 'symbols': 0, 'numbers': 0}
    requerimentos=0
    for c in senha:
        if c in lower:
            qtd['lowers'] += 1
            l = True
        elif c in upper:
            qtd['uppers'] += 1
            u = True
        elif c in symbols:
            qtd['symbols'] += 1
            s = True
        elif c in numbers:
            qtd['numbers'] += 1
            n = True

    pont = calculaComplexidade(senha, qtd) + presencaDeRequerimentos(l, u, s, n, len(senha))

    print(pont)

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols='!@#$%&_+-/\*~<>?'
numbers='1234567890'
todosCaracteres=upper+symbols+lower+numbers
senha = ''

tamanhoDaSenha = int(input("Digite o tamanho da sua senha: "))

for c in range(0, tamanhoDaSenha):
    senha += todosCaracteres[randint(0, len(todosCaracteres)-1)]

print(f'\033[0;37msua senha é : \033[4;32m{senha}\033[m')

verificaComplexidade(senha)

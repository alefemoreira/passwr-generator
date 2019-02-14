from random import randint

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols='!@#$%&_+-/\*~<>?'
todosCaracteres=upper+symbols+lower
senha = ''

tamanhoDaSenha = int(input("Digite o tamanho da sua senha: "))

for c in range(0, tamanhoDaSenha):
    senha += todosCaracteres[randint(0, len(todosCaracteres)-1)]

print(f'sua senha é : {senha}')

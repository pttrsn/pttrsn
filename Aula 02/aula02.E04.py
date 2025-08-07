#Aula 02 - Exercício 4

ssenha='senha123'

tentativa = 0

while tentativa < 3:
    ssenha = str(input('Digite sua senha: '))
    if ssenha == 'senha123':
        print('Acesso concedido.')
        break
    elif ssenha != 'senha123':
        print('Senha incorreta.')
        tentativa += 1
        print('Acesso negado.')
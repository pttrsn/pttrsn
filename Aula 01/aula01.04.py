#Aula01.04 - Exercício de login

print('Login')

email = input('Insira seu e-mail: ')
senha = input('Insira sua senha: ')
conf_senha = input('Confirme sua senha: ')

if conf_senha != senha:
    print("Senha Incorreta")

#comp_senha = senha == conf_senha
#print(comp_senha)
#Aula01 - Exercício de operações

#Comando
print('- Operações Matemáticas -')
x = int(input('Digite um número: '))
y = int(input('Digite um operador: '))

#Variáveis de operação
numero = x
op = y
#
#Operações matemáticas
soma = x+y
subtracao = x-y
multiplicacao = x*y
divisao = x/y
divisao_inteira = x//y
resto_da_divisao = x%y
potencia = x**y

#Respostas do programa
print('A soma de', x,'+', y, '=', soma)
print('A subtração de', x,'-', y, '=', subtracao)
print('A multiplicação de', x,'*', y, '=', multiplicacao)
print('A divisão de', x,'/', y, '=', divisao)
print('A divisão inteira de', x,'//', y, '=', divisao_inteira)
print('O resto da divisão de', x,'%', y, '=', resto_da_divisao)
print('A potência de', x,'**', y, '=', potencia)
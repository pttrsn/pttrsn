#Aula 02 - Exercício 2

preco = float(input('Digite o preço do produto: '))

desconto = preco*0.10

if preco >= 100:
    print(f'O valor do produto com desconto é: R$,{preco-desconto:.2f}')
else:
    print('O produto não possui desconto.')
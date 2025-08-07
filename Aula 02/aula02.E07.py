#Aula 02 - Exercício 7

i = int(input('Escreva sua idade: '))

if i <= 12:
    print('Criança. De 0 a 12 anos')
elif i <= 17:
    print('Adolescente. De 13 a 17 anos')
else:
    print('Adulto. De 18 a 59 anos')
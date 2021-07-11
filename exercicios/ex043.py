"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seus status, de acordo com a tabela abaixo:
— Abaixo de 18.5: Abaixo do peso
— Entre 18.5 e 25: Peso ideal
— 25 até 30: Sobrepeso
— 30 até 40: Obesidade
— Acima de 40: Obesidade mórbida
"""

print('='*20)
print('Calculadora de IMC')
print('='*20)

peso = float(input('Quantos kilos você pesa? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / pow(altura, 2)

print('O seu IMC é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está em obesidade')
else:
    print('Você está em obesidade mórbida')

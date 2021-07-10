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
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')

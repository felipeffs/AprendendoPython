"""
Escreva um programa que converta uma temperatura
digitada em ºC e converta para ºF.

Formula de Conversão (0 °C × 9/5) + 32 = 32 °F
"""
tempC = float(input('>>Conversor de Celsius para Fareheint'
                    '\nDigite a temperatura em graus celsius: '))
tempF = tempC * 9 / 5 + 32
print('{}°C equivale a {}°F'.format(tempC, tempF))

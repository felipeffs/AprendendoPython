# Extra: fazer Km,hm,dam,m,dm,cm,mm
valorM = float(input('Digite um valor em metros: '))
valorCm = valorM * 100
valorMm = valorCm * 10
print('{} metros é igual a {:.0f} centimetros, {:.0f} milimetros'.format(valorM, valorCm, valorMm))

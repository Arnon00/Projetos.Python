from math import pow

co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))

# Forma matematica pura:   hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa é {:.2f}'.format(hi))

co2 = pow(co,2)
ca2 = pow(ca,2)

hipo = co2+ca2

print('O Cateto Adjacente é: {:.0f}, O Cateto Oposto é: {:.0f}, e a Hipotenusa é: {:.2f} '.format(ca2, co2, math.sqrt(hipo)))

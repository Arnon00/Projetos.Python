import math

angulo = float(input('Digite o valor do angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O angulo de {:.0f}º. \nO seno é: {:.2f}. \nO cosseno é: {:.2f}. \nA tangente é: {:.2f}'.format(angulo, sen, cos, tan))
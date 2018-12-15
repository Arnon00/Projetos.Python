from math import trunc, ceil, floor

num = float(input('Digite um numero real fracionado qualquer: '))
print("O arredindamento é: Para Baixo -> {}, para Cima -> {}, Truncado -> {}".format(floor(num), ceil(num), trunc(num) ))

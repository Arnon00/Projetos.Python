num = float(input('Digite a distancia em metros: '))

cen = float(0.00100)
mil = float(0.00010)

rescen = int(num/cen)
resmil = int(num/mil)

print('metros: {}, centimetros: {}, Milimetros: {}'.format(num, rescen, resmil))

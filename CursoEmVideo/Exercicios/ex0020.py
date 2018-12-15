import random

non = []

sort = random.randint(0,4)

for i in range(0,4):
    non.append(str(input('Digite o nome dos alunos: ')))

else:
        print('\n\nvocê cadastou {} alunos.'.format(len(non)))

random.shuffle(non)
print ('A ordem de apresentação sera: ')
for i in non:
    print('{}'.format(i))
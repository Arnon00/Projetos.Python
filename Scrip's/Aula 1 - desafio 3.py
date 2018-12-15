num1 = int(input('Digite o primeiro numero desejado: '))
num2 = int(input('digite o segundo numero desejado: '))

soma = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2

print('soma:', soma)
print('Subtração:', sub)
print('Multiplicação:', mult)
print('Divisão:', div)


print('Potencialização!')

def main():
    n = int(input("Digite o primeiro numero: "))
    k = int(input("Digite o segundo numero: "))
    s = 0
    soma = 1
    while s < k:
            soma = soma * n
            s = s+1

    print('O resultado é: ',soma)

main()

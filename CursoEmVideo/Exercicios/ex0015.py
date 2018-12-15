dias = int(input("Ola, quantos dias você focou com o carro? \n:"))
km = float(input("Quantos Km foram rodados? \n:"))

valordias = (dias*60)
valorkm = (km*0.15)

apagar = (float(valordias)+valorkm)

print("Voce alugou o carro por {} dias, e rodou {} Km... O valor do seu aluguel é de {}.".format(dias, km, apagar))

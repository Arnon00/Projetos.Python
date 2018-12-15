print("Digite a seguir as medidas da parede (Na ordem, Altura depois largura)")
alt = float(input("Qual a Altura? : "))
lag = float(input("Qual a Largura? : "))

area = (alt*lag)
pint = (area/2)

print("A area da sua parede é: {:.2f}m², você precisara de {} litros de tinta".format(area, pint))

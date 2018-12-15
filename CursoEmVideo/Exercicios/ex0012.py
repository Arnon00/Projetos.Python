val = float(input("Qual o valor do produto desejado? "))
desc = float(input("Quanto de desconto sera praticado? "))

ndesc = (((desc/100)*val))
nval = (val-ndesc)

print("O preço do produto é {}, foi concedido {:.1f}% de desconto, em reais foram {} de desconto, e o novo valor sera {}".format(val, desc, ndesc, nval))
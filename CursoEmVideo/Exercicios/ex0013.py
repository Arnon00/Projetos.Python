sal = float(input("Voce esta prestes a promover um funcionario, digite o valor atual do salario dele: "))
bns = float(input("Em quantos porcentos você quer almentar o salario dele? "))

nbns = ((bns/100)*sal)
nsal = (sal+nbns)

print("O salario antigo era {}, com um acrecimo de {}%, agora passara a ser {:.2f}".format(sal, bns, nsal))

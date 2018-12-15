temp = float(input("Digit a temperatura atual em Cº: "))

fahrein = float((1.8*temp)+32) #conversão Cº para Fº >> (((9*temp)/5)+32)
celcios = float((fahrein-32)/1.8) #conversão Fº para Cº
kelvin = float(celcios+273.15) #conversão Cº para K

print("a temperatura é: \nCelcios: {:.2f} Cº.\nfahrein: {:.2f} Fº.\nkelvin: {:.2f} K.".format(celcios, fahrein, kelvin))
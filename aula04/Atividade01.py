valor = float(input("Digite o valor da compra: "))

if valor > 250:
    desconto = valor * 0.16
    valor_final = valor - desconto
    print ("Valor com Desconto:", valor_final)
else:
    print("Valor sem desconto:", valor)
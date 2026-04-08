valor = float(input("Digite o valor da compra: "))
forma_de_pagamento = (input("Digite se a compra é a vista ou a prazo").lower().strip()) 

if valor >= 250 and forma_de_pagamento == "a vista":
    desconto = valor * 0.16
    valor_final = valor - desconto
    print ("Valor com Desconto:", valor_final)
else:
    print("Valor sem desconto:", valor)
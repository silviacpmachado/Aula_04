tempo = float(input("Digite o tempo de filiação (anos): "))
valor = float(input("Digite o valor movimentado nos últimos 6 meses (R$): "))

if tempo > 3 or valor > 5000:
    print("O cooperado tem direito ao benefício especial.")
else:
    print("O cooperado ainda não atende aos critérios para o benefício.")
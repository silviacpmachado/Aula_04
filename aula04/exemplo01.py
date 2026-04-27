# # idade = 16
# # if idade >=18:
# #     print('você é adulto')
# # else:
# #     print('Você não é adulto')

# # #--------------------------------

# # pontos = int(input('Informe os pontos: '))
# # if pontos >= 100:
# #     print('excelente')
# # elif pontos >= 50:
# #     print('Bom Desempenho')
# # elif pontos >= 25:
# #     print('Satisfatório')
# # else:
# #     print('Pratique Mais...')

# # Operadores AND e OR
# usuario = input('Nome: ')
# senha = input('Senha: ')

# if usuario == "admin" and senha == "1234":
#     print('Login Realizado com Sucesso')
# else:
#     print('Usuário ou senha incorretos')

# if usuario == "admin" or senha == "1234":
#     print('Login Realizado com Sucesso')
# else:
#     print('Usuário ou senha incorretos')

#Exemplo IFs encadeados - verifica todas
nota = 5.5
if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('E')

#Exemplo IFs não encadeados
nota = 10
if nota >= 9:
    print('A')

if nota >= 7:
    print('B')

if nota >= 5:
    print('C')

elif nota >= 3:
    print('D')
else:
    print('E')

#Ifs aninhados
nota = float(input('Insira a nota: '))
frequencia = float(input('Informe a frequencia'))

if nota >=7:
    #Aprovado por nota, mas precisa checar a frequência.
    if frequencia >= 75:
        print('Aluno aprovado por Nota e Frequência')
    else:
        print('Reprovado por frequência baixa')
else: 
    print('Reprovado por nota baixa.')

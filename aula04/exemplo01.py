# idade = 16
# if idade >=18:
#     print('você é adulto')
# else:
#     print('Você não é adulto')

# #--------------------------------

# pontos = int(input('Informe os pontos: '))
# if pontos >= 100:
#     print('excelente')
# elif pontos >= 50:
#     print('Bom Desempenho')
# elif pontos >= 25:
#     print('Satisfatório')
# else:
#     print('Pratique Mais...')

# Operadores AND e OR
usuario = input('Nome: ')
senha = input('Senha: ')

if usuario == "admin" and senha == "1234":
    print('Login Realizado com Sucesso')
else:
    print('Usuário ou senha incorretos')

if usuario == "admin" or senha == "1234":
    print('Login Realizado com Sucesso')
else:
    print('Usuário ou senha incorretos')
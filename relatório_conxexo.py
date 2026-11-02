print("Preencha como solicitado poara obter resultados");

nome_Usuario = input("DIGITE O NOME DO USUARIO: ")
porta_alvo = 80
status_concexao = True

print("--- RELATÓRIO DE CONEXÃO---")
print("Usuario",  nome_Usuario)
print("Porta analisada", porta_alvo)
print("Status da conexão ativa:  ", status_concexao)

tentatuivas = (int(input("DIGITE O NUMERO DE TENTATIVAS DE LOGIN: ")))
print("TOTAL DE TENTATIVAS DE LOGIN REGISTRADAS: ", tentatuivas)
print("-----SISTEMADE NALISE DE RISCO-----")

tentativas= int(input("DIGITE A QUANTIDADE DE TENTAUVAS EFETIVADAS: "))

if tentativas>= 10:
    print("[ALERTA CRITICO] Possivel ataque de força bruta detectado!")
    print("Bloquear o IP imediatamente")
elif tentativas >= 5:
    print("[ALERTA MODERADO] Numero elevado de tentativas incorretas")
    print("Enviar e-mail de confirmaão ao usuario")
else:
    print("[STATUS NORMAL] NENHUMA AÇÃO NECESSARIA")
    print(" Permitir o acesso normalmente")
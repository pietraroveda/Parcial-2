# Programa que converte:
# 1 - Segundos para horas, minutos e segundos
# 2 - Horas, minutos e segundos para segundos

# Exibe o menu
print("=== Conversor de Tempo ===")
print("1 - Converter segundos para horas/minutos/segundos")
print("2 - Converter horas/minutos/segundos para segundos")

# Escolha do usuário
opcao = input("Escolha uma opção (1 ou 2): ")

# Opção 1: segundos -> horas, minutos e segundos
if opcao == "1":
    # Solicita o total de segundos
    segundos = int(input("Digite o total de segundos: "))
    
    # Calcula as horas
    horas = segundos // 3600
    
    # Calcula o restante após retirar as horas
    resto = segundos % 3600
    
    # Calcula os minutos
    minutos = resto // 60
    
    # Calcula os segundos restantes
    seg_restantes = resto % 60
    
    # Mostra o resultado
    print("Resultado:")
    print(horas, "horas,", minutos, "minutos e", seg_restantes, "segundos")

# Opção 2: horas, minutos e segundos -> segundos
elif opcao == "2":
    # Solicita os valores
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    
    # Converte tudo para segundos
    total = (horas * 3600) + (minutos * 60) + segundos
    
    # Mostra o resultado
    print("Total em segundos:", total)

# Caso o usuário digite uma opção inválida
else:
    print("Opção inválida!")
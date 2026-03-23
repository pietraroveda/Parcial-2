# Programa para calcular juros simples
# Fórmula: J = (C * I * T) / 100

# Solicita ao usuário o valor do capital (C)
capital = float(input("Digite o valor do capital (C): "))

# Solicita ao usuário a taxa de juros (I) em porcentagem
taxa = float(input("Digite a taxa de juros (I) em %: "))

# Solicita ao usuário o tempo (T)
tempo = float(input("Digite o tempo (T): "))

# Calcula o valor dos juros simples usando a fórmula
juros = (capital * taxa * tempo) / 100

# Exibe o resultado final
print("O valor dos juros simples (J) é:", juros)
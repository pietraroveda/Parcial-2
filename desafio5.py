# Programa para calcular a área de um triângulo

# Função que calcula a área
def calcular_area(base, altura):
    return (base * altura) / 2  # Fórmula da área do triângulo

# Exibe uma mensagem inicial
print("=== Cálculo da Área de um Triângulo ===")

# Solicita os valores ao usuário
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

# Chama a função para calcular a área
area = calcular_area(base, altura)

# Mostra o resultado
print("A área do triângulo é:", area)
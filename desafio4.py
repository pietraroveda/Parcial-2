# Calculadora simples em Python

# Função para somar
def soma(a, b):
    return a + b

# Função para subtrair
def subtracao(a, b):
    return a - b

# Função para multiplicar
def multiplicacao(a, b):
    return a * b

# Função para dividir
def divisao(a, b):
    # Verifica se o divisor é zero para evitar erro
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Exibe o menu de opções
print("=== Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Pede ao usuário para escolher uma opção
opcao = input("Escolha uma operação (1/2/3/4): ")

# Pede os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica a opção escolhida e executa a operação
if opcao == "1":
    print("Resultado:", soma(num1, num2))

elif opcao == "2":
    print("Resultado:", subtracao(num1, num2))

elif opcao == "3":
    print("Resultado:", multiplicacao(num1, num2))

elif opcao == "4":
    print("Resultado:", divisao(num1, num2))

else:
    print("Opção inválida!")
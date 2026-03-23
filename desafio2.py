# Programa para verificar se um número é par ou ímpar

# Solicitar ao usuário para inserir um número
# A função input() recebe uma entrada do usuário, que será convertida para inteiro (int)
numero = int(input("Digite um número: "))  # Lê o número do usuário e converte para inteiro

# Verificar se o número é par ou ímpar usando o operador módulo (%)
# O operador % calcula o resto da divisão entre o número e 2
if numero % 2 == 0:  # Se o resto da divisão for 0, o número é par
    # Se o número for divisível por 2 (resto 0), ele é par
    print(f"O número {numero} é par.")  # Exibe que o número é par
else:
    # Caso contrário, o número é ímpar
    print(f"O número {numero} é ímpar.")  # Exibe que o número é ímpar
# Programa para somar dois números

try:
    # Solicita ao usuário para inserir o primeiro número
    # O input() recebe dados como texto, então usamos float() para converter para um número decimal
    numero1 = float(input("Digite o primeiro número: "))
    
    # Solicita ao usuário para inserir o segundo número
    # Da mesma forma, convertemos o input em um número decimal
    numero2 = float(input("Digite o segundo número: "))

    # Somamos os dois números e guardamos o resultado na variável 'soma'
    soma = numero1 + numero2

    # Exibimos o resultado da soma para o usuário
    # Usamos f-strings para formatar a mensagem com os valores das variáveis
    print(f"A soma de {numero1} e {numero2} é {soma}.")

# Caso o usuário insira algo que não possa ser convertido para float (como letras ou símbolos), 
# o programa entra no bloco 'except' e exibe uma mensagem de erro amigável.
except ValueError:
    print("Por favor, insira apenas números válidos.")
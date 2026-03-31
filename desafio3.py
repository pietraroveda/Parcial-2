nomes = []

quantidade = int(input("Quantos nomes você quer digitar? "))

for i in range(quantidade):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("\nNomes digitados:")
for nome in nomes:
    print(nome)

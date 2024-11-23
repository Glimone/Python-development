nome = input("Informe o seu nome: ")
x = 0
print(f"  Bem vindo! ")
while x < len(nome):
    novo_nome = nome[x].upper()
    print(f"{novo_nome}*", end="")
    x += 1


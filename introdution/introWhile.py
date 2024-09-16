print("Uma dessas palavras dessa frase é a palavra mágica. Você vai precisar em breve dela...")

name = input("Informe o seu nome: ")

magic = "mágica"
while name != "sair":
    palavraCerta = input(f"{name}, para escapar desse loop, informe a palavra mágica: ")
    if palavraCerta == magic:
        print("VOCÊ ESTÁ LIVRE!")
        break
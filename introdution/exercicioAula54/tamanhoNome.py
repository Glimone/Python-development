firstName = input("Informe apenas o seu primeiro nome: ")
firstName.strip()

if len(firstName) <= 4:
    print("Seu nome é curto. ")
elif len(firstName) == 5 or len(firstName) == 6:
    print("Seu nome é normal. ")
elif len(firstName) > 6:
    print("Seu nome é grande.")
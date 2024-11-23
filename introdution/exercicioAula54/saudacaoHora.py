

nome = input("Qual é o seu nome? ")
horas = input("Que horas são? ")

horas = int(horas.split(":")[0])

if horas >= 0 and horas <= 11:
    print(f"Bom dia, {nome}!")
elif horas >= 12 and horas <= 17:
    print(f"Boa tarde, {nome}!")
elif horas >= 18 and horas <= 23:
    print(f"Boa noite, {nome}! ")

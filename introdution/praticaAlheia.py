p = "Auga"
c = ""
while True:
    letra = input("Digite uma letra: ").lower()
    if letra in p.lower():
        c += letra
    
    for s in p:
        if s.lower() in c:
            print(s)
        else:
            print("*")
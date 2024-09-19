nome = input("Informe o seu nome: ")
x = 0
print(f"\nBem vindo(a)!")
while x < len(nome):
    novo_nome = nome[x].upper()
    print(f"{novo_nome}*", end="" )
    x += 1

print("\n")
while True:
    print("---------------------------------------------------")
    print("Você está na cálculadora de operações básicas!".upper())
    print("---------------------------------------------------")
    sair = input("Você deseja sair? [s]im ou [n]ão? \n")
    if sair == "s":
        break
    else:   
        print("Escolha abaixo o tipo de operação que deseja fazer: ")
        print("Para SOMA, digite: + \n")
        print("Para SUBTRAÇÃO, digite: - \n")
        print("Para divisão, digite: / \n")
        print("Para multiplicação, digite: x \n")      
        op = input("Digite a sua preferência: ".upper())
        if op == "+":
            op_Name = "Soma"
        elif op == "-":
            op_Name = "Subtração"
        elif op == "/":
            op_Name = "Divisão"
        elif op == "x":
            op_Name = "Multiplicação"
        print(f"Que bom que escolheu uma {op_Name}!")
        n1 = int(input(f"Agora, preciso que você me digite o primeiro número da sua {op_Name}: "))
        n2 = int(input(f"Ótimo! Agora o segundo número: "))
        if op == "+":
            n3 = n1 + n2
            print(f"A {op_Name} de {n1} e {n2} é igual a{n3}")
        elif op == "-":
            n3 = n1 - n2
            print(f"A {op_Name} de {n1} e {n2} é igual a {n3}")
        elif op == "/":
            n3 = n1 / n2
            print(f"A {op_Name} de {n1} e {n2} é igual a {n3}")
        elif op == "x":
            n3 = n1 * n2
            print(f"A {op_Name} de {n1} e {n2} é igual a {n3}")
            
print("calculadora encerrada".upper())

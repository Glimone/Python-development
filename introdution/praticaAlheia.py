# """Arquivo usado apenas para praticas coisas aleatórias que não serão salvas.
# """


name = input("Digite o seu nome: ")
age =  input("Digite a sua idade: ")

if name != "" or name != " " and age != "" or age != " ":
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    
    if " " in name:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços.")

    print(f"Seu nome tem {len(name)} letras.")
    
    if len(name) > 0:
        print(f"A última letra do seu nome é {name[-1]}")
        print(f"A primeira letra do seu nome é {name[0]}")
    else:
        print("Você não digitou o seu nome! ")
        
else: 
    print("Desculpe, você deixou campos vázios! ")


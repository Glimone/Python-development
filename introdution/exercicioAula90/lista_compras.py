lista = []
valores = []

print(f"Os itens no momento da sua lista de compras são: {lista}\n")

while True: 
    
    condic = input("Deseja fazer mais alguma dessas ações?\n ADICIONAR(Digite A)\n EXCLUIR O ÚLTIMO ITEM(Digite E)\n MOSTRAR LISTA(Digite M)\n SAIR(Digite X)\n\nInforme a sua opção: ")
    try:

        if condic == "A":
            new_item = input("Informe o novo item: ")
            try:
                new_value = float(input("Informe o valor desse item(Uso ponto antes dos decimais, ex: 12.20): \n"))
                lista.append(new_item)
                valores.append(new_value)
            except ValueError:
                print("Valor inválido, por favor, digite um número. ")
            

        elif condic == "E":
            if lista:
                lista.pop()
                valores.pop()
                print(f"Sua lista: {lista} ")
            else:
                print("Não existe nada na lista para a exclusão.")

        elif condic == "M":
            for x, y in zip(lista, valores):
                print(f"Item {x} no valor {y}\n")
        elif condic == "X":
            print("Encerrando o programa...")
            break
        
        elif condic not in ["A", "E", "M", "X"]:
            print("Opção inválida, por favor, selecione uma válida. \n")

    except ValueError as ve:
        print(f"erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

for x, y in zip(lista, valores):
    print(f"Item {x} no valor {y}")


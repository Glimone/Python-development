x = "Eugema"
y = 12.453
lista_variavel = ("João", True, 14.5, "Augas", 11, x, y)

for indice, z in enumerate(lista_variavel): #O enumerate() transforma uma sequência iterável em pares, cujos sempre serão indice e elemento no indice. Ao aplicar isso num for, está iterando, dizendo que esses pares devem ser armazenados nas variáveis indice e z, na respectiva ordem. 
    print(f"indice: {indice} item: {z}")
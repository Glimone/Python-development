#Para casos de concatenação e extensão, usa-se em padrão + e o método extend().

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista3 = lista1 + lista2 #"+ Concatena listas."
print(lista3)

lista4 = [10, 11, 12, 13, 14, 15, "Juiz"]

lista1.extend(lista4) #Modificamos a lista1, fazendo com que ela seja extendida agora pela lista4. É diferente de concatenar quando realiza a alteração da lista1 para lista1 definidamente para lista1 e a lista4 para a lista1 (A lista 4 segue existindo como na origem)
print(lista1)


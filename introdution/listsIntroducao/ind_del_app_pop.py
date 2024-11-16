#Métodos com utilidade em listas: append, insert, pop, del, clear, extend

lista = [1, 2, 3, 4]

del lista[3] #del apaga o indice indicado ou toda a variavel se optar, assim como qualquer elemento indicado.
print(lista)


lista.append(4) #Append serve para adicionar valores no final da lista. 
lista.append(5)
print(lista)

lista.pop() #Remove o último elemento da lista.
print(lista)

print(len(lista)) 
lista.insert(5, 25) #Insert serve pra adicionar um valor em um indice específicado.
           #Ordem: (indice, valor)
print(lista)
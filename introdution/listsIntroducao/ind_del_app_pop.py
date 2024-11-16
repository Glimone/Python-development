#Métodos com utilidade em listas: append, insert, pop, del, clear, extend

lista = [1, 2, 3, 4]

del lista[3] #del apaga o indice indicado ou toda a variavel se optar, assim como qualquer elemento indicado.
print(lista)


lista.append(4) #Append serve para adicionar valores no final da lista. 
lista.append(5)
print(lista)

lista.pop() #Remove o último elemento da lista.
print(lista)
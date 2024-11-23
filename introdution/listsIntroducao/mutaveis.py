
#listas de tipos comuns:
lista = ["Nome1", "Nome2"]
print(lista)
print(type(lista)) #listas são mutaveis. 


#listas de tipos diversos: 
x = "Teste"
lista_comum = [5/2, 10/5, 20/2]
diverso = [10, 12.5, "Doze", True, x, lista_comum]
print(diverso)
print()
#Acesso de listas por indice:

print(diverso[5])

#Alteração de item:
print()
print("Compare antes de alterarmos o item por indice: ")
diverso[2] = "Quarenta e nove"
print(diverso)
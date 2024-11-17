lista = ["Arroz", "Feijão", "Salgadinho", "Macarrão"]
i1, i2, *r = lista #Nós aplicamos os indices em ordem nas novas variáveis e a var com "*" define que os outros são restos.
print(i1, i2,)

lista1 = lista.copy()
i3,_, *l = lista1
print(i3, _) #O "_" é usado para informar que o indice guardado na var chamada _ não deve ser considerada.

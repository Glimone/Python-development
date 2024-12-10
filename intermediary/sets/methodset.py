tuplex = ('Gabriel', "Eduardo")
tupley = ('Maria', 'Francisca')
s1 = {tuplex, tupley}

tuplez = ('Cemento', 'Cenoura')
s1.add(tuplez) # - Adiciona um novo item
print(s1)

s1.update('Se o mundo inteiro') #Adiciona mais de um item e atualiza como desejar.
print(s1)

s1.clear() #Limpa todo o conjunto set
print(s1)

s1 = {tuplex, tupley}
s1.discard(tupley) #Você discarta um dos valores deixando claro qual é. 
print(s1)
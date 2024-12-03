# Principais métodos para dicionários:

carro = {
    'Marca': 'Ferrari',
    'Modelo': 'SF90 Stradale',
    'Ano' : '2024',
    'Cor' : 'Vermelha',}

# len - Mostra quantas chaves tem no dict
print(len(carro))

# keys() - Mostra as chaves do dict
print(f"{carro.keys()}\n")

#Values() - Mostra os valores contidos nas chaves
print(f"{carro.values()}\n")

#Items() - Mostra as chaves e seus respectivos valores (É o keys + values em um só)
print(f"{carro.items()}\n")

#setdefault() - Caso a chave não exista, você a adiciona e seu respctivo valor. 
# print(carro['velocidade']) - Se rodar isso, dará keyError, pois essa chave não existe. 
carro.setdefault('velocidade', 250) 
print(carro['velocidade']) #Estrutura = dict_name.setdefault('keyName', value)


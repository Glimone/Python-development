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

#Get - Obtem chave do dicionário e retorna valor ou nome da chave.
print(carro.get('Cor'))


#pop - Serve para excluir uma chave, mas não necessariamente o valor. Ao usar o pop você pode transferir o valor para uma var. 

ano = carro.pop('Ano')
print(ano)
print(f"{carro}\n") #Veja que o ano está na var agora e não aparece mais no dict.

#popitem - Elima a última chave do dicionário. 

ultima_chave = carro.popitem()
print(ultima_chave)

#update - Modo de atualizar totalmente o seu dict com a quantidade de chaves e valores que você desejar.

carro.update( {

    'ano': 2024,
    'km': 0, 
    'revestimento': 'prata',
} )

print(f"{carro}\n")
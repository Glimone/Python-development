#É possível fazer copias de elementos mutáveis de um modo raso(ShallowCopy) e um modo que copie os detalhes de elementos mutáveis. 

d1 = {
    'a':1,
    'b':2,
    'c':3,
    'li': [5,6,7,8]
}

d2 = d1.copy() #Copy copia o elemento e salva em outro endereço de memória.

d1['d'] = 4

# d2['li'][1] = 100
#Veja que ambas as listas abaixo vão mudar com essa mudança no d2, por isso é essencial o deepcopy().

#O shallow copy não copia subníveis, apenas o nível mais superficial.
#Isso significa que se você mudar um subnível em um copy, mudará no original também, pois o copy não trata processamento complexo. 
#Importando o modulo copy pro uso do deepcopy().
import copy

d2 = copy.deepcopy(d1)
d2['li'][1] = 100 #Deep copy fez com que a mudança seja considerada apenas na copia profunda, a d2.
print(d2)
print(d1)
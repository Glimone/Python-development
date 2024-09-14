#Fatiamento é o ato de dividir partes da str selecionadas. 
#ex: 

exemplo = "Isso é um fatiamento de Str."
#Primeiro pra fatiar, você precisa ter uma noção do tamanho da str, nesse caso use a função len().
print(len(exemplo)) #28 caracteres
#Agora, fatie usando o indice inicial, ":" e o indice final. Caso você deseje que o indice comece já no 0 ou que finalize no último caracter, não precisa citar o primeiro indice nem o último, respectivamente. 

print(exemplo[10:21]) #[indice inicial : indice final]
print(exemplo[:21])  #[: indice final]
print(exemplo[21:]) #[indice inicial :]

#Errata: len() pode ser aplicado com outros tipos de dados também.

#Você pode colocar o conceito de passo também em seu fatiamento: 

print(exemplo[0:27:2])
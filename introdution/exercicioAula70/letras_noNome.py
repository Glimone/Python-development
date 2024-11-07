frase = """Bailam, corujas e pirilancos, entre os sacis e as fadas! """
contador = 0
letra_principal = ""
qnt_letra_principal = 0

while contador < len(frase):
    letra_atual = frase[contador]

    if letra_atual == " " or letra_atual == ".":  #Retira pontos e espaços da filtragem das letras. 
        contador += 1
        continue

    qnt = frase.count(letra_atual)   
    #Qnt retorna na ordem da string o total de cada uma delas, mesmo já sido repetida.


    if qnt_letra_principal < qnt: #Aqui, ele basicamente compara a quantidade da letra principal com a quantidade total da letra atual. 
        qnt_letra_principal = qnt #Quando a quantidade de x que a letra for maior que anterior, ele iguala essa quantidade e guarda a letra na linha abaixo. Então ele segue a estrutura comparando com as próximas letras, mesmo que já repetidas. 
        letra_principal = letra_atual  

        #Enquanto em cada loop a qnt adiciona quando aquela letra for repetida, logo em seguida essa quantidade é comparada com a quantidade anterior (A qnt_letra_principal) pra ver se ela é maior ou não. 

    contador += 1 

print(F"A letra que apareceu mais vezes foi {letra_principal}, em {qnt_letra_principal}x.")














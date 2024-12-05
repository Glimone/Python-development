#Sintaxe:
#dict_name = {'chave_name':valor}
pessoa = {
    'nome' : "Gabriel",
    'sobrenome' : "Limone ",
    'idade' : 20,
    'altura' : 1.78
}

#Acesso a valor: 
#dict_name['chave_name' desejada]
print(f"{pessoa['nome']}\n")

#Iteração de chaves:
for chaves in pessoa:
    print(f"{chaves}\n")

#Iteração de chaves e valores:
for chaves in pessoa:
    print(f"{chaves}, {pessoa[chaves]}")

#Criação de nova chave:
pessoa['sangue'] = 'O+'

print(pessoa['sangue'])
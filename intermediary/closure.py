#Closure são funções que tem como utilidade lembrar do ambiente em que foi criada, com esse ambiente encerrado ou não. Isso é útil pra manter um estado externo e lembrar de informações específicas entre chamadas.

#Ou seja, mesmo que a função principal seja encerrada, a interna pode ser chamada. A interna é definida com os dados da principal, assim quando chamada a interna, recorda os dados da principal.

def cria_contador(inicial): #Função principal
    contador = inicial #Var local que será lembrada

    def increment():
        nonlocal contador #Forma de dizer que a var do ambiente será modificada nesse escopo.
        contador += 1
        return contador #Retorno da varque será lembrada
    
    return increment #Retorno da função interna como closure, no caso, sem "()".

contador = cria_contador(20)
contadorx = cria_contador(50)

#Uso do closure, iniciando-o com "()" após a var global definida com a def:

print(f"contador: {contador()}")
print(f"contadorx: {contadorx()}")
print(f"contador: {contador()}")
print(f"contadorx: {contadorx()}")
print(f"contador: {contador()}")
print(f"contadorx: {contadorx()}")
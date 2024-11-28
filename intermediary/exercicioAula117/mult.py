#Duplicação:
def duplicar(n):
    x = n*2
    return x

duplicado = duplicar(10)

print(duplicado)

#Triplicação: 
def triplicar(n):
    x = n*3
    return x

triplicado = triplicar(5)
print(triplicado)

#Quadriplicação: 

def quadriplicar(n):
    x = n*4
    return x

quadriplicado = quadriplicar(25)
print(quadriplicado)


#Função usando closure:

def criar_mult(mult):
    def multiplicar(n):
        x = n * int(mult)
        return x
    return multiplicar

dupli = criar_mult(2)
tripli = criar_mult(3)
quadri = criar_mult(4)

print(f"Com closure duplicate: {dupli(4)}")
print(f"Com closure triplicate: {tripli(5)}")

print(f"Com closure quadriplicate: {quadri(10)}")
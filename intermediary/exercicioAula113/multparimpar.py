#Multiplicação dos valores
def multiplicator(*args):
    acumulador = 1
    for x in args:
        acumulador *= x
    return acumulador
 
 
n, y, z = [random.randrange(0, 100) for i in range(3)]
 
y = multiplicator(n, y, z)
print(y)
 
 
def parirmpar(a):
    if a % 2 == 0:
        return "Esse número é par"
    elif a % 2 == 1:
        return "Esse número é impar"
    
print(parirmpar(y))
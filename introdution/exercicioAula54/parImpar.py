try:
    number = int(input("Informe um número inteiro: "))
    if number % 2 == 0 :
        print("Esse número é par. ")
    else: 
        print("Esse número é impar. ")
except: 
    print("O caractere informado não é um número. ")
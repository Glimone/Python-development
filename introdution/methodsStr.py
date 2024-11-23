frase = "eu  amarei te minha princesa."
new_frase = frase.split()
#Split() cria uma lista com os elementos de um conjunto iterável, usando como ponto de separação o valor padrão (WhiteSPace) ou o valor indicado (Como uma letra.)

print(" Pra sempre ".join(new_frase)) #Join uso o elemento definido (Nesse caso whiteSpace) pra separar cada elemento do conjunto.

print(frase.strip()) #Método de tirar whitespaces de uma str (Só funciona em str, outros iteráveis como listas precisam ser tratadas, onde os elementos dela precisam ser iterados.) Também possui o lstrip e rstrip que 



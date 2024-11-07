word = "Corinthians"

print("------------------------")
print("Olá! Vamos jogar um joguinho? Tente adivinhar a palavra! \n")
print("------------------------")
print("Você deve dizer apenas uma letra até que acerte tudo! \n")
print("------------------------")
print("Sua quantidade de chances é o dobro de letras da palavra ;) ")
print("------------------------ \n")

x = 0
right_word = ""

while x < len(word)*2:
    letter = input("Digite uma letra: ")

    if letter in word:
        right_word += letter
    
    for letter in word:
        if letter in right_word:
            print(letter)
        else:
            print("*")


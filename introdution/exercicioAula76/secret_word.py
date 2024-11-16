import os

word = "Corinthians"

print("------------------------")
print("Olá! Vamos jogar um joguinho? Tente adivinhar a palavra! \n")
print("------------------------")
print("Você deve dizer apenas uma letra até que acerte tudo! \n")
print("------------------------")



right_letter = ""
chances = 0

while True:
    chances += 1
    letter = input("Digite uma letra: ").lower()

    if len(letter) > 1:
        print("Você deve digitar apenas uma letra! ")
        continue

    if letter in word.lower():
        right_letter += letter
    
    formad = ""
    for secret in word:
        if secret.lower() in right_letter: 
            formad += secret
        else:
            formad += "*"
        #A palavra será percorrida, se a letra da palavra percorrida for igual a letra correta informada pelo usuario, essa letra da palavra percorrida deverá ser adicionada na palavra formada. Se ocorrer dessa letra do usuario não for informada corretamente OU apenas não informada (Ou seja, uma outra certa que não seja ela), deve-se adicionar * na palavra formada.

    print(formad)
    if formad == word:
        os.system('clear')
        print(f"Parabéns, você ganhou! Completou a palvra {formad}! ")
        print(f"E precisou de {chances} tentativas pra acertar, ")
        break

    
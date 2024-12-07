perguntas = [
    { 
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opcoes': ['Salvador', 'São Paulo', 'Brasília', 'Rio de Janeiro'],
        'Resposta': 'Brasilia',
    },
    { 
        'Pergunta': 'Qual é o grupo indígena mais encontrado no Brasil?',
        'Opcoes': ['Tupi', 'Goytacaz', 'Astecas', 'Yanomami'],
        'Resposta': 'Tupi',
    },
    {
        'Pergunta': 'Quem criou o telescópio?',
        'Opcoes': ['Romero Brito', 'Galileu', 'Da Vinci', 'Copérnico'],
        'Resposta': 'Galileu',
    },
]

acertos = 0  

for i in perguntas:
    print(i['Pergunta'])

    alternativaCerta = ""  
    alternativas = 0  
    for x in i['Opcoes']:
        alternativas += 1
        print(f"{alternativas}) {x}")

       
        if x.strip().lower() == i['Resposta'].strip().lower():
            alternativaCerta = str(alternativas)
    
   
    userReturn = input("\nDigite a sua opção: ").strip().lower()

    
    if userReturn == i['Resposta'].strip().lower() or userReturn == alternativaCerta:
        acertos += 1
        print("Resposta Correta! \n")
    else:
        print("Resposta errada! \n")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

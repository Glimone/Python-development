import unicodedata  # Para tratar acentos diretamente

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

acertos = 0  # Inicializar fora do loop principal

for i in perguntas:
    print(i['Pergunta'])

    alternativaCerta = ""  # Inicializa a alternativa correta
    alternativas = 0  # Contador de alternativas

    for x in i['Opcoes']:
        alternativas += 1
        print(f"{alternativas}) {x}")

        # Normaliza para comparar sem acentos
        x_normalizado = ''.join(
            c for c in unicodedata.normalize('NFD', x)
            if unicodedata.category(c) != 'Mn'
        ).lower().strip()

        resposta_normalizada = ''.join(
            c for c in unicodedata.normalize('NFD', i['Resposta'])
            if unicodedata.category(c) != 'Mn'
        ).lower().strip()

        if x_normalizado == resposta_normalizada:
            alternativaCerta = str(alternativas)

    # Entrada do usuário
    userReturn = input("\nDigite a sua opção: ").strip()

    # Normaliza a entrada do usuário para remover acentos
    userReturn_normalizado = ''.join(
        c for c in unicodedata.normalize('NFD', userReturn)
        if unicodedata.category(c) != 'Mn'
    ).lower().strip()

    # Verifica se está correto comparando o texto ou o índice
    if userReturn_normalizado == resposta_normalizada or userReturn == alternativaCerta:
        acertos += 1
        print("Resposta Correta! \n")
    else:
        print("Resposta errada! \n")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

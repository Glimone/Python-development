#----------FUNDAMENTOS DE FUNÇÃO----------#

# def - Define uma função personalizada.
# estrutura de função: 
#     def function_name(parametros):

# A função tem como padrão um retorno em None, isso significa que você pode deixar o campo de parâmetros vázio: 
#     def function_name():
    
# Além disso, ao usar um parâmetro (O que basicamente faz obrigatório um retorno que não seja None), você pode definir um valor para esse parâmetro ainda dentro da estrutura da função, para caso não seja informado nada, esse valor substitua:
#     def function_name(parametros = "Valor do parâmetro"):

# Em casos de não definir esse valor ainda dentro da estrutura e tiver parâmetro, seus valores devem ser definidos fora da função: 
# def function_name(parametros):
#     c = 12 + parametros
#     return c - Retorno 
# print(function_name(14)) - Valor definido fora da função

# ------- Declaração de Argumento --------#

# Ao declarar os argumentos da função (Valores passados fora da função para a mesma), pode optar em declará-los por posição ou por nomes. 
#     Declaração por posição:
#         def function_name(x,y):
#             a = x + y 
#             return a
#         function_name(10, 12)
    
#     Declaração por nome:
#         def function_name(x, y):
#             a = x + y
#             return a
#         function_name(y = 12 x = 10) #A posição não importa, apenas a declaração do nome,


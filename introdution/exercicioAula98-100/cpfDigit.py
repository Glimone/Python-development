try:
    cpf = input("Informe os 9 dígitos do seu CPF, vamos informar os 2 últimos (sem pontos ou hífens): ")

    if not cpf.isdigit() or len(cpf) != 9:
        raise ValueError("Você deve informar exatamente 9 números! Reinicie o terminal.")

except ValueError as e:
    print(e)
    exit() 
    
cpf_first_list = list(str(cpf))
cpf_first_list.extend(["0", "0"])

i_first = []
first_reverse_list = []
first_list_mult = []

for i,x in enumerate(cpf_first_list):
    x = int(x)
    i_first.append(i)
    first_reverse_list = list(reversed(i_first))
    

for a,b in zip(cpf_first_list, first_reverse_list):
    a = int(a)
    c = a * b 
    first_list_mult.append(c)
    
*essenciais, _, _ = first_list_mult

first_soma = sum(essenciais)

first_number = (first_soma * 10) % 11



#-------------- 2 DIGITO -------------#

cpf_second_list = cpf_first_list
del cpf_second_list[9:]
cpf_second_list.extend([first_number, '0', '0'])

i_second = []
second_reverse_list = []
second_list_mult = []

for i,x in enumerate(cpf_second_list):
    x = int(x)
    i_second.append(i)
    second_reverse_list = list(reversed(i_second))

for a,b in zip(cpf_second_list, second_reverse_list):
    a = int(a)
    c = a * b 
    second_list_mult.append(c)

*essenciais2, _, _ = second_list_mult

second_soma = sum(essenciais2)


second_number = (second_soma * 10) % 11


#------------ Return to client ------------#


if first_number < 9 and second_number < 9:
    print(f"O seu CPF completo é: {cpf}-{first_number}{second_number}!")
elif first_number > 9:
    first_number = 0
    print(f"O seu CPF completo é: {cpf}-{first_number}{second_number}!")
elif second_number > 9:
    second_number = 0
    print(f"O seu CPF completo é: {cpf}-{first_number}{second_number}!") 
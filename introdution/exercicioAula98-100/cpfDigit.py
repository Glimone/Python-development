cpf = input("Informe os 9 digitos do seu CPF, vamos adivinhar o penúltimo:  ")

cpf_list = list(str(cpf))
cpf_list.extend(["0", "0"])

i_list = []
reverse_ind_list = []
c_list = []

for i,x in enumerate(cpf_list):
    x = int(x)
    i_list.append(i)
    reverse_ind_list = list(reversed(i_list))
    

for a,b in zip(cpf_list, reverse_ind_list):
    a = int(a)
    c = a * b 
    c_list.append(c)
    
*essenciais, _, _ = c_list

soma = 0
for i in essenciais:
    soma = soma + i
    
result = (soma * 10) % 11


if result < 9:
    print(f"O penultimo dígito do seu cpf é: {result}")
elif result > 9:
    result = 0
    print(f"O penultimo dígito do seu cpf é: {result}")
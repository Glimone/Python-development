"""
Try - Código que tentará ser executado

Except - Um possível erro no código que tentou em try.(Uma exceção)
"""

n1 = input("Vou dobrar o número que você digitar: ")

try: 
    conv_dec = float(n1)
    dobro = conv_dec * 2
    print(f"O dobro de {n1} é {dobro}. ")
except:
    print("Isso não é um número.")
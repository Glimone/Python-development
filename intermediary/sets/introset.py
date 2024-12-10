#Sets são mutáveis.
#Modos de sets:


#Usando a classe set()
s1 = set('Gabriel')
print(s1)

#Usando {}, que diferente do dict, vocẽ aplica sem keys.
s2 = {'Gabriel', 30}
print(s2)

#Sets eliminam valores duplicados.

s2 = {'Gabriel', 'Gabriel', 10, 20, 20, 30, 30, 50, 40, 40, 50, 60}
print(s2)

#Além disso, set é mutável, porém só aceita valores imutáveis.
tuplex = (1, 2, 3)
s3 = {'Gabriel', tuplex}
print(s3)
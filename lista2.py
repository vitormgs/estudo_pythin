# Obter os números pares de uma lista e somálos
 
num = [34,6,11,19,52,51,83,90]
resultado = 0
 
for x in num:
 
    if x % 2 == 0:
        resultado = resultado + x
        print(x)
 
print("--------------------------------------")
print("O resultado da soma é ", str(resultado))
numero = (input(" Digite qualquer Número para ver a Tabuada: "))
num_1 = int(numero)
 
# A variavel contador começa em 1 e vai até 10
 
contador = 1
 
while contador <= 10:
    resultado = num_1 * contador
    print(str(num_1) + " x " + str(contador) + " = " + str(resultado))
    contador += 1
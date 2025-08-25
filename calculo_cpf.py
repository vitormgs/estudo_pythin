cpf_original = input("Digite o seu cpf sem pontuação: ")
# Criar uma variável para guardar os 9 primeiros digitos
cpf9 = ""
esp = 1
for i in cpf_original:
    if esp > 9:
        break
    esp = esp + 1
    cpf9 = cpf9 + i

print(cpf9)

# Variável que contém os pesos de 10 à 2
peso10 = 10

# Variável que irá guardar os resultados da multiplicação
resultado = 0

for x in cpf9:
    resultado = resultado + (int(x) * peso10)
    peso10 = peso10 - 1

# Variável para guardar o resto da divisão
resto = 0
resto = resultado % 11
cpf10 = cpf9
if resto < 2:
    cpf10 = cpf10 + "0"
else:
    cpf10 = cpf10 + str(11-resto)

# Variável com peso 11, que irá até 2
peso11 = 11

#  Zerar a variável resultado para o novo cálculo
resultado = 0

for x in cpf9:
    resultado = resultado + (int(x) * peso11)
    peso11 = peso11 - 1

resto = 0    
resto = resultado % 11
cpf_calculado = cpf10

if resto <2:
    cpf_calculado = cpf_calculado + str(11-resto)

if cpf_original==cpf_calculado:
    print("CPF Correto!")
else:
    print("CPF Inválido!")
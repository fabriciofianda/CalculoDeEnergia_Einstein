import math

# Pedindo as variáveis ao usuário
massa = float(input("Digite a massa da partícula em kg: "))
velocidade = float(input("Digite a velocidade da partícula em m/s: "))

# Calculando o momento da partícula
momentum = massa * velocidade

# Calculando a energia total da partícula
energia = math.sqrt((massa * (3*10**8)**2)**2 + momentum**2)

# Imprimindo o resultado
print("A energia total da partícula é de: ", energia, " J")
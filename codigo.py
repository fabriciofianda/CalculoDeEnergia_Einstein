import math

# Pedindo as variáveis ao usuário
mass = float(input("Digite a massa da partícula em kg: "))
velocity = float(input("Digite a velocidade da partícula em m/s: "))

# Calculando o momento da partícula
momentum = mass * velocity

# Calculando a energia total da partícula
energy = math.sqrt((mass * (3*10**8)**2)**2 + momentum**2)

# Imprimindo o resultado
print("A energia total da partícula é de: ", energy, " J")
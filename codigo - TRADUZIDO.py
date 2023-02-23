import math

massa = float(input("Digite a massa da partícula em kg: "))
velocidade = float(input("Digite a velocidade da partícula em m/s: "))

momento = massa * velocidade

energia = math.sqrt((massa * (3*10**8)**2)**2 + momento**2)
print("A energia total da partícula é de: ", energia, " J")
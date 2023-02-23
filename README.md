Código em Python simples para Cálculo de Energia com base na equação de Einstein;

Gerado inteiramente por chat gpt

descrição da resposta:

Sim, a equação reduzida E=mc² é uma simplificação da equação completa E² = (mc²)² + (pc)². No entanto, essa equação completa é importante para levar em consideração o momento da partícula (pc), além da sua massa (mc²), ao calcular a energia total (E) da partícula.

Segue abaixo um exemplo de programa em Python que pede as variáveis e executa a solução do cálculo de energia de Einstein utilizando a equação completa:

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

Nesse exemplo, a velocidade da partícula é fornecida em metros por segundo (m/s) e a massa em quilogramas (kg). A solução é obtida utilizando a biblioteca de matemática do Python para calcular a raiz quadrada (math.sqrt).
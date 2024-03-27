import math

def calcular_posicao_EF_robo(theta1, theta2, grad0rad1): 
    #Entradas:
    #   theta1 (float): Ângulo da primeira junta em radianos.
    #   theta2 (float): Ângulo da segunda junta em radianos.
    #   grad0rad1: seleção de ângulo em graus (0) ou radianos (1)
    
    #Saída:
    #    posEF[float, float]: Coordenadas X_u e Y_u efetuador final (em cm).
    
    #Raises:
    #    ValueError: Se os ângulos estão no intervalo [0, 2*pi].
    
    # Comprimentos dos braços
    L1 = 20  # cm
    L2 = 15  # cm
    if grad0rad1 == 0:
        theta1_rad = theta1*math.pi/180
        theta2_rad = theta2*math.pi/180
    if grad0rad1 == 1:
        theta1_rad = theta1
        theta2_rad = theta2
    
    # Verifica se os ângulos estão no intervalo [0, 2*pi]
    if not (0 <= theta1_rad <= 2*math.pi) or not (0 <= theta2_rad <= 2*math.pi):
        raise ValueError("Os ângulos devem estar no intervalo de 0 a 2*pi(0,360 graus)].")
    
    # Calcula das coordenadas X_u e Y_u
    X_u = L1 * math.cos(theta1_rad) + L2 * math.cos(theta1_rad + theta2_rad)
    Y_u = L1 * math.sin(theta1_rad) + L2 * math.sin(theta1_rad + theta2_rad)
    
    # Arredondamento 1 casa decimal
    X_u = round(X_u, 1)
    Y_u = round(Y_u, 1)
    return X_u, Y_u

# Exemplo de uso
theta1_exemplo = 30 #*math.pi  
theta2_exemplo = 30 #*math.pi 
try:
    posicao_efetuador = calcular_posicao_EF_robo(theta1_exemplo, theta2_exemplo, 0)
    print(f"Posição do efetuador final: X_u = {posicao_efetuador[0]} cm, Y_u = {posicao_efetuador[1]} cm")
except ValueError as e:
    print("Erro:", str(e))
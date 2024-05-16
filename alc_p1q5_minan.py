import numpy as np

def inversa_eliminacao(matriz):
    #Calcula a inversa de uma matriz quadrada utilizando o método de eliminação.
    
    #Entrada:
    #A (np.array): Matriz quadrada que queremos inverter.
    
    #Saída:
    #np.array: Matriz inversa de A.
    
    #Raise:
    #ValueError: Se a matriz A tiver elementos nulos na diagonal principal, não for quadrada ou não puder realizar o pivoteamento.
    
   # Verifica se A é uma matriz quadrada
    n = len(matriz)  # Número de linhas
    if any(len(row) != n for row in matriz):
        raise ValueError("A matriz deve ser quadrada.")
    
    # Verifica elementos nulos na diagonal principal
    for i in range(n):
        if matriz[i, i] == 0:
            raise ValueError("A matriz possui um ou mais elementos nulos na diagonal principal. Utilize outra técnica para obtenção da inversa.")
    
    # Matriz identidade de mesma dimensão
    I = np.eye(n)
    
    # Matriz aumentada iniciada com zeros
    matriz_aumentada = np.zeros((n, 2 * n))
    
    # Copia da Matriz para o lado esquerdo e Identidade para o lado direito
    for i in range(n):
        for j in range(n):
            matriz_aumentada[i, j] = matriz[i, j]
            matriz_aumentada[i, j + n] = I[i, j]
    
    # Método de eliminação 
    for i in range(n):
        # Pivoteamento
        pivo = matriz_aumentada[i, i]
        if pivo == 0:
            for k in range(i + 1, n):
                if matriz_aumentada[k][i] != 0:
                    matriz_aumentada[[i, k]] = matriz_aumentada[[k, i]]
                    pivo = matriz_aumentada[i][i]
                    break
            else:
                raise ValueError("A matriz não admite inversa")
        
        matriz_aumentada[i] = matriz_aumentada[i] / pivo
        
        for j in range(n):
            if i != j:
                matriz_aumentada[j] = matriz_aumentada[j] - matriz_aumentada[j, i] * matriz_aumentada[i]
                
                
    
    # Cópia da matriz inversa, parte direita da matriz aumentada matriz_aumentada
    matriz_inv = matriz_aumentada[:, n:]
    
    return matriz_inv


# Exemplo de uso:
A4 = np.array([[1, 2, 3, 4], 
              [6, 3, 8, 9],
              [6, 3, 1, 5],
              [3, 4, 7, 6]])
A3 = np.array([[7, 1, 5], 
              [8, 6, 2],
              [3, 2, 7]])
A2 = np.array([[1, 1], 
              [3, 4 ]])

try:
    print("Matriz Entrada:\n", A3)
    A_inv = inversa_eliminacao(A3)
    print("\nMatriz Inversa:\n", A_inv)
except ValueError as e:
    print(e)

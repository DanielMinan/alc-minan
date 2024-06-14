import numpy as np
import scipy as sp

def ludecomp(A):
    """
    Função de Decomposição LU com pivoteamento parcial de uma matriz quadrada A.
    
    Entrada:
    Matriz A (numpy.ndarray): 
    
    Returns:
    Matriz P (numpy.ndarray): Permutação.
    Matriz L (numpy.ndarray): Triangular Inferior
    Matriz U (numpy.ndarray): Triangular Superior
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("A matriz de entrada deve ser quadrada.")

    n = A.shape[0]
    L = np.eye(n)  # Inicializa L como matriz identidade
    P = np.eye(n)  # Inicializa P como matriz identidade
    U = A.copy()   # Copia A para U
    eps=1e-7       # Valor mínimo de pivô considerado não nulo
    
    for i in range(n-1):
        # Encontra o índice do pivô
        imax= np.argmax(np.abs(U[i:n, i]))
        pivo_index =  imax + i

        if np.abs(U[pivo_index, i]) < eps:
            break
        
        if pivo_index != i:
            # Troca as linhas i e pivo_index de U
            U[[i, pivo_index], i:n] = U[[pivo_index, i], i:n]
            # Troca as linhas i e pivo_index de P
            P[[i, pivo_index], :] = P[[pivo_index, i], :]
            # Troca as linhas i e pivo_index de L
            L[[i, pivo_index], :i] = L[[pivo_index, i], :i]
        
        # Calcula os faotres de multiplicação
        L[i+1:n, i] = U[i+1:n, i] / U[i, i]
        # Atualiza a submatriz de U
        for j in range(i+1, n):
            for k in range(i+1, n):
                U[j, k] = U[j, k] - L[j, i] * U[i, k]
        # Define os elementos abaixo da diagonal principal como zero
        U[i+1:n, i] = 0
    
    return P, L, U


#Exemplo de uso com 3 matrizes
A1 = np.array([[1, 2 , 3], [2, 5, 4], [3, 5, 4]], dtype=float)
A2 = np.array([[-1, -1 , 0, 1], [-1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 1, 0]], dtype=float)
A3 = np.array([[2, 1 , 3, 5], [1, 6, -1, 2], [3, 7, 2, 7], [5, 19, 0, 11]], dtype=float) #singular

try:
    #Teste da Função ludecomp e linalg.lu
    P1, L1, U1= ludecomp(A1)      #SUBSTITUIR POR A1, A2 OU A3
    P2, L2, U2 = sp.linalg.lu(A1) #SUBSTITUIR POR A1, A2 OU A3
    print("\nDecomposição LU da Matriz A1:")
    print("L1=\n", L1, "\nL2=\n", L2)
    print("\nU1=\n", np.round(U1,6), "\nU2=\n", np.round(U2,6))
    print("\nP1=\n", P1, "\nP2=\n", P2)
    
    P1, L1, U1= ludecomp(A2)      #SUBSTITUIR POR A1, A2 OU A3
    P2, L2, U2 = sp.linalg.lu(A2) #SUBSTITUIR POR A1, A2 OU A3
    print("\nDecomposição LU da Matriz A2:")
    print("L1=\n", L1, "\nL2=\n", L2)
    print("\nU1=\n", np.round(U1,6), "\nU2=\n", np.round(U2,6))
    print("\nP1=\n", P1, "\nP2=\n", P2)
    
    P1, L1, U1= ludecomp(A3)      #SUBSTITUIR POR A1, A2 OU A3
    P2, L2, U2 = sp.linalg.lu(A3) #SUBSTITUIR POR A1, A2 OU A3
    print("\nDecomposição LU da Matriz A3:")
    print("L1=\n", L1, "\nL2=\n", L2)
    print("\nU1=\n", np.round(U1,6), "\nU2=\n", np.round(U2,6))
    print("\nP1=\n", P1, "\nP2=\n", P2)
except ValueError as e:
    print(e)
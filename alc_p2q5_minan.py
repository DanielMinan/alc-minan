import numpy as np

def alc_cholesky(A):
    """
    decomposição de cholesky
    Entrada
    A : Matriz quadrada positiva definida
    
    Saída
    R : Matriz triangular superior tal que R.T @ R = A
    """
    A = np.array(A)
    m, n = A.shape
    if m != n:
        raise ValueError('A matriz não é quadrada')

    R = np.zeros((n, n), dtype=float)
    for i in range(n):
        # Cálculo soma de quadrados
        somaq = 0
        for k in range(i):
            somaq += R[k, i]**2
        
        tmp = A[i, i] - somaq
        if tmp <= 0:
              raise ValueError('A matriz de entrada não é positiva definida, impossibilidade de realizar a decomposição de Cholesky')
            
        #Cálculo da diagonal principal 
        R[i, i] = tmp**0.5
        
        # Cálculo dos elementos acima da diagonal
        for j in range(i + 1, n):
            somap = 0
            for k in range(i):
                somap += R[k, i] * R[k, j]
            
            R[i, j] = (A[i, j] - somap) / R[i, i]
    
    return R

# Teste da função
try:
    A = np.array([[23, 12, -16],
              [12, 55, -23],
              [-13, -23, 98]])
    R = alc_cholesky(A)
    print("R = \n",R)
    #print("A = \n", A)
    print("R.T @ R = \n",  R.T @ R )
except ValueError as e:
    print(e)

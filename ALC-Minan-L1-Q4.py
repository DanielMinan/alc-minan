import numpy as np

# Função
def algo_subst_regressiva(matriz_tri_sup, vetor_col):
    n = len(matriz_tri_sup)
    #início solução
    sol = np.zeros(n)
    # Verificação se a matriz é quadrada
    for i in range(n):
        if len(matriz_tri_sup[i]) != n:
            raise ValueError("A matriz não é quadrada.")
    # Verificação se a matriz é triangular superior
    for j in range(n):
        for i in range(j + 1, n):
            if matriz_tri_sup[i][j] != 0:
                raise ValueError("A matriz não é triangular superior")
    # Verificação se a matriz é compatível com o vetor coluna
    if len(vetor_col) != n:
        raise ValueError("O vetor coluna não é compatível a matriz.")
    # Verificação se há elemento nulo na diagonal da matriz triangular superior
    for i in range(n-1, -1, -1):
        if matriz_tri_sup[i][i] == 0:
            raise ValueError("Elemento nulo na diagonal da matriz triangular superior.")
        soma = np.dot(matriz_tri_sup[i][i+1:], sol[i+1:])
        sol[i] = (vetor_col[i] - soma) / matriz_tri_sup[i][i]
    return sol

# Exemplo de uso
matriz1 = np.array([
    [1, 2, -1, 5, -2], 
    [0, 5, 3, 4, -4], 
    [0, 0, 4, 3, -3], 
    [0, 0, 0, 3, 2],
    [0, 0, 0, 0, 7], ])
vetor1= np.array([8, 5, 6, 3, 13])

# Tratamento de Exceção
try:
    solucao = algo_subst_regressiva(matriz1, vetor1)
    print("Solução do Sistema:", solucao)
except ValueError as err:
    print("Erro:", str(err))
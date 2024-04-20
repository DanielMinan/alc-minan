import numpy as np

def is_orthogonal_by_definition(matriz_d):
    # Verificação se a matriz é quadrada
    linhas, colunas = matriz_d.shape
    if linhas != colunas:
        print("A matriz não é quadrada")
        return False
    
    # Cálculo da matriz transposta
    matriz_transposta = np.transpose(matriz_d)
    
    # Cálculo da multiplicação da Matriz transposta pela matriz
    produto = np.dot(matriz_transposta, matriz_d)
    
    # Matriz identidade para comparação
    matriz_identidade = np.eye(linhas)
    
    # Erro mínimo entre os elementos da matriz resultante e os elementos da matriz identidade
    erromax_d = 1e-5
    
    # Comparação entre a matriz resultante e a matriz identidade
    for i in range(linhas):
        for j in range(colunas):
            if abs(produto[i, j] - matriz_identidade[i, j]) > erromax_d:
                return False
    
    # Retorno booleano True se a matriz é ortogonal pela definição
    return True


def is_orthogonal_by_vectors(matriz_v):
    # Verificação se a matriz é quadrada
    linhas, colunas = matriz_v.shape
    if linhas != colunas:
        print("A matriz não é quadrada")
        return False
    
    # Erro máximo para produto interno =~ 0 e norma =~ 1
    erromax_v = 1e-5
    
    # Cálculo e verificação da norma do vetor coluna
    for i in range(colunas):
        vetcol = matriz_v[:, i]
        norma = np.linalg.norm(vetcol)
        if abs(norma - 1.0) > erromax_v:
            return False
    
    # Cálculo e verificação do produto interno igual a 0 (vetores colunas ortogonais)
    for i in range(colunas):
        for j in range(i + 1, colunas):
            produto_interno = np.dot(matriz_v[:, i], matriz_v[:, j])
            if abs(produto_interno - 0.0) > erromax_v:
                return False
    
    # Retorno booleano True se a matriz é ortogonal pelos vetores colunas
    return True




matriz_6_38_P1= np.array([[-0.40825, 0.43644, 0.80178], 
                          [-0.8165, 0.21822, -0.53452], 
                          [-0.40825, -0.87287, 0.26726]])

matriz_6_38_P2 = np.array([[-0.51450, 0.48507, 0.70711], 
                          [-0.68599, -0.72761, 0.0000], 
                          [0.51450, -0.48507, 0.70711]])

matriz_6_39_P1 = np.array([[-0.58835, 0.70206, 0.40119], 
                          [-0.78446, -0.37524, -0.49377], 
                          [-0.19612, -0.60523, 0.77152]])

matriz_6_39_P2 = np.array([[-0.47624, -0.4264, 0.30151], 
                          [0.087932, 0.86603, -0.40825], 
                          [-0.87491, -0.26112, 0.86164]])

# Questão 6.38 a) P1
if is_orthogonal_by_definition(matriz_6_38_P1):
    print("A matriz 6.38 P1 é ortogonal pela definição")
else:
    print("A matriz 6.38 P1 não é ortogonal pela definição")
if is_orthogonal_by_vectors(matriz_6_38_P1):
    print("A matriz 6.38 P1 é ortogonal pelo vetores colunas")
else:
    print("A matriz 6.38 P1 não é ortogonal pelos vetores colunas")
 
# Questão 6.38 b) P2 
if is_orthogonal_by_definition(matriz_6_38_P2):
    print("A matriz 6.38 P2 é ortogonal pela definição")
else:
    print("A matriz 6.38 P2 não é ortogonal pela definição")
if is_orthogonal_by_vectors(matriz_6_38_P2):
    print("A matriz 6.38 P2 é ortogonal pelo vetores colunas")
else:
    print("A matriz 6.38 P2 não é ortogonal pelos vetores colunas")

# Questão 6.39 a) P1 
if is_orthogonal_by_definition(matriz_6_39_P1):
    print("A matriz 6.39 P1 é ortogonal pela definição")
else:
    print("A matriz 6.39 P1 não é ortogonal pela definição")
if is_orthogonal_by_vectors(matriz_6_39_P1):
    print("A matriz 6.39 P1 é ortogonal pelo vetores colunas")
else:
    print("A matriz 6.39 P1 não é ortogonal pelos vetores colunas")

# Questão 6.39 b) P2
if is_orthogonal_by_definition(matriz_6_39_P2):
    print("A matriz 6.39 P2 é ortogonal pela definição")
else:
    print("A matriz 6.39 P2 não é ortogonal pela definição")
if is_orthogonal_by_vectors(matriz_6_39_P2):
    print("A matriz 6.39 P2 é ortogonal pelo vetores colunas")
else:
    print("A matriz 6.39 P2 não é ortogonal pelos vetores colunas")
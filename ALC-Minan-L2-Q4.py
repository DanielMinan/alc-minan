import numpy as np

def compara_posto_norma(n_valores):
    for n in n_valores:
        # Geração dos vetores u e v
        u = np.random.rand(n, 1)
        v = np.random.rand(n, 1)
        
        # Cálculo da matriz A = uv^T
        A = np.dot(u, v.T)
        
        # Cálculo do posto da matriz A = uv^T
        posto_A = np.linalg.matrix_rank(A)
        
        # Cálculo do produto das normas 2 dos vetores u e v
        norma2_u = np.linalg.norm(u)
        norma2_v = np.linalg.norm(v)
        produto_normas = norma2_u * norma2_v
        
        # Cálculo da norma 2 da matriz A = uv^T
        norm_uv_T = np.linalg.norm(A)
        
        # Resultados
        print(f"n = {n}:")
        print(f"1) Posto da matriz A (uv^T): {posto_A}")
        print(f"2) Produto da norma 2 de u e norma 2 de v: {produto_normas}")
        print(f"3) Norma 2 da matriz (uv^T): {norm_uv_T}")
        print(f"4) Diferença: {norm_uv_T - produto_normas}\n")

# Valores de n para simulação
valores_n = [5, 15, 25]

# Calculate metrics
compara_posto_norma(valores_n)

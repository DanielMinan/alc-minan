import numpy as np
import random as rd

def produto_vetorial(v1, v2):
    # Calcula o produto vetorial de dois vetores v1 e v2.

    # Parâmetros:
    # v1: Primeiro vetor de comprimento 3.
    # v2: Segundo vetor de comprimento 3.

    # Saída:
    # w: O produto vetorial de v1 e v2.
    
    # Verifica se os vetores possuem a mesma dimensão
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Ambos os vetores devem ter comprimento 3.")
    
    # Calcula o produto vetorial manualmente
    w = [   v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]]
    
    return w

# Exemplo de uso
u = [rd.randint(-20,20), rd.randint(-20,20), rd.randint(-20,20)]
v = [rd.randint(-20,20), rd.randint(-20,20), rd.randint(-20,20)]
print("u =", u, "\nv =", v, "\nProduto vetorial u x v =" , produto_vetorial(u, v))
# Lista #3 Questão 2
print("\nLista 3 Questão 2:")
print("u =", u, "\nv =", v)
print("u x v =" , produto_vetorial(u, v))
print("v x u =" , produto_vetorial(v, u))
print("<u x v, u> =" , np.inner(produto_vetorial(u, v), u))
print("<v x u, v> =" , np.inner(produto_vetorial(v, u), v))

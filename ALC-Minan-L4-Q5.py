import numpy as np
import scipy as sp

def modqrgrsch(matEntr):
    m, n = matEntr.shape
    matriz = np.zeros((m, n), dtype=float)
    Q = np.zeros((m, n), dtype=float)
    R = np.zeros((n, n), dtype=float)
    matriz = matEntr.copy()

    for i in range(n):
        Q[:, i] = matriz[:, i]
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], Q[:, i])
            Q[:, i] -= R[j, i] * Q[:, j]
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] /= R[i, i]

    return Q, R


# Exemplo de uso:
A = np.array([[1.0, 9, 0, 5, 3, 2],
              [-6, 3, 8, 2, -8, 0],
              [3, 15, 23, 2, 1, 7],
              [3, 57, 35, 1, 7, 9],
              [3, 5, 6, 15, 55, 2],
              [33, 7, 5, 3, 5, 7]
              ])\


# Realize a decomposição QR usando Gram-Schmidt modificado
print("////////// FUNÇÃO modqrgrsch(A) //////////")
Q1, R1 = modqrgrsch(A)
print("Matriz A:")
print(A)
print("\nMatriz Q1 (ortogonal):")
print(Q1.round(4))
print("\nMatriz R1 (triangular superior):")
print(R1.round(4))

# Verifique a decomposição QR: A deve ser aproximadamente igual a Q @ R
Aqr1 = np.dot(Q1, R1)
print("\nVerificação A=Q1R1 [round(10)]:\n", Aqr1.round(10))
print("Norma de A-Q1R1: ", np.linalg.norm(A-Aqr1))

print("\n\n////////// FUNÇÃO numpy.linalg.qr(A) //////////")
Q2, R2 = np.linalg.qr(A)
print("\nMatriz Q2 (ortogonal):")
print(Q2.round(4))
print("\nMatriz R2 (triangular superior):")
print(R2.round(4))

#Verifique a decomposição QR: A deve ser aproximadamente igual a Q @ R
Aqr2 = np.dot(Q2, R2)
print("\nVerificação A=Q2R2 [round(10)]:\n", Aqr2.round(10))
print("Norma de A-Q2R2: ", np.linalg.norm(A-Aqr2))

print("\n\n////////// FUNÇÃO scipy.linalg.qr(A) //////////")
Q3, R3 = sp.linalg.qr(A)
print("\nMatriz Q3 (ortogonal):")
print(Q3.round(4))
print("\nMatriz R3 (triangular superior):")
print(R3.round(4))

#Verifique a decomposição QR: A deve ser aproximadamente igual a Q @ R
Aqr3 = Q3 @ R3
print("\nVerificação A=Q3R3 [round(10)]:\n", Aqr3.round(10))
print("Norma de A-Q3R3: ", sp.linalg.norm(A-Aqr3))

print("\n14.15, a base ortonormal das colunas da matriz A:\b")
print("e_1 = ", Q1.round(4)[:,0].T,"^T")
print("e_2 = ", Q1.round(4)[:,1].T,"^T")
print("e_3 = ", Q1.round(4)[:,2].T,"^T")
print("e_4 = ", Q1.round(4)[:,3].T,"^T")
print("e_5 = ", Q1.round(4)[:,4].T,"^T")
print("e_6 = ", Q1.round(4)[:,5].T,"^T")
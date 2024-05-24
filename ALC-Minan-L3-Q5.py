import numpy as np
import matplotlib.pyplot as plt

def wilkinson_bidiagonal(n):
    # Cria matriz Wilkinson bidiagonal ordem n (int).
    # Retorno Matriz Wilkinson Bidiagonal W (numpy.array)
    
    # Inicialização da matriz W n x n com elementos zero
    W = np.zeros((n, n))
    
    # Substituição dos elementos da diagonal principal
    for i in range(n):
        W[i, i] = n-i
    
    # Substituição dos elementos da diagonal acima da principal
    for i in range(0, n-1):
        W[i, i + 1] = n
    
    return W

# Exemplo de Uso:
n = 5
matrizW = wilkinson_bidiagonal(n)
print("Condicionamento matrizW ordem 5 = ", np.linalg.cond(matrizW))

#Cálculo do condicionamento das matrizes Wilkinson de ordem 1 a 15
nCond = 15
vetorCond = np.zeros(nCond)
for k in range(0, nCond):
        vetorCond[k] = np.linalg.cond(wilkinson_bidiagonal(k+1))

print("\nCondicionamento ordem 1 a 15 = \n", vetorCond)

#Eixo x
ordem = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Criando a figura e os subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Plotagem em escala normal
ax1.scatter(ordem, vetorCond, color='blue', edgecolor='k', s=100, alpha=0.75)
ax1.set_title('Gráfico Condicionamento', fontsize=12)
ax1.set_xlabel('Ordem')
ax1.set_ylabel('Condicionamento')
ax1.grid(True, linestyle='--', alpha=0.7)

# Plotagem em escala logarítmica
ax2.scatter(ordem, vetorCond, color='red', edgecolor='k', s=100, alpha=0.75)
ax2.set_yscale('log')
ax2.set_title('Gráfico Condicionamento Esc Log', fontsize=12)
ax2.set_xlabel('Ordem')
ax2.set_ylabel('Condicionamento')
ax2.grid(True, which='both', linestyle='--', alpha=0.7)

# Criação da Matriz A (20x20) Wilkinson Bidiagonal
A = wilkinson_bidiagonal(20)
# Cálculo autovalores A
autovalores = np.linalg.eigvals(A)
print("\nAutovalores de A = ", autovalores)

# Criação da Matriz Aperturb com perturbação em A(20,1) = 10^-10
Aperturb = A
Aperturb[19][0] = np.power(10.0, -10) 
# Cálculo de autovalores Aperturb
autovaloresP = np.linalg.eigvals(Aperturb)
print("\nAutovalores de Aperturb = ",autovaloresP)

# Plotando os autovalores de A
ax3.scatter(autovalores.real, autovalores.imag, color='green')
ax3.axhline(0, color='black', linewidth=0.5)
ax3.axvline(0, color='black', linewidth=0.5)
ax3.grid(color='gray', linestyle='--', linewidth=0.5)
ax3.set_title('Autovalores de A')
ax3.set_xlabel('Parte Real')
ax3.set_ylabel('Parte Imaginária')
ax3.set_xlim(-1, 21)
ax3.set_ylim(-5, 5)

# # Plotando os autovalores de Aperturb
ax4.scatter(autovaloresP.real, autovaloresP.imag, color='orange')
ax4.axhline(0, color='black', linewidth=0.5)
ax4.axvline(0, color='black', linewidth=0.5)
ax4.grid(color='gray', linestyle='--', linewidth=0.5)
ax4.set_title('Autovalores de Aperturb')
ax4.set_xlabel('Parte Real')
ax4.set_ylabel('Parte Imaginária')
ax4.set_xlim(-1, 21)
ax4.set_ylim(-5, 5)

# Visualização dos gráficos
plt.tight_layout()
plt.show()
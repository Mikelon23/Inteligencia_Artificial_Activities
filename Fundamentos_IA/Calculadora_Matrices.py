def mostrar_matriz(matriz, nombre="Matriz"):
    print(f"\n{nombre}:")
    for fila in matriz:
        print(fila)

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

def main():
    # Ejemplo de uso
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    mostrar_matriz(A, "Matriz A")
    mostrar_matriz(B, "Matriz B")

    mostrar_matriz(sumar_matrices(A, B), "A + B")
    mostrar_matriz(restar_matrices(A, B), "A - B")
    mostrar_matriz(multiplicar_matrices(A, B), "A x B")

if __name__ == "__main__":
    main()

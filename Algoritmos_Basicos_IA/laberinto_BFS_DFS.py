# Algoritmos de búsqueda en laberintos (BFS y DFS)
# Proyecto práctico del Mes 2

from collections import deque

# Representamos el laberinto como una lista de listas
# 0 = camino libre, 1 = muro
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
inicio = (0, 0)  # fila, columna
meta = (4, 4)

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

def vecinos(nodo):
    fila, col = nodo
    for df, dc in movimientos:
        nf, nc = fila + df, col + dc
        if 0 <= nf < len(laberinto) and 0 <= nc < len(laberinto[0]):
            if laberinto[nf][nc] == 0:
                yield (nf, nc)

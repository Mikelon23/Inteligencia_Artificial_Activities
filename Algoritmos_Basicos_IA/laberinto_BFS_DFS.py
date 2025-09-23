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
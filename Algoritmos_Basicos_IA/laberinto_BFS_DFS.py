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

def bfs(inicio, meta):
    cola = deque([inicio])
    visitados = {inicio: None}
    
    while cola:
        nodo = cola.popleft()
        if nodo == meta:
            break
        for v in vecinos(nodo):
            if v not in visitados:
                visitados[v] = nodo
                cola.append(v)
    
    # reconstruir camino
    camino = []
    nodo = meta
    while nodo:
        camino.append(nodo)
        nodo = visitados.get(nodo)
    return camino[::-1]
def dfs(inicio, meta):
    pila = [inicio]
    visitados = {inicio: None}
    
    while pila:
        nodo = pila.pop()
        if nodo == meta:
            break
        for v in vecinos(nodo):
            if v not in visitados:
                visitados[v] = nodo
                pila.append(v)
    
    # reconstruir camino
    camino = []
    nodo = meta
    while nodo:
        camino.append(nodo)
        nodo = visitados.get(nodo)
    return camino[::-1]
if __name__ == "__main__":
    print("Camino BFS:", bfs(inicio, meta))
    print("Camino DFS:", dfs(inicio, meta))
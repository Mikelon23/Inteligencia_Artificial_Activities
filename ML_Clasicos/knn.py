from sklearn.neighbors import KNeighborsClassifier

# Datos: [peso (g), textura (0 = rugosa, 1 = suave)]
X = [
    [150, 0],  # Naranja
    [170, 0],  # Naranja
    [140, 1],  # Manzana
    [130, 1],  # Manzana
]

y = ["naranja", "naranja", "manzana", "manzana"]

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# Predecir
nueva_fruta = [[160, 0]]
print("Clasificación para fruta nueva:", modelo.predict(nueva_fruta))

from sklearn import svm
import matplotlib.pyplot as plt

# Datos: coordenadas X, Y
X = [[1, 2], [2, 3], [3, 3], [8, 8], [9, 9], [10, 10]]
y = [0, 0, 0, 1, 1, 1]  # Grupo 0 y grupo 1

modelo = svm.SVC(kernel='linear')
modelo.fit(X, y)

# Predecir
nuevo_punto = [[4, 4]]
print("Clasificación para el punto (4,4):", modelo.predict(nuevo_punto))

# Visualización básica
plt.scatter([p[0] for p in X], [p[1] for p in X], c=y, cmap="coolwarm")
plt.scatter(4, 4, c="green", marker="x", s=200, label="Nuevo punto")
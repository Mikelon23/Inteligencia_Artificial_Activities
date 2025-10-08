from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Datos: [horas estudio, horas sueño]
X = [
    [2, 6],   # Reprueba
    [4, 6],   # Aprueba
    [6, 7],   # Aprueba
    [1, 5],   # Reprueba
]

y = ["reprueba", "aprueba", "aprueba", "reprueba"]

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Predecir
nuevo_estudiante = [[3, 6]]
print("Resultado:", modelo.predict(nuevo_estudiante))

# Visualizar árbol
plt.figure(figsize=(6,4))
tree.plot_tree(modelo, feature_names=["Horas estudio", "Horas sueño"], class_names=["reprueba", "aprueba"], filled=True)
plt.show()
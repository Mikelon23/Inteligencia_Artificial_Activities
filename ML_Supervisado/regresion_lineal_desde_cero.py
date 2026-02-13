import numpy as np


class RegresionLinealGD:
    """Regresión lineal simple entrenada con descenso de gradiente."""

    def __init__(self, tasa_aprendizaje: float = 0.0001, epocas: int = 5000):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.peso = 0.0
        self.sesgo = 0.0
        self.historial_error = []

    def entrenar(self, x: np.ndarray, y: np.ndarray) -> None:
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        n = len(x)

        for _ in range(self.epocas):
            predicciones = self.peso * x + self.sesgo
            error = predicciones - y

            gradiente_peso = (2 / n) * np.dot(error, x)
            gradiente_sesgo = (2 / n) * np.sum(error)

            self.peso -= self.tasa_aprendizaje * gradiente_peso
            self.sesgo -= self.tasa_aprendizaje * gradiente_sesgo

            mse = np.mean(error ** 2)
            self.historial_error.append(mse)

    def predecir(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=float)
        return self.peso * x + self.sesgo


if __name__ == "__main__":
    # Datos de ejemplo: metros cuadrados y precio (en miles de dólares)
    metros_cuadrados = np.array([50, 60, 80, 100, 120], dtype=float)
    precios = np.array([150, 180, 220, 260, 300], dtype=float)

    modelo = RegresionLinealGD(tasa_aprendizaje=0.0001, epocas=20000)
    modelo.entrenar(metros_cuadrados, precios)

    casa_nueva = np.array([90], dtype=float)
    prediccion = modelo.predecir(casa_nueva)[0]

    print(f"Peso (m): {modelo.peso:.4f}")
    print(f"Sesgo (b): {modelo.sesgo:.4f}")
    print(f"Precio estimado para una casa de 90 m²: {prediccion:.2f} mil dólares")

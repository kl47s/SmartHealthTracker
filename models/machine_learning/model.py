from sklearn.linear_model import LinearRegression
import numpy as np

class HealthModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Пример использования
if __name__ == '__main__':
    # Данные для обучения
    X = np.array([[1, 5], [2, 6], [3, 7]])
    y = np.array([1, 2, 3])
    
    health_model = HealthModel()
    health_model.train(X, y)
    print(health_model.predict([[4, 8]]))

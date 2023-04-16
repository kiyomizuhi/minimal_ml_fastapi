import typing as T


class InCircleClassifier:
    def __init__(self, r=1.0):
        self.r = r

    def predict(self, X: T.List[float]) -> bool:
        radius = X[0] ** 2 + X[1] ** 2
        return radius <= self.r

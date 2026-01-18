import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future_popularity(stars):
    X = np.array(range(len(stars))).reshape(-1, 1)
    y = np.array(stars)

    model = LinearRegression()
    model.fit(X, y)

    future = model.predict([[len(stars)]])
    return int(future[0])

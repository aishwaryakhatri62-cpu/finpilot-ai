import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_cash_flow(data):
    df = pd.DataFrame(data, columns=["month", "amount"])
    X = df[["month"]]
    y = df["amount"]
    model = LinearRegression()
    model.fit(X, y)
    future = np.array([[len(data)+1],[len(data)+2],[len(data)+3]])
    prediction = model.predict(future)
    return prediction.tolist()

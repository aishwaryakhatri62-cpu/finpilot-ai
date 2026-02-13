import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomaly(amounts):
    df = pd.DataFrame(amounts, columns=["amount"])
    model = IsolationForest(contamination=0.2)
    df["anomaly"] = model.fit_predict(df)
    return df[df["anomaly"] == -1]["amount"].tolist()

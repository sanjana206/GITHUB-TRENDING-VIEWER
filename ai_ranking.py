import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def rank_repositories(repo_list):
    df = pd.DataFrame(repo_list)

    scaler = MinMaxScaler()
    df["Popularity_Score"] = scaler.fit_transform(df[["Stars"]])

    df = df.sort_values(by="Popularity_Score", ascending=False)
    return df

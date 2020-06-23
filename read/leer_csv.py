import pandas as pd
def leer_csv (csv):
    df = pd.read_csv(csv, sep=";", decimal=",")
    df_sin_na = df.dropna()
    return df_sin_na
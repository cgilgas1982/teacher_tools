
def leer_columna (df, columna):
    columna =  df[columna].astype(float).values
    return columna
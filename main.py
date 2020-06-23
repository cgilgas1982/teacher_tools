import read.leer_csv as le
import read.leer_columna as lc
import operaciones.calc_media as cm



def main (csv, columna):
    df_sin_na = le.leer_csv(csv)
    columna = lc.leer_columna(df_sin_na, columna)
    media = cm.calc_media(columna)
    return media

media_columna = main("/Users/mariacarmengilgas/Desktop/NOTAS_3EV.csv", "2EV")
print (media_columna)





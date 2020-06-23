
import statistics as st

def calc_media (columna):
    media= st.mean(columna)
    round_media= round(media, 2)
    return (round_media)
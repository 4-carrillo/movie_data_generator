from numpy.random import (
    randint
)
import configparser

config = configparser.ConfigParser()
config.read(r'config.ini')


BRONZEPATH=config['DATAPATH']['BRONZEPATH']

COL_LIST=[
    'userid',
    'age',
    'title',
    'genres',
    'rating',
    'commentary',
    'date'
]

REGISTRES=randint(8000, 9000, size=1)[0]

DATELOW = "1/1/2015 1:30 PM"
DATEHIGH = "1/1/2023 4:50 AM"

GOODCOMMENTS = [
    'Genial',
    'Buena pelicula, interesente y captiva',
    'Pelicula divertida',
    'Obra de arte',
    'Pelicual de Oscar!!!',
    'No puedo dejar de verla',
    'La he repetido mas de 3 veces',
    'Entretenida',
    'Quiero verla una y otra vez',
    'Me gusto',
    'Sin Comentario',
    'Pocas peliculas como esta',
    'Sin dudar de las mejores',
    'Hay peliculas malas y luego existen estas bellezas',
    'Quisiera volver a verla',
    'Me gusto tanto q la vi varias veces',
    'q joya acabo de ver',
    'No puedo creer q existan este tipio de peliculas!',
    'Buena',
    'Interesante',
    'Captiva',
    'Entretenida',
    'Mucha accion!',
    'Buenisima!!!!!!',
    'Super buena!!!!!!!',
    'Buena!',
    'Entretenida!',
    'Me encanto!!',
    'Top 10',
    'Buena buena buena',
    'Excelente!',
    'Una pelicula increible',
    'Un clasico',
    'Inolvidable',
    'Brillante, Brillante, Brillante',
    'Simple pero buena'
]

MEDCOMMENTS = [
    'Ni buena, ni mala',
    'Meh',
    'He visto mejores',
    'Mas o menos',
    'Sin Comentario',
    'Poco entretenida',
    'q pelicula mas x',
    'Sin duda, nada nuevo',
    'He bisto peores',
    'No me encato',
    'Media',
    'Promedio',
    'Lo mismo de siempre',
    'Mah',
    'Nada nuevo',
    'Una vez y ya',
    'He visto peores'
]

BADCOMMENTS = [
    'Pesima!',
    'Me dormi viendola',
    'Me arrepiento de verla',
    'Una pelicula que paso sin pena ni gracia',
    'Sin Comentario',
    'Muy aburridaaaaa!!',
    'Muy aburrida',
    'He visto peores',
    'Pfff, prefiero no hablar de ella',
    'No vale la pena verla!',
    'No vale la pena verla!',
    'Desperdicio de dinero',
    'Hay peliculas malas y luego esta esta',
    'No se que poner',
    'Prefiero no decir nada...',
    'No la vean',
    'Le hacen un favor al mundo al no ver tremenda caga...',
    'quieranse y vean otra cosa',
    'Mala',
    'Horrible',
    'Pesima!!!!!!!',
    'Pesima',
    'Malisima!!!',
    'Mala mala mala',
    'Malisima',
    'Horrible!',
    'Absurdamente mala',
    'Si pudiera darle menos, lo haria',
    'No para ser tomada enserio',
    'Intenta hacer una peor pelicula...'
]
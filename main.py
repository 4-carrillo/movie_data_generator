#------------- Imports -----------------
from numpy.random import (
    randint,
    uniform,
    choice
)
from src.constants import(
    COL_LIST,
    REGISTRES,
    BRONZEPATH,
    DATELOW,
    DATEHIGH,
    GOODCOMMENTS,
    MEDCOMMENTS,
    BADCOMMENTS
)
from pandas import (
    DataFrame,
    read_csv
)
from src.user.generate_users import generate_user
from src.user.calculate_age import age_by_year
from src.datamodels.models import dataOut
#from pydantic import Json
from typing import List
from fastapi import FastAPI
import uvicorn

#------------- Config -----------------

movies =  read_csv(BRONZEPATH + 'movies.csv')
app = FastAPI()

#----------- Main Code ----------------

@app.get(
        '/',
        status_code=200
)
async def root():

    """
    Endpoint for health check
    """

    return {"Health": "Ok"}

@app.post(
        "/data",
        status_code=200
)
async def generate_random_samples() -> List[dataOut]:

    """
    Endpoint for generating movie data \n

    Args: \n
        None
    Output: \n
        List[Dict]: JSON list with the following schema 

        [
            {
                'userid': int,
                'age': int,
                'title': string,
                'genres': string,
                'rating': float,
                'commentary': string,
                'date': string
            },
            {...},
            .
            .
            .
            {...}
        ]
    """

    moviesRandom = movies.sample(n = REGISTRES, replace = True)
    moviesRandom = moviesRandom[['title', 'genres']]

    users = generate_user()
    userNew =  age_by_year(users)

    rating = [round(x,1) for x in uniform(1, 5, size=REGISTRES)]
    comments = [ choice(GOODCOMMENTS) if x > 3.9 else choice(MEDCOMMENTS) if x > 2.9 else choice(BADCOMMENTS) for x in rating ]

    moviesFinal = DataFrame(
        {
            COL_LIST[0]: userNew['users'].tolist(),
            'signup_age': userNew['signup_age'].tolist(),
            COL_LIST[1]: userNew['ages'].tolist(),
            COL_LIST[2]: moviesRandom['title'].tolist(),
            COL_LIST[3]: moviesRandom['genres'].tolist(),
            COL_LIST[4]: rating,
            COL_LIST[5]: comments,
            COL_LIST[6]: userNew['dates'].tolist()
        }
    )

    return moviesFinal.to_dict(orient = 'records')

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)
# ------- Imports ------------
from pandas import DataFrame
from numpy.random import (
    randint
)
from src.constants import(
    REGISTRES
)

# ------- Main Code ----------

def generate_user():

    ages = randint(18, 60, size=100)
    users = [i+1 for i in range(100)]

    usersData = DataFrame(
        {
            'users': users,
            'ages': ages
        }
    )

    return usersData

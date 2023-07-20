# ------ Imports ------------
from pandas import to_datetime
from datetime import datetime
from src.constants import (
    DATEHIGH,
    DATELOW,
    REGISTRES
)
from src.date.random_date import(
    random_date
)

# ------ Main Code ----------

def age_by_year(users):

    usersData = users.sample(n = REGISTRES, replace = True)
    usersData['dates'] = [random_date(DATELOW, DATEHIGH) for i in range(REGISTRES)]

    signUpDate = datetime.strptime(DATELOW, '%m/%d/%Y %I:%M %p')

    usersData['signup_age'] = usersData['ages']
    usersData['ages'] = (
            usersData['ages'] * 365 * 24 * 60 * 60 
                + 
            (to_datetime(usersData['dates']) - signUpDate).dt.total_seconds()
        )/(365 * 24 * 60 * 60)

    return usersData
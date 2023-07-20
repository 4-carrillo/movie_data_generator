from pydantic import BaseModel
from pydantic import Field


class dataOut(BaseModel):
    userid: int = Field(
                    42,
                    title='User ID',
                    description='User ID'
                )
    age: int = Field(
                    25,
                    title='User Age',
                    description='User Age'
                )
    title: str = Field(
                    'Minions (2015)',
                    title='Movie Title',
                    description='Movie Title',
                )
    genres: str = Field(
                    'Action|Drama',
                    title='Movie genre',
                    description='Movie genre',
                ) 
    rating: float = Field(
                    3.2,
                    title='Movie rating',
                    description='Movie rate given by user',
                ) 
    commentary: str = Field(
                    'Patetica!',
                    title='Movie commentary',
                    description='User given review',
                )
    date: str = Field(
                    '10/26/2015 09:43 AM',
                    title='Review date',
                    description='Date where the review was submitted',
                )
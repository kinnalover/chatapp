from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

#параметры которые нужны во время создания пользователя
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

#то что мы хотим показывать
class ShowUser(BaseModel):
    username: str
    email : EmailStr
    is_active: bool


    #Для того чтоб пидантик смог конвертануть не словари в json
    class Config():
        orm_mode=True

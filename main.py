from pydantic import BaseModel, ValidationError, Field, validator, root_validator


class City(BaseModel):
    id: int
    name: str = Field(alias='cityFullName')

    @validator("name")
    def name_should_be_sbp(cls, v:str) -> str:
        if "sbp" not in v.lower():
            raise ValueError("Error sbp is not allowed!")
        return v
    
    @root_validator
    def root_validator(cls, values):
        print(values)
        return values


input_json = """{"id": 1, "cityFullName": "sbp"}"""
try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print(e.json())  
else:   
    print(city.json(by_alias=True, #для простарнства имен между back & front-end
                    exclude={"id"}) #исключение некоторых полей 
) 

class UserModelWithoutPassword(BaseModel):#наружу можно отдавать эту модель
    id: int
    name: str
    email: str
    about: str 

class UserModelWithPassword(UserModelWithoutPassword): #в бд можно хранить эту модель
    password: str
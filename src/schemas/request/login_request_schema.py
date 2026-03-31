from pydantic import BaseModel

class LoginRequesSchema(BaseModel):
    username: str
    password: str
        
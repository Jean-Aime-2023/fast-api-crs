from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

users = [] 

class User(BaseModel):
    email: str
    is_Active: bool
    bio: Optional[str]

@app.get("/users", response_model = List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User): 
    users.append(user)
    return {"message": "User created"}

@app.get('/users/:id')
async def get_user(
    id: int = Path(...,description="User Id",gt=0),
    q: bool = Query(None,max_length=5)
):
    return {"User":users[id],"query":q}
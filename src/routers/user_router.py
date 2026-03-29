from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.user_repository import UserRepository
from repositories.action_repository import ActionRepository
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repo = UserRepository(db)
    action_repo = ActionRepository(db)
    return UserService(user_repo, action_repo)

@router.get("/{user_id}")
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    pass
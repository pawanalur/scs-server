from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.action_repository import ActionRepository
from services.action_service import ActionService
from services.user_service import UserService
from routers.user_router import get_user_service


router = APIRouter(prefix="/actions", tags=["Actions"])

def get_action_service(db: Session = Depends(get_db),
                       user_service: UserService = Depends(get_user_service)) -> ActionService:
    action_repo = ActionRepository(db)
    return ActionService(action_repo, user_service)

@router.post("/")
async def create_action(service: ActionService = Depends(get_action_service)):
    pass
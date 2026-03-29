from repositories.action_repository import ActionRepository
from services.user_service import UserService

class ActionService:
    def __init__(self, action_repo: ActionRepository, user_service: UserService):
        self.action_repo = action_repo
        self.user_service = user_service
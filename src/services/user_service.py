from repositories.user_repository import UserRepository
from repositories.action_repository import ActionRepository

class UserService:
    def __init__(self, user_repo: UserRepository, action_repo: ActionRepository):
        self.user_repo = user_repo
        self.action_repo = action_repo
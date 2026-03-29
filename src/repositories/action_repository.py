from sqlalchemy.orm import Session

class ActionRepository:
    def __init__(self, db: Session):
        self.db = db
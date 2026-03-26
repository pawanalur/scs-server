from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}/energy")
async def get_user_energy(user_id: int):
    return {
        "user_id": user_id,
        "physicalEnergy": 100,
        "mentalEnergy": 80
    }
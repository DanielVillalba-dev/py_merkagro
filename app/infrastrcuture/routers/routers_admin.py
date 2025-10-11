from fastapi import APIRouter, Request

from app.application.service.admin_service import UserService
from app.infrastrcuture.repositories.admin_repository_adapter import UserRepositoryAdapter

router = APIRouter(prefix="/admin", tags=["admin"])

repo = UserRepositoryAdapter()
service = UserService(repo)
@router.get("/")
async def load_data():
    count = service.count_users()
    return {"cantidad usuarios: ": count}
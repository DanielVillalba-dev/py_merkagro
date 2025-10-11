from fastapi import APIRouter, Request

from app.application.service.admin_service import UserService
from app.infrastrcuture.repositories.admin_repository_adapter import UserRepositoryAdapter

router = APIRouter(prefix="/admin", tags=["admin"])

repo = UserRepositoryAdapter()
service = UserService(repo)
@router.get("/")
async def load_data():
    count_users = service.count_users()
    count_companys = service.count_companys()
    return {
        "cantidad usuario", count_users,
        "cantidad companys", count_companys
    }
from fastapi import APIRouter
from fastapi.params import Depends

from app.application.service.admin_service import AdminService
from app.infrastructure.repositories.admin_repository_adapter import AdminRepositoryAdapter
router = APIRouter(prefix="/admin", tags=["admin"])

def get_service():
    repo = AdminRepositoryAdapter()
    return AdminService(repo)

@router.get("/")
async def load_data(service: AdminService = Depends(get_service())):
    count_users = service.count_users()
    count_companies = service.count_companys()
    return {
        "cantidad usuario": count_users,
        "cantidad companys": count_companies
    }
from fastapi import APIRouter
from fastapi.params import Depends
from app.application.service.admin_service import AdminService
from app.domain.repositories.generics_methods_repository import GenericsMethodsRepository
from app.infrastructure.adapter.admin_repository_adapter import AdminRepositoryAdapter
from app.infrastructure.adapter.generics_methods_adapter import GenericsMethodsAdapter

router = APIRouter(prefix="/admin", tags=["admin"])

def get_service():
    admin_repo = AdminRepositoryAdapter()
    generic_repo = GenericsMethodsAdapter()
    return AdminService(admin_repo, generic_repo)

@router.get("/")
async def load_data(service: AdminService = Depends(get_service)):
    count_users = service.count_users()
    return {
        "cantidad usuario": count_users
    }
from fastapi import APIRouter
from fastapi.params import Depends
from app.application.service.admin_service import AdminService
from app.application.service.generics_service import GenericsService
from app.infrastructure.adapter.admin_repository_adapter import AdminRepositoryAdapter

router = APIRouter(prefix="/admin", tags=["admin"])

def get_service():
    admin_repo = AdminRepositoryAdapter()
    generics = GenericsService()
    return AdminService(admin_repo, generics)

@router.get("/")
async def load_data(service: AdminService = Depends(get_service)):

    count_users = service.count_users()
    count_associations = service.count_associations()

    return {
        "usuarios": count_users,
        "asociaciones": count_associations
    }
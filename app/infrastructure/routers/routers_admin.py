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
    users_month = service.count_users_by_month()
    associations_month = service.count_associations_by_month()
    user_growth = service.growth_percentage_user()
    association_growth = service.growth_percentage_association()

    return {
        "usuarios": {
            "usuarios_totales": count_users,
            "usuarios_nuevos": users_month,
            "porcentaje_crecimiento_usuario": user_growth
        },
        "asociaciones": {
            "asociaciones_totales": count_associations,
            "asociaciones_nuevas": count_associations,
            "porcentaje_crecimiento_asociacion": association_growth
        }
    }
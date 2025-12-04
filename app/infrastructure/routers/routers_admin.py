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
    count_requests = service.count_request()
    request_month = service.count_request_by_month()
    request_growth = service.growth_percentage_request()
    rejected_tase = service.conversion_rate_rejected()
    accepted_tase = service.conversion_rate_accepted()
    departament_by_associations = service.porcentaje_associations_by_departament()
    donut_users = service.porcentaje_users_by_rol()

    return {
        "usuarios": {
            "usuarios_totales": count_users,
            "usuarios_nuevos": users_month,
            "porcentaje_crecimiento_usuario": user_growth
        },
        "asociaciones": {
            "asociaciones_totales": count_associations,
            "asociaciones_nuevas": associations_month,
            "porcentaje_crecimiento_asociacion": association_growth
        },
        "solicitudes": {
            "cantidad_solicitudes": count_requests,
            "solicitudes_nuevas": request_month,
            "porcentaje_de_crecimiento_solicitudes": request_growth
        },
        "tasas_de_conversion_solicitudes": {
            "solicitudes_rechazadas": rejected_tase,
            "solicitudes_aceptadas": accepted_tase
        },
        "porcentaje_de_asociaciones_por_departamento": {
            "porcentaje_de_departamentos": departament_by_associations
        },
        "donuts": {
            "porcentaje_por_usuario": donut_users
        }
    }
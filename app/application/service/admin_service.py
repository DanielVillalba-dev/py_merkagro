import pandas as pd

from app.infrastructure.adapter.generics_methods_adapter import GenericsMethodsRepository
from app.domain.repositories.admin_repository import AdminRepository


class AdminService:
    def __init__(self, admin_repository: AdminRepository, generics_methods_repository: GenericsMethodsRepository):
        self.admin_repository = admin_repository
        self.generics_methods_repository = generics_methods_repository

    #Toma todos los usuarios de la base de datos y los convierte en un DataFrame
    def get_users_dataframe(self) -> pd.DataFrame:
        users = self.admin_repository.get_all_users()
        return self.generics_methods_repository.to_dataframe(users)

    #Devuelve el ancho del dataframe de usuarios
    def count_users(self) -> int:
        df_users = self.get_users_dataframe()
        return len(df_users)
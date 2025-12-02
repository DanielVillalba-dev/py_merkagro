import pandas as pd

from app.application.service.generics_service import GenericsService
from app.domain.repositories.admin_repository import AdminRepository


class AdminService:
    def __init__(self, admin_repository: AdminRepository, generics_service: GenericsService):
        self.admin_repository = admin_repository
        self.generics_service = generics_service

    def get_users(self) -> pd.DataFrame:
        users = self.admin_repository.get_all_users()
        return self.generics_service.to_dataframe(users)

    def get_associations(self) -> pd.DataFrame:
        associations = self.admin_repository.get_all_association()
        return self.generics_service.to_dataframe(associations)

    def count_users(self) -> int:
        df_users = self.get_users()
        return len(df_users)

    def count_associations(self) -> int:
        df_associations = self.get_associations()
        return len(df_associations)

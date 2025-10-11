import pandas as pd
from app.domain.repositories.admin_repository import AdminRepository

class AdminService:
    def __init__(self, admin_repository: AdminRepository):
        self.admin_repository = admin_repository

    def _to_dataframe(self, data: list[dict]) -> pd.DataFrame:
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    def get_users_dataframe(self) -> pd.DataFrame:
        users = self.admin_repository.get_all_users()
        return self._to_dataframe(users)

    def get_company_dataframe(self) -> pd.DataFrame:
        companies = self.admin_repository.get_all_companies()
        return self._to_dataframe(companies)

    def count_users(self) -> int:
        df_users = self.get_users_dataframe()
        return len(df_users)

    def count_companies(self) -> int:
        df_companies = self.get_company_dataframe()
        return len(df_companies)
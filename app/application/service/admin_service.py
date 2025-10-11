import pandas as pd
from app.domain.repositories.admin_repository import AdminRepository

class UserService:
    def __init__(self, admin_repository: AdminRepository):
        self.admin_repository = admin_repository

    def get_users_dataframe(self) -> pd.DataFrame:
        users = self.admin_repository.get_all_users()
        df = pd.DataFrame(users)
        return df

    def get_company_dataframe(self) -> pd.DataFrame:
        companys = self.admin_repository.get_all_companys()
        df = pd.DataFrame(companys)
        return df

    def count_users(self) -> int:
        number_columns = len(self.get_users_dataframe())
        return number_columns

    def count_companys(self) -> int:
        number_columns = len(self.get_company_dataframe())
        return number_columns
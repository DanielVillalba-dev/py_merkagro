from datetime import datetime

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

    @staticmethod
    def growth_percentage(users_this_month: int, users_last_month: int) -> float:
        growth: float = ((users_this_month - users_last_month) / users_last_month) * 100

        if growth == -100.0:
            return 0.0

        return round(growth, 2)

    @staticmethod
    def _by_month(data: pd.DataFrame) -> int:

        now = datetime.now()

        start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = (start_date + pd.offsets.MonthBegin(1))

        df = data[(data['creado_en'] >= start_date) & (data['creado_en'] < next_month)]

        return len(df)

    def count_users_by_month(self) -> int:

        df_users = self.get_users()
        df_users = self.generics_service.to_datetime(df_users, 'creado_en')

        return self._by_month(df_users)

    def count_associations_by_month(self) -> int:

        df_associations = self.get_associations()
        df_associations = self.generics_service.to_datetime(df_associations, 'creado_en')

        return self._by_month(df_associations)

    def growth_percentage_user(self) -> float:

        df_users = self.get_users()
        df_users = self.generics_service.to_datetime(df_users, 'creado_en')

        users_this_month = self.count_users_by_month()

        now = datetime.now()
        first_day_last_month = (now.replace(day=1) - pd.DateOffset(months=1)).replace(day=1)
        last_day_last_month = (now.replace(day=1) - pd.DateOffset(days=1))

        users_last_month = df_users[
            (df_users['creado_en'] >= first_day_last_month) &
            (df_users['creado_en'] <= last_day_last_month)
        ]

        count_users_last_month = len(users_last_month)

        return self.growth_percentage(users_this_month, count_users_last_month)

    def growth_percentage_association(self) -> float:

        df_associations = self.get_associations()
        df_associations = self.generics_service.to_datetime(df_associations, 'creado_en')

        associations_this_month = self.count_associations_by_month()

        now = datetime.now()
        first_day_last_month = (now.replace(day=1) - pd.DateOffset(months=1)).replace(day=1)
        last_day_last_month = (now.replace(day=1) - pd.DateOffset(days=1))

        associations_last_month = df_associations[
            (df_associations['creado_en'] >=  first_day_last_month) &
            (df_associations['creado_en'] <= last_day_last_month)
        ]

        count_associations_last_month = len(associations_last_month)

        return self.growth_percentage(associations_this_month, count_associations_last_month)


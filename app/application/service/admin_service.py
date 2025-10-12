from datetime import datetime

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

    def get_requests(self) -> pd.DataFrame:
        pending_requests = self.admin_repository.get_all_registration_requests()
        return self._to_dataframe(pending_requests)

    def count_users(self) -> int:
        df_users = self.get_users_dataframe()
        return len(df_users)

    def count_companies(self) -> int:
        df_companies = self.get_company_dataframe()
        return len(df_companies)

    def count_pending_requests(self, status: str) -> int:
        df_requests = self.get_requests()
        if "estado_documento" not in df_requests:
            return 0
        return len(df_requests[df_requests['estado_documento'] == status])

    def conversion_rate_rejected_applications(self, status: str) -> float:
        df_requests = self.get_requests()

        if "creado_en" in df_requests:
            df_requests["creado_en"] = pd.to_datetime(df_requests["creando_en"], errors="coerce")

            df_approved = df_requests[df_requests["estado"] == "ACEPTADA"].copy()

            df_approved["año"] = df_approved["creado_en"].dt.year
            df_approved["mes"] = df_approved["creado_en"].dt.month

            today = datetime.now()
            month_actual = today.month
            year_actual = today.year
            month_past = month_actual - 1 if month_actual > 1 else 12
            year_past = year_actual if month_actual > 1 else year_actual - 1

            actual = len(df_approved[(df_approved["año"] == year_actual) & (df_approved["mes"] == month_actual)])
            past = len(df_approved[(df_approved["año"] == year_past) & (df_approved["mes"] == month_past)])

            if past == 0:
                return 0.0

            variation = ((actual - past) / past) * 100
            return round(variation, 2)
        return 0
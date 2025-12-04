from datetime import datetime
from typing import Dict, List

import pandas as pd
from app.application.service.generics_service import GenericsService
from app.domain.repositories.admin_repository import AdminRepository


class AdminService:
    def __init__(self, admin_repository: AdminRepository, generics_service: GenericsService):
        self.admin_repository = admin_repository
        self.generics_service = generics_service

    #Tomar datos de la BD y transformarlos en DataFrame

    def get_users(self) -> pd.DataFrame:
        users = self.admin_repository.get_all_users()
        return self.generics_service.to_dataframe(users)

    def get_associations(self) -> pd.DataFrame:
        associations = self.admin_repository.get_all_association()
        return self.generics_service.to_dataframe(associations)

    def get_request_registers(self) -> pd.DataFrame:
        requests = self.admin_repository.get_all_registration_request()
        return self.generics_service.to_dataframe(requests)

    #Contar el ancho del DataFrame

    def count_users(self) -> int:
        df_users = self.get_users()
        return len(df_users)

    def count_associations(self) -> int:
        df_associations = self.get_associations()
        return len(df_associations)

    def count_request(self) -> int:
        df_request = self.get_request_registers()
        return len(self.generics_service.check_status_request(df_request, "PENDIENTE"))

    #Contar usuarios nuevos del mes

    def count_users_by_month(self) -> int:

        df_users = self.get_users()
        df_users = self.generics_service.to_datetime(df_users, 'creado_en')

        return self.generics_service.by_month(df_users)

    def count_associations_by_month(self) -> int:

        df_associations = self.get_associations()
        df_associations = self.generics_service.to_datetime(df_associations, 'creado_en')

        return self.generics_service.by_month(df_associations)

    def count_request_by_month(self) -> int:

        df_request = self.get_request_registers()
        df_request = self.generics_service.check_status_request(df_request, "PENDIENTE")
        df_request = self.generics_service.to_datetime(df_request, 'creado_en')

        return self.generics_service.by_month(df_request)

    #Porcentaje de crecimiento

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

        return self.generics_service.growth_percentage(users_this_month, count_users_last_month)

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

        return self.generics_service.growth_percentage(associations_this_month, count_associations_last_month)

    def growth_percentage_request(self) -> float:

        df_request = self.get_request_registers()
        df_request = self.generics_service.check_status_request(df_request, "PENDIENTE")
        df_request = self.generics_service.to_datetime(df_request, 'creado_en')

        request_this_month = self.count_request_by_month()

        now = datetime.now()
        first_day_last_month = (now.replace(day=1) - pd.DateOffset(months=1)).replace(day=1)
        last_day_last_month = (now.replace(day=1) - pd.DateOffset(days=1))

        request_last_month = df_request[
            (df_request['creado_en'] >= first_day_last_month) &
            (df_request['creado_en'] <= last_day_last_month)
        ]

        count_request_last_month = len(request_last_month)

        return self.generics_service.growth_percentage(request_this_month, count_request_last_month)

    #Tasa de conversion solicitudes

    def conversion_rate_rejected(self) -> float:
        df_request = self.get_request_registers()
        rejected = len(self.generics_service.check_status_request(df_request, "RECHAZADA"))
        pendiente = len(self.generics_service.check_status_request(df_request, "PENDIENTES"))
        accepted = len(self.generics_service.check_status_request(df_request, "ACEPTADA"))

        return self.generics_service.conversion_rate(rejected, accepted, pendiente)

    def conversion_rate_accepted(self) -> float:
        df_request = self.get_request_registers()
        accepted = len(self.generics_service.check_status_request(df_request, "ACEPTADA"))
        pendiente = len(self.generics_service.check_status_request(df_request, "PENDIENTE"))
        rejected = len(self.generics_service.check_status_request(df_request, "RECHAZADA"))

        return self.generics_service.conversion_rate(accepted, rejected, pendiente)

    #Card
    #Porcentaje de asociaciones por departamento
    def porcentaje_associations_by_departament(self) -> List[Dict[str, float]]:
        df_associations = self.get_associations()
        counts = df_associations['municipalityName'].value_counts()
        total = counts.sum()
        result: List[Dict[str, float]] = []
        top5 = counts.head(5)
        for departament, count in top5.items():
            porcentaje = (count / total) * 100
            result.append({
                "departamento": str(departament),
                "porcentaje": float(round(porcentaje, 2))
            })
        return result

    #Donuts
    def porcentaje_users_by_rol(self) -> List[Dict[str, float]]:
        df = self.get_users()
        result: List[Dict[str, float]] = []

        counts = df['rolName'].value_counts()

        total = counts.sum()

        result: List[Dict[str, float]] = []

        for rol, count in counts.items():
            porcentaje = (count / total) * 100

            result.append({
                "rol": str(rol),
                "porcentaje": float(round(porcentaje, 2))
            })
        return result
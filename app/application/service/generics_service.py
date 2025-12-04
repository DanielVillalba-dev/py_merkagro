from datetime import datetime

import pandas as pd

class GenericsService:

    @staticmethod
    def to_dataframe(data: list[dict]) -> pd.DataFrame:
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    @staticmethod
    def to_datetime(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        if column_name not in data.columns:
            raise ValueError(f"La columna '{column_name}' no existe")

        data[column_name] = pd.to_datetime(data[column_name], errors = "coerce")

        return data

    @staticmethod
    def check_status_request(data: pd.DataFrame, state: str) -> pd.DataFrame:
        pending = data[data['state'] == "PENDIENTE"]
        rejected = data[data['state'] == "RECHAZADA"]
        accepted = data[data['state'] == "ACEPTADA"]

        if state == "PENDIENTE":
            return pending
        elif state == "RECHAZADA":
            return rejected
        elif state == "ACEPTADA":
            return accepted

        return data

    @staticmethod
    def growth_percentage(users_this_month: int, users_last_month: int) -> float:
        growth: float = ((users_this_month - users_last_month) / users_last_month) * 100

        if growth == -100.0:
            return 0.0

        return round(growth, 2)

    @staticmethod
    def by_month(data: pd.DataFrame) -> int:

        now = datetime.now()

        start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = (start_date + pd.offsets.MonthBegin(1))

        df = data[(data['creado_en'] >= start_date) & (data['creado_en'] < next_month)]

        return len(df)

    @staticmethod
    def conversion_rate(val1: int, val2: int, val3:int) -> float:
        total = val1 + val2 + val3

        if total == 0:
            return 0.0

        return round((val1 / total) * 100, 2)
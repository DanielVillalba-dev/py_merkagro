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
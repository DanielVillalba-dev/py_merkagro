import pandas as pd

class GenericsService:

    @staticmethod
    def to_dataframe(self, data: list[dict]) -> pd.DataFrame:
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    @staticmethod
    def to_datetime(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
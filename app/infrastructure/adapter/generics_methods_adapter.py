from app.domain.repositories.generics_methods_repository import GenericsMethodsRepository
import pandas as pd

class GenericsMethodsAdapter(GenericsMethodsRepository):

    def to_dataframe(self, data: list[dict]) -> pd.DataFrame:
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)
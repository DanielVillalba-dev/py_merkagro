from abc import ABC, abstractmethod
import pandas as pd

class GenericsMethodsRepository(ABC):

    @abstractmethod
    def to_dataframe(self, data: list[dict]) -> pd.DataFrame:
        pass
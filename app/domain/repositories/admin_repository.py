from abc import ABC, abstractmethod
from typing import List, Dict


class AdminRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def get_all_companies(self) -> List[Dict[str, any]]:
        pass
from abc import ABC, abstractmethod
from typing import List, Dict


class AdminRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def get_all_companies(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def get_all_registration_requests(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def conversion_rate_rejected_applications(self) -> List[Dict[str, any]]:
        pass

    @abstractmethod
    def conversion_rate_approved_applications(self) -> List[Dict[str, any]]:
        pass
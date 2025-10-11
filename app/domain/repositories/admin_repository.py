from abc import ABC, abstractmethod

class AdminRepository(ABC):

    @abstractmethod
    def get_all_users(self):
        pass
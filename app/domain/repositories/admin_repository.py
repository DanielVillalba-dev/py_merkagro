from abc import ABC, abstractmethod
from typing import List, Dict
class AdminRepository(ABC):

    #Metodo abstracto para obtener todos los usuarios
    @abstractmethod
    def get_all_users(self) -> List[Dict[str, any]]:
        pass

    #Metodo para obtener cuantos usuarios nuevos se registraron al mes
    # def get_user_by_moth(self) -> List[Dict[str, any]]:
    #     pass
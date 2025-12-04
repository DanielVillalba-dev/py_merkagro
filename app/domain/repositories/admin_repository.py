from abc import ABC, abstractmethod
from typing import List, Dict
class AdminRepository(ABC):

    #Metodo abstracto para obtener todos los usuarios
    @abstractmethod
    def get_all_users(self) -> List[Dict[str, any]]:
        pass

    #Metodo para obtener asociaciones
    @abstractmethod
    def get_all_association(self) -> List[Dict[str, any]]:
        pass

    #Metodo para obtener solicitudes de registro
    @abstractmethod
    def get_all_registration_request(self) -> List[Dict[str, any]]:
        pass
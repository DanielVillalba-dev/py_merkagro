from typing import List, Dict
import requests
from app.domain.repositories.admin_repository import AdminRepository

JAVA_API_URL = "http://localhost:8080/api/v1"

class AdminRepositoryAdapter(AdminRepository):
    def __init__(self):
        self.session = requests.Session()

    def take_data(self, endpoint: str, page: int = 0, size: int = 10000):
        url = f"{JAVA_API_URL}/{endpoint}?page={page}&size={size}"
        response = self.session.get(url)

        try:
            response.raise_for_status()
            data = response.json()

            return data.get("content", [])

        except requests.RequestException as e:
            print(f"Error al consultar {url}: {e}")
            return []

    def get_all_users(self) -> List[Dict[str, any]]:
        return self.take_data("usuarios/listar-usuarios")

    def get_all_association(self) -> List[Dict[str, any]]:
        return self.take_data("asociacion/listar-asociaciones")
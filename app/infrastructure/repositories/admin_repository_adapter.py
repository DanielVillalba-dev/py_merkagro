import requests
from app.domain.repositories.admin_repository import AdminRepository

JAVA_API_URL = "http://localhost:8080/api/v1"

class AdminRepositoryAdapter(AdminRepository):
    def __init__(self):
        self.session = requests.Session()

    def _fetch_data(self, endpoint: str, page: int = 0, size: int = 100):
        url = f"{JAVA_API_URL}/{endpoint}?page={page}size={size}"
        response = self.session.get(url)

        try:
            response.raise_for_status()
            data = response.json()
            return data.get("content", [])
        except requests.RequestException as e:
            print(f"Error al consultar {url}: {e}")
            return []

    def get_all_users(self):
        return self._fetch_data("user")

    def get_all_companies(self):
        return self._fetch_data("companies")

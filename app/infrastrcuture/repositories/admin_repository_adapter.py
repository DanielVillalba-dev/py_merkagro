import requests
from app.domain.repositories.admin_repository import UserRepository

JAVA_API_URL = "http://localhost:8080/api/v1/user"

class UserRepositoryAdapter(UserRepository):
    def get_all_users(self):
        response = requests.get(f"{JAVA_API_URL}?page=0&size=100")
        response.raise_for_status()
        data = response.json()
        return data.get("content", [])


import pandas as pd
from app.domain.repositories.admin_repository import UserRepository # interfaz abstracta

class AnalyticsService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute_metric(self, metric: str):

        users = self.user_repository.get_all_users()

        df = pd.DataFrame(users)

        if df.empty:
            return {"message": "No se encontraron usuarios"}

        if metric == "all":
            total = len(df)
            return {"total_usuario": total}

        elif metric == "byRol":
            if "nombre_rol" in df.columns:
                resumen = df.groupby("nombre_rol")["nombre_rol"].count().reset_index(name="cantidad")
                return resumen.to_dict(orient="records")
            else:
                return {"Error": "La columna nombre_rol no existe"}

        return None
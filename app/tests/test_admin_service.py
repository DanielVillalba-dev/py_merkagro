# #Toma todos los usuarios de la base de datos y los convierte en un DataFrame
#     def get_users_dataframe(self) -> pd.DataFrame:
#         users = self.admin_repository.get_all_users()
#         return self.generics_methods_repository.to_dataframe(users)
#
#     def get_association_dataframe(self) -> pd.DataFrame:
#         associations = self.admin_repository.get_all_association()
#         return self.generics_methods_repository.to_dataframe(associations)
#
#     def to_datetime(self, data: pd.DataFrame) -> pd.DataFrame:
#
#
#     #Devuelve el ancho del dataframe de usuarios
#     def count_users(self) -> int:
#         df_users = self.get_users_dataframe()
#         return len(df_users)
#
#     #Devuelve el ancho del dataframe con los usuarios por mes
#     def count_user_by_moth(self) -> int:
#
#         #Toma los usuarios registrados
#         df_users = self.get_users_dataframe()
#
#         #Convierte la fecha de la columna seleccionada en formato datetime64
#         df_users["creado_en"] = pd.to_datetime(df_users["creado_en"])
#
#         #Toma la fecha actual
#         now = datetime.now()
#         #Resetea la fecha tomada por el now
#         start = now.replace(day = 1, hour = 0, minute = 0, second = 0, microsecond = 0)
#         #Aumenta un mes a la fecha guardada en start
#         next_month = (start + pd.offsets.MonthBegin(1))
#
#         #guarda en un nuevo dataFrame los usuarios mayores a la fecha en start y menores a la fecha en next_month
#         df_month = df_users[(df_users['creado_en'] >= start) & (df_users['creado_en'] < next_month)]
#
#         #Devuelve el ancho del dataFramne
#         return len(df_month)
#
#     #Calcular el porcentaje de crecimiento de usuarios
#     def growth_percentage_user(self) -> float:
#
#         #Toma los usuarios registrados
#         df_users = self.get_users_dataframe()
#
#         #Toma los usuarios registrados en este mes
#         users_this_month = self.count_user_by_moth()
#
#         #Convierte la fecha de la columna seleccionada en formato datetime64
#         df_users["creado_en"] = pd.to_datetime(df_users["creado_en"])
#
#         #Toma la fecha actual
#         now = datetime.now()
#
#         #Primer día del mes pasado
#         first_day_last_month = (now.replace(day=1) - pd.DateOffset(months=1)).replace(day=1)
#
#         #Último día del mes pasado
#         last_day_last_month = (now.replace(day=1) - pd.DateOffset(days=1))
#
#         #Filtrar usuarios del mes pasado
#         users_last_month = df_users[
#             (df_users["creado_en"] >= first_day_last_month) &
#             (df_users["creado_en"] <= last_day_last_month)
#         ]
#
#         #Cuenta el ancho del dataFrame
#         count_users_last_month = len(users_last_month)
#
#         #se calcula el porcentaje de crecimiento
#         growth: float = ((users_this_month - count_users_last_month) / count_users_last_month) * 100
#
#         if growth == -100.0:
#             growth = 0.0
#
#         return growth
#
#     #Devuelve el ancho del dataframe de las asociaciones
#     def count_associations(self) -> int:
#         df_association = self.get_association_dataframe()
#         return len(df_association)
#
#     def count_association_by_month(self) -> int:
#
#         df_associations = self.get_association_dataframe()
#
#         df_associations['creado_en'] = pd.to_datetime(df_associations['creado_en'])
#
#         now = datetime.now()
#         start = now.replace(day = 0, hour = 0, minute = 0, second = 0, microsecond = 0)
#         next_month = (start + pd.offsets.MonthBegin(1))
#
#         df_month = df_associations[(df_associations['creado_en'] >= start) & (df_associations['creado_en'] <= next_month)]
#
#         return len(df_month)
#
#     def growth_percentage_association(self) -> float:
#
#         df_associations = self.get_association_dataframe()
#
#         df_associations_this_month = self.count_association_by_month()
#
#         df_associations['creado_en'] = pd.to_datetime(df_associations['creado_en'])
#
#         now = datetime.now()
#
#         #Primer día del mes pasado
#         first_day_last_month = (now.replace(day=1) - pd.DateOffset(months=1)).replace(day=1)
#
#         #Último día del mes pasado
#         last_day_last_month = (now.replace(day=1) - pd.DateOffset(days=1))
#
#         df_association_last_month = df_associations[(df_associations['creado_en'] >= first_day_last_month) & (df_associations['creado_en'] <= last_day_last_month)]
#
#         count_association_last_month = len(df_association_last_month)
#
#         growth: float = ((df_associations_this_month - count_association_last_month) / count_association_last_month) * 100
#
#         if growth == -100.0:
#             return 0.0
#
#         return growth
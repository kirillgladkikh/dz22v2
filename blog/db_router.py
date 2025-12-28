# class BlogRouter:
#     """
#     Роутер для направления запросов к БД 'blog'
#     """
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'blog':
#             return 'blog'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'blog':
#             return 'blog'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         # Разрешаем отношения внутри одной БД
#         db1 = self.db_for_read(obj1.__class__)
#         db2 = self.db_for_read(obj2.__class__)
#         return db1 == db2
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'blog':
#             return db == 'blog'
#         return None

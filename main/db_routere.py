class AuthRouter:

    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        """Читання даних із users_db для моделей auth"""
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        """Запис даних у users_db для моделей auth"""
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Дозволити зв’язки між моделями у users_db"""
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Міграції для auth ідуть тільки в users_db"""
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return db == 'default'

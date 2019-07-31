class StatsRouter:

    def db_for_read(self, model, **hints):
        if model._meta.label == 'stats.Domain_stats':
            return 'dns_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.label == 'stats.Domain_stats':
            return 'dns_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'domain_stats':
		return db == 'dns_db' 
	else:
		return db == 'default'
        return None


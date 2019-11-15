from celery import Celery
import os

def make_celery(app):
    celery_app = Celery(app.import_name, broker=os.getenv('CELERY_BROKER_URL'))
    celery_app.conf.update(app.config)
    TaskBase = celery_app.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery_app.Task = ContextTask
    return celery_app
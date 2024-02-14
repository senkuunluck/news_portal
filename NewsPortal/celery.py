import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday8am': {
        'task': 'news.tasks.send_mail_every_monday8am',
        'schedule': crontab(hour=21, minute=25, day_of_week='thursday'),
        'args': ()
    }
}
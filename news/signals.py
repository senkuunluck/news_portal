from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from NewsPortal.news.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'news_create':
        categories = instance.category.all()
        subscribe = []

        for cat in categories:
            subscribers += cat.subscribers.all()
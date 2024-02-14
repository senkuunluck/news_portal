from datetime import datetime, timedelta

from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import PostCategory, Post, Category


@shared_task
def new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.title
    preview = post.preview()
    subscribers: list[str] = []
    for category in categories:
        subscribers += category.subscribers.all()
        subscribers = [s.email for s in subscribers]

    html_content = render_to_string(
        'post_created.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def weekly_post():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(datetime_post__gte=last_week)
    cat = set(posts.values_list('category__name', flat=True))
    subs = set(Category.objects.filter(name__in=cat).values_list('subscriber__email', flat=True))

    from NewsPortal.NewsPortal.settings import SITE_URL
    html_context = render_to_string(
        'account/email/email_weekly_posts.html',
        {
            'head_link': f'{SITE_URL}',
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Последние посты за неделю',
        body='',
        from_email=EMAIL_HOST_USER,
        to=subs,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()
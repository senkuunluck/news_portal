from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(
            Sum('rating'))['rating__sum']
        comment_rating = Comment.objects.filter(user=self.user).aggregate(
            Sum('rating'))['rating__sum']
        comment_rating_to_posts = Comment.objects.filter(
            post__author__user=self.user).aggregate(Sum('rating'))[
            'rating__sum']

        self.rating = ((post_rating * 3) + comment_rating +
                       comment_rating_to_posts)
        self.save()


class Category(models.Model):
    name_of_category = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.name_of_category


class Post(models.Model):
    article = 'A'
    news = 'N'
    TYPES = [
        (article, 'A'),
        (news, 'N')
    ]
    type = models.CharField(max_length=1, choices=TYPES, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return self.text[:124] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    time_of_comm = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

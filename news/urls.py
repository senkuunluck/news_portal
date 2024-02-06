from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsEdit, NewsDelete, ArticleCreate, ArticleEdit, \
   ArticleDelete, CategoryListView, subscribe

urlpatterns = [
   path('', PostList.as_view(), name='news'),
   path('search/', PostSearch.as_view(), name='search'),
   path('<int:pk>/', PostDetail.as_view(), name='detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]
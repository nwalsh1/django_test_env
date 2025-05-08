from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'), #path to the blog list page
    # path('create/', blog_create_view, name='blog-create'), #path to the blog create page
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), #path to the blog detail page
]                                                                                   
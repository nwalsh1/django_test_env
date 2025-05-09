from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'), #path to the blog list page
    path('create/', ArticleCreateView.as_view(), name='article-create'), #path to the blog create page
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), #path to the blog detail page
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'), #path to the blog update page
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'), #path to the blog delete page
]                                                                                   
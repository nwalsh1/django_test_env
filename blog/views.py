from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView) #importing class based views
from .models import Article #import model
from .forms import ArticleForm #import form

## Create your views here.
#simplest class based view, ListView
class ArticleListView(ListView):
    template_name = 'articles/article_list.html' #overide the default template name
    queryset = Article.objects.all() #blog/[modlename]_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html' #overide the default template name
    queryset = Article.objects.all() #blog/[modlename]_list.html

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_) #get the object from the url, if not found return 404 error
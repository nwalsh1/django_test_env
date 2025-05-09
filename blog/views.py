from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView) #importing class based views
from .models import Article #import model
from .forms import ArticleForm #import form

## Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html' #overide the default template name
    form_class = ArticleForm #form to be used in the view
    queryset = Article.objects.all() 
    #success_url = '/' #redirect to the home page after creating the article
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_sucess_url(self):
    #     return '/'


#simplest class based view, ListView
class ArticleListView(ListView):
    template_name = 'articles/article_list.html' #overide the default template name
    queryset = Article.objects.all() #blog/[modlename]_list.html

#DetailView - class based view for the detail page of the blog
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html' #overide the default template name
    queryset = Article.objects.all() #blog/[modlename]_list.html

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_) #get the object from the url, if not found return 404 error
    

#almost the same as create, but gets an instance of an object and then updates it
class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html' #overide the default template name
    form_class = ArticleForm #form to be used in the view
    queryset = Article.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

#similar to detail view 
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html' #overide the default template name

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_) 
    
    def get_success_url(self):
        return reverse('articles:article-list')
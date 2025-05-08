from django.urls import path
from .views import(
    product_detail_view, 
    product_create_view,
    product_delete_view,
    product_list_view,
    product_update_view
)
#relative import of all the views in the products app

#namespacing
app_name = 'products'
urlpatterns = [
    path('create/', product_create_view, name='create'),
    path('<int:my_id>/', product_detail_view, name='product-detail'),
    path('<int:my_id>/update', product_update_view, name='product-update'), #update the product
    path('<int:my_id>/delete', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'), #list all products
]

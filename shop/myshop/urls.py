from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product, name='product_list'),
    path('<slug:category_slug>/', views.product, name='product_list_by_category'),
    path('detail/<int:id>', views.detail, name='product_detail'),
    path('review/<int:id>', views.add_comment, name='add_comment'),

]
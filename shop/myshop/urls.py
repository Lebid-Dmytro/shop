from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.ProductView.as_view(), name='product_list'),
    path('<slug:category_slug>/', views.ProductView.as_view(), name='product_list_by_category'),
    path('<int:id>/', views.ProductDescriptionView.as_view(), name='product_detail'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),

]
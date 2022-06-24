from django.urls import path
from . import views
# app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('collections/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('things/', views.products, name='products'),
    path('collections/', views.categories, name='categories'),
    path('collections/<slug:category_slug>/<int:product_id>/things_detail/', views.product_detail, name='product_detail'),
]


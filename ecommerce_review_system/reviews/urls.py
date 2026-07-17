from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    
    path('products/<int:product_id>/reviews/', views.ReviewListView.as_view(), name='review_list'),
    
    path('products/<int:product_id>/reviews/add/', views.ReviewCreateView.as_view(), name='add_review'),
    
    path('reviews/<int:review_id>/delete/', views.ReviewDeleteView.as_view(), name='delete_review'),
    
    path('ratings/', views.ProductRatingsView.as_view(), name='product_ratings'),
]

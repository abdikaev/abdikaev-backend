from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index_page_view, name='index_page'),
    path('basket/', views.basket_page_view, name='basket'),
    path('add_to_basket/<int:pk>/', views.add_movie_to_basket_view, name='add_to_basket'),
    path('delete_from_basket/<int:pk>/', views.delete_from_basket_view, name='delete_from_basket'),
    path('movies/', views.movie_page_view, name='movie_page'),
    path('movies/<int:pk>/', views.movie_details_view, name='movie_details'),
    path('movies/<int:pk>/delete/', views.delete_movie_page_view, name='delete_movie_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile_page, name='profile'),
]

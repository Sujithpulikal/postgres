from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('list/', views.movie_list, name='movie_list'),
    path('edit/<int:movie_id>/', views.edit, name='edit'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
    path('',views.home,name='home')
   
    
]
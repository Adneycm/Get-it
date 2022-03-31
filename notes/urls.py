from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.destroy, name='destroy'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('tags', views.pageTags, name='pageTags'),
    path('specificTag/<str:tag>', views.specificTag, name='specificTag'),
    path('home', views.home, name='home')
]
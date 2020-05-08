from django.urls import path
from . import views
#app_name = 'catalog'
urlpatterns = [
    path("", views.index, name='index'),
    path('allbooks/', views.BookListView.as_view(), name='all_books'),
]
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
    path('<slug:slug>/edit/', views.page_edit, name='page_edit'),
    path('<slug:slug>/delete/', views.page_delete, name='page_delete'),
    path('create/', views.page_create, name='page_create'),
]
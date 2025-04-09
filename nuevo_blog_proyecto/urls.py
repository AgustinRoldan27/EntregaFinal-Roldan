from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # Importa las vistas de la app 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('', blog_views.home, name='home'),  # Asigna la raíz a la vista 'home' de 'blog'
]
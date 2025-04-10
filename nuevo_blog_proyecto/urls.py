from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # Importa las vistas de la app 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('blog/', include('blog.urls')),  # Incluye las URLs de la app 'blog' bajo la ruta '/blog/'
    path('', blog_views.home, name='home'),  # Tu vista 'home' sigue en la raíz
]
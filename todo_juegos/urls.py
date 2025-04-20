"""
URL configuration for todo_juegos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import index, registro, login, cerrar_sesion, categorias,carreras, deportes, supervivencia, mundo_abierto, terror, accion, resident_evil_village, outlast, resident_evil, helldivers, split_fiction, elden_ring, ark, gta, monster_hunter,f124,ndfs,most_wanted,reinicio_pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro/', registro, name="registro"),
    # path('cuenta/', cuenta, name="cuenta"),
    path('login/', login, name='login'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('categorias/', categorias, name='categorias'),
    
    path('reinicio_pass/', reinicio_pass, name='reinicio_pass'),
    

    # Categorias
    path('categorias/terror', terror, name='terror'),
    path('categorias/accion', accion, name='accion'),
    
    path('categorias/mundo_abierto', mundo_abierto, name='mundo_abierto'),
    path('categorias/carreras', carreras, name='carreras'),
    path('categorias/supervivencia', supervivencia, name='supervivencia'),
    path('categorias/deportes', deportes, name='deportes'),

    # Juegos de terror
    path('categorias/terror/resident_evil_village', resident_evil_village, name='resident_evil_village'),
    path('categorias/terror/outlast', outlast, name='outlast'),
    path('categorias/terror/resident_evil', resident_evil, name='resident_evil'),

    # Juegos de accion
    path('categorias/accion/helldivers', helldivers, name='helldivers'),
    path('categorias/accion/split_fiction', split_fiction, name='split_fiction'),
    path('categorias/accion/elden_ring', elden_ring, name='elden_ring'),
    
    
    # Juegos de mundo abierto
    path('categorias/mundo_abierto/ark', ark, name='ark'),
    path('categorias/mundo_abierto/gta', gta, name='gta'),
    path('categorias/mundo_abierto/monster_hunter', monster_hunter, name='monster_hunter'),

    # Juegos de mundo carreras
    path('categorias/carreras/ndfs', ndfs, name='ndfs'),
    path('categorias/carreras/most_wanted', most_wanted, name='most_wanted'),
    path('categorias/carreras/f124', f124, name='f124'),

]

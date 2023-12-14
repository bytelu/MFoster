"""
URL configuration for MFoster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('persona/', views.persona, name='persona'),
    path('persona/create/', views.create_persona, name='create_persona'),
    path('persona/<int:persona_id>/', views.persona_detail, name='persona_detail'),
    path('persona/<int:persona_id>/delete', views.delete_persona, name='delete_persona'),
    path('direccion/', views.direccion, name='direccion'),
    path('direccion/create/', views.create_direccion, name='create_direccion'),
    path('direccion/<int:direccion_id>/', views.direccion_detail, name='direccion_detail'),
    path('direccion/<int:direccion_id>/delete', views.delete_direccion, name='delete_direccion'),
    path('puesto/', views.puesto, name='puesto'),
    path('puesto/create/', views.create_puesto, name='create_puesto'),
    path('puesto/<int:puesto_id>/', views.puesto_detail, name='puesto_detail'),
    path('puesto/<int:puesto_id>/delete', views.delete_puesto, name='delete_puesto'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/create/', views.create_contacto, name='create_contacto'),
    path('contacto/<int:contacto_id>/', views.contacto_detail, name='contacto_detail'),
    path('contacto/<int:contacto_id>/delete', views.delete_contacto, name='delete_contacto')
]

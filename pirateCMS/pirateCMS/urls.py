"""
URL configuration for pirateCMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from cms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='welcome'),
    path('cases/', views.cases_list, name='cases-list'),
    path('cases/<int:id>/', views.case_detail, name='case-detail'),
    path('cases/add/', views.case_create, name='case-create'),
    path('cases/<int:id>/update/', views.case_update, name='case-update'),
    path('cases/<int:id>/delete/', views.case_delete, name='case-delete'),
    path('cases/<int:id>/add_service/', views.add_service, name='add-service'),
    path('update_service/<int:id>/', views.update_service, name='update-service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete-service'),
    path('default_methodology/', views.default_methodology, name='default-methodology'),
    path('methodologies/', views.methodologies_list, name='methodologies-list'),
    path('methodologies/<int:id>/update/', views.methodology_update, name='update-methodology'),
    path('methodologies/<int:id>/delete/', views.methodology_delete, name='delete-methodology'),
    path('methodologies/<int:id>/', views.methodology_detail, name='methodology-detail'),
]

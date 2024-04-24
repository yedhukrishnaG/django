"""
URL configuration for hello_django project.

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
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('hello/', views.print_hello_world, name='hello'),
    path('create/', views.create, name='create'),
   # path('edit/<pk>', views.edit, name='edit'),
    path('edit/<pk>', views.editnew, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
    path('list/', views.list, name='list'),
    path('menu/', views.menu, name='menu'),
    path('nonbt/', views.old_view, name='nonbt'),
    path('report/', views.report, name='report'),
    path('homepage/', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addrow/', views.addrow, name='addrow'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('newreport/', views.newreport, name='newreport'),
    path('newhomepage/', views.newhomepage, name='newhomepage'),
    path('', views.print_hello),
]

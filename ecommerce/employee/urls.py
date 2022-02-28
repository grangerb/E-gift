

from django.contrib import admin
from django.urls import include, path
from employee import views


urlpatterns = [

    path('add/',views.addEmloyee),
    path('view/',views.viewemployee),
    path('view/',views.viewemployee),
    path('delete/',views.deleteEmployee),
    path('update/',views.updateEmployee),



]

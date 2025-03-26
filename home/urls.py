
from django.contrib import admin
from django.urls import path
# from django.urls import path,include
from home import views


admin.site.site_header = "Django pro"
admin.site.site_title = "Welcome"
admin.site.index_title = "Welcome to the Admin Dash-board"
urlpatterns = [
   
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
]
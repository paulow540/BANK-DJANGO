
from django.views.generic import TemplateView

from django.urls import path, re_path, include
from myCityBank.userapp import views as user_view

urlpatterns = [
    re_path(r'^my_profile/(?P<user_id>\d+)/', user_view.myProfile, name= "my_profile"),
    re_path(r'^edit_profile/(?P<user_id>\d+)/', user_view.editmyProfile, name= "edit_profile"),
    re_path(r'^deactivate_profile/(?P<user_id>\d+)/', user_view.deactivatemyProfile, name= "deactivate_profile"),
    re_path(r'^manage_staff/', user_view.manageStaff, name= "manage_staff"),
    re_path(r'^manage_customer/', user_view.manageCustomer, name= "manage_customer"),





]

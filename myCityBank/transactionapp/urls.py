
from django.views.generic import TemplateView

from django.urls import path, re_path, include
from myCityBank.transactionapp import views as transact_view

urlpatterns = [
    re_path(r'^manage_account/(?P<user_id>\d+)/', transact_view.manageAccount, name= "manage_account"),
   





]

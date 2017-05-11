from django.conf.urls import url 
from . import views

urlpatterns = [
url (r'^$' , views.index , name='inedex'),
#make routes depends on offers id 
url (r'^(?p<offer_id>[0-9]+)$' , views.detail , name='detail'),


]
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view/$',views.profile_view, name ="view"),
    url(r'^edit/$',views.profile_edit,name="edit"),
    url(r'^password/$',views.editPassword,name="password"),
]
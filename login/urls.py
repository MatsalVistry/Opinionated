from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^signup/$',views.signup_view, name ="signup"),
    url(r'^loginpage/$', LoginView.as_view(template_name="login/loginpage.html"), name="loginpage"),
    url(r'^logoutpage/$', LogoutView.as_view(template_name="login/logoutpage.html"), name="logoutpage"),

]
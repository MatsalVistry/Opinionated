from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


urlpatterns = [
    url(r'^signup/$',views.signup_view, name ="signup"),
    url(r'^loginpage/$', LoginView.as_view(template_name="login/loginpage.html"), name="loginpage"),
    url(r'^logoutpage/$', LogoutView.as_view(template_name="login/logoutpage.html"), name="logoutpage"),
    url(r'^emailPassword/$', PasswordResetView.as_view(template_name="login/loginpage.html"), name="emailPassword"),
    url(r'^emailPasswordDone/$',PasswordResetDoneView.as_view(template_name="login/loginpage.html"), name="emailPasswordDone"),
    url(r'^emailPasswordConfirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',PasswordResetConfirmView, name="password_reset_confirm"),
    url(r'^reset/$', PasswordResetView.as_view(template_name="login/loginpage.html"), name="password_reset_complete"),


]
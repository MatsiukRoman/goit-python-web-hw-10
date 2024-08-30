from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import LoginForm

app_name = "app_auth"

urlpatterns = [
    path("signup/", views.RegisterViews.as_view(), name="signup"),
    path(
        "signin/",
        LoginView.as_view(
            template_name="app_auth/login.html",
            form_class=LoginForm,
            redirect_authenticated_user=True,
            next_page='/'
        ),
        name="signin",
    ),
    path("logout/", views.logoutuser, name="logout")
]

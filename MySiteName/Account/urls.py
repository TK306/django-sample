from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("info/", views.account_info_view, name="account_info"),
    path("change_password/", views.change_password_view, name="change_password"),
    path("change_username/", views.change_username_view, name="change_username"),
    path("delete_account/", views.delete_account_view, name="delete_account"),
]

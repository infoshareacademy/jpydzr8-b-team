from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),  # login/logout
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='online_library:main'), name='logout'),
]

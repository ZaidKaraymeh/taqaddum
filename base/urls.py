from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('add_blog/', views.add_blog, name="add_blog"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:id>', views.view_blog, name="view_blog"),

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', user_views.register, name="register"),
    # path('profile/', user_views.profile, name="profile"),
]
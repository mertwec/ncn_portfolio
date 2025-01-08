from django.urls import include, path

from user.view import LoginViewUser, LogoutViewUser

urlpatterns = [
    path("login/", LoginViewUser.as_view(), name="login"),
    path('logout/', LogoutViewUser.as_view(), name='logout')
    ]

from django.contrib.auth.views import LoginView, LogoutView

from ncn.settings import LOGIN_REDIRECT_URL


class LoginViewUser(LoginView):
    extra_context = {"title": "Login"}
    template_name = "registration/login.html"


class LogoutViewUser(LogoutView):
    next_page = LOGIN_REDIRECT_URL

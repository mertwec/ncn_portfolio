from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def main(request: HttpRequest):
    return render(request, template_name="base.html")


def resume(request: HttpRequest):
    return render(request, template_name="about_me/resume.html")   


def mock_api(request: HttpRequest):
    """for update serwer render.com"""
    return HttpResponse(content="Ok")
    
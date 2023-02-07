from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main(request:HttpRequest):
    return render(request, template_name="base.html")
    
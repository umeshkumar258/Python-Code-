from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Home Page")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Home Page!"

if __name__ == '__main__':
    app.run(port=5000)

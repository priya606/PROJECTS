from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path("",views.index,name="index"),
    path("about.html",views.about,name="about"),
    path("resume.html",views.resume,name="resume"),
    path("portfolio.html",views.portfolio,name="portfolio"),
    path("contact.html",views.contact,name="contact")
]


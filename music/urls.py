# music/urls.py
from django.conf.urls import url
from music import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^night$', views.NightcorePageView.as_view()),
    url(r'^ncs$', views.NCSPageView.as_view()),
    url(r'^aboutncs$', views.aboutncsPageView.as_view()),
    url(r'^aboutnight$', views.aboutnightPageView.as_view()),
    url(r'^register$' ,  views.registerPageView.as_view()),
    url(r'^login$' , views.loginPageView.as_view()),
]

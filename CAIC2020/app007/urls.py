from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('signup/', views.signup),
    path('covid19/', views.covid)
    # path('survey/', views.survey)
]

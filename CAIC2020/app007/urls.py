from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('login/', views.login)
    # path('survey/', views.survey)
]

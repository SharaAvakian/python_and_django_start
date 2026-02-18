from django.urls import path

from . import views

urlpatterns = [
    path('<int:month>', views.monthly_challenges_by_number,name="month_"),
    path('<str:month>', views.monthly_challenge),
]


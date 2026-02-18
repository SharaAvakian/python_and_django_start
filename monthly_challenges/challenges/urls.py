from django.urls import path

from . import views

urlpatterns = [
    path('<months>', views.monthly_challenges)
]
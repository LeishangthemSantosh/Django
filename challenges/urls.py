from django.urls import path
from . import views

urlpatterns = [
    # path('january', views.januray)
    path("", views.index, name='main-page'),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="monthly-challenge")
]
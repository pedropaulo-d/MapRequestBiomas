from django.urls import path
from .views import WaterURLView

urlpatterns = [
    path('water-url/', WaterURLView.as_view()),
]

from django.urls import path
from .views import *

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', GetSensorsView.as_view()),
    path('sensors/<pk>/', GetSensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]

from .models import Sensors, Measurment
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class GetSensorsView(ListCreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class GetSensorView(RetrieveUpdateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurment.objects.all()
    serializer_class = AddMeasurementSerializer

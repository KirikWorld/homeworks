from pyexpat import model
from rest_framework import serializers
from .models import Measurment, Sensors

# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['temperature', 'date']


class SensorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'describe']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(
        source='measurements', many=True, read_only=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'describe', 'measurement']
        
        
class AddMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['temperature', 'sensor']

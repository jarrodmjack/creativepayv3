from rest_framework import viewsets
from .models import Employee, TimePunch
from .serializers import EmployeeSerializer, TimePunchSerializer

class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class TimePunchAPIView(viewsets.ModelViewSet):
    queryset = TimePunch.objects.all()
    serializer_class = TimePunchSerializer

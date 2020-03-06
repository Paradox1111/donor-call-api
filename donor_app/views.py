from rest_framework import generics
from .serializers import StewardSerializer, DonorSerializer
from .models import Steward, Donor

class StewardList(generics.ListCreateAPIView):
    queryset = Steward.objects.all()
    serializer_class = StewardSerializer

class StewardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Steward.objects.all()
    serializer_class = StewardSerializer

class DonorList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class DonorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
from rest_framework import generics
from .serializers import ProfileSerializer, DonorSerializer, UserSerializer
from .models import Profile, Donor
from django.contrib.auth.models import User

class StewardList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StewardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DonorList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class DonorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
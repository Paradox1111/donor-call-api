from rest_framework import generics
from .serializers import DonorSerializer, UserSerializer
from .models import Donor
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
    def post(self, request, format=None):
        return Response("ok")
    def allowed_methods(self):
        """
        Return the list of allowed HTTP methods, uppercased.
        """
        self.http_method_names.append("post")
        self.http_method_names.append("delete")
        self.http_method_names.append("get")
        return [method.upper() for method in self.http_method_names
                if hasattr(self, method)]
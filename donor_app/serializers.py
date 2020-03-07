from rest_framework import serializers
from .models import Donor, Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'donors')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    donors = serializers.HyperlinkedRelatedField(
        view_name='donor_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Profile
        fields = ('user', 'donors')

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('id', 'orgName', 'lastname', 'phone', 'email', 'paymentnum', 'yeartotal', 'lastgift', 'lastgiftdate', 'nextlastgift', 'botsteward', 'nextlastgiftdate', 'comments')
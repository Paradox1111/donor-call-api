from rest_framework import serializers
from .models import Steward, Donor

class StewardSerializer(serializers.HyperlinkedModelSerializer):
    donors = serializers.HyperlinkedRelatedField(
        view_name='donor_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Steward
        fields = ('id', 'name', 'password', 'donors')

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('id', 'orgName', 'lastname', 'phone', 'email', 'paymentnum', 'yeartotal', 'lastgift', 'lastgiftdate', 'nextlastgift', 'botsteward', 'nextlastgiftdate', 'comments')
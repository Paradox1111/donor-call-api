from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('stewards/<int:pk>', views.StewardDetail.as_view(), name='steward_detail'),
    path('donors/<int:pk>', views.DonorDetail.as_view(), name='donor_detail'),
    path('stewards', views.StewardList.as_view(), name='steward_list'),
    path('donors', views.DonorList.as_view(), name='donor_list'),
]
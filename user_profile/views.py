from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import User_Profile
from .serializer import UserProfileSerializer, TestSerializer
# from .permissions import IsOwner
from rest_framework import filters


class UserProfileList(ListCreateAPIView):
    # permission_classes = (IsOwner,)
    queryset = User_Profile.objects.all()
    serializer_class = TestSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)


class UserProfileDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwner,)
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer


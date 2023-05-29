from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('', UserProfileList.as_view(), name='user_profile_list'),
    path('<int:pk>', UserProfileDetail.as_view(), name='user_profile_detail'),
]
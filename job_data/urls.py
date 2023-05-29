from django.urls import path
from .views import JobDataList, JobDataDetail

urlpatterns = [
    path('', JobDataList.as_view(), name='job_data_list'),
    path('<int:pk>', JobDataDetail.as_view(), name='job_data_detail'),
]
from django.urls import path
from .views import ColCityList, ColCityDetail

urlpatterns = [
    path('', ColCityList.as_view(), name='col_city_list'),
    path('<int:pk>', ColCityDetail.as_view(), name='col_city_detail'),
]
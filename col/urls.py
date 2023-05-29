from django.urls import path
from .views import ColList, ColDetail

urlpatterns = [
    path('', ColList.as_view(), name='col_list'),
    path('<int:pk>', ColDetail.as_view(), name='col_detail'),
]
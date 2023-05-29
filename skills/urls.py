from django.urls import path
from .views import SkillList, SkillDetail

urlpatterns = [
    path('', SkillList.as_view(), name='skill_list'),
    path('<int:pk>', SkillDetail.as_view(), name='skill_detail'),
]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect URL
    path('', lambda req: redirect('api/v1/job_data/')),

    # Login Endpoint
    path('api-auth', include("rest_framework.urls")),

    # Users Endpoint
    path('api/v1/users/', include('user_profile.urls')),

    # Job Data Endpoint
    path('api/v1/job_data/', include('job_data.urls')),

    # Skills Endpoint
    path('api/v1/skills/', include('skills.urls')),

    # Cost of Living (State) Endpoint
    path('api/v1/col/', include('col.urls')),

    # Cost of Living (City) Endpoint
    path('api/v1/col_city/', include('col_city.urls')),

    # JWT URLS
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import ColCity
from .serializer import ColCitySerializer
from django.db.models import Q

class ColCityList(ListCreateAPIView):
    queryset = ColCity.objects.all()
    serializer_class = ColCitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_state = self.request.query_params.getlist('state')
        search_query_state_code = self.request.query_params.getlist('state_code')
        search_query_city = self.request.query_params.getlist('city')

        # Search by one or multiple states
        if search_query_state:
            # Use Q objects to perform OR operation on multiple states
            filter_query = Q()
            for state in search_query_state:
                filter_query |= Q(state__icontains=state)
            queryset = queryset.filter(filter_query)

        # Search by one or multiple state codes
        if search_query_state_code:
            # Use Q objects to perform OR operation on multiple states
            filter_query = Q()
            for state_code in search_query_state_code:
                filter_query |= Q(state_code__icontains=state_code)
            queryset = queryset.filter(filter_query)

        # Search by one or multiple cities
        if search_query_city:
            # Use Q objects to perform OR operation on multiple cities
            filter_query = Q()
            for city in search_query_city:
                filter_query |= Q(city__icontains=city)
            queryset = queryset.filter(filter_query)

        return queryset


class ColCityDetail(RetrieveUpdateDestroyAPIView):
    queryset = ColCity.objects.all()
    serializer_class = ColCitySerializer

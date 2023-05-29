from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Col
from .serializer import ColSerializer
from django.db.models import Q

class ColList(ListCreateAPIView):
    queryset = Col.objects.all()
    serializer_class = ColSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_state = self.request.query_params.getlist('state')

        # Search by one or multiple states
        if search_query_state:
            # Use Q objects to perform OR operation on multiple states
            filter_query = Q()
            for state in search_query_state:
                filter_query |= Q(state__icontains=state)
            queryset = queryset.filter(filter_query)

        return queryset

class ColDetail(RetrieveUpdateDestroyAPIView):
    queryset = Col.objects.all()
    serializer_class = ColSerializer

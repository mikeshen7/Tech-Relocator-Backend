from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Job
from .serializer import JobSerializer
from django.db.models import Q


class JobDataList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_title = self.request.query_params.getlist('title', None)
        search_query_location = self.request.query_params.getlist('location', None)
        search_query_salary = self.request.query_params.get('salary', None)

        # search by one or more titles
        if search_query_title:
            # Use Q objects to perform OR operation on multiple states
            filter_query = Q()
            for title in search_query_title:
                filter_query |= Q(title__icontains=title)
            queryset = queryset.filter(filter_query)

        # search by one or more locations
        if search_query_location:
            # Use Q objects to perform OR operation on multiple states
            filter_query = Q()
            for location in search_query_location:
                filter_query |= Q(location__icontains=location)
            queryset = queryset.filter(filter_query)

        # Search by salary in range
        if search_query_salary:
            queryset = queryset.filter(
                Q(salary_low__lte=search_query_salary) & Q(salary_high__gte=search_query_salary)
            )

        return queryset

class JobDataDetail(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

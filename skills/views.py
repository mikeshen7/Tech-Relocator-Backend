from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Skill
from .serializer import SkillSerializer
from rest_framework.response import Response


class SkillList(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def list(self, request, *args, **kwargs):
        # save the keyword to search_query if endpoint is /?search
        search_query = self.request.query_params.get('search', None)

        # if keyword exists, return 1 list of associated skills
        if search_query:
            queryset = self.queryset.filter(title__icontains=search_query)
            skills_list = list(queryset.values_list('skills', flat=True))
            combined_skills = list(set(skill.lower() for skills in skills_list for skill in skills))
            return Response(combined_skills)

        # If no /?search parameter, return normal list of jobs/skills
        return super().list(request, *args, **kwargs)


class SkillDetail(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
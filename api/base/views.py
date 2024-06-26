from rest_framework.generics import ListAPIView
from .models import Company
from .serializers import CompanySerializer


class GetCompany(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

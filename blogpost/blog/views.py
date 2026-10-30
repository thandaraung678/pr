from rest_framework import viewsets
from .models import Branch, Country, Currency, Custodian, Department
from .serializers import BranchSerializer, CustodianSerializer 
from .serializers import CountrySerializer
from .serializers import CurrencySerializer, DepartmentSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all().order_by("currency_id")
    serializer_class = CurrencySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by("country_id")
    serializer_class = CountrySerializer


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all().order_by('department_id')
    serializer_class = DepartmentSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('branch_id')
    serializer_class = BranchSerializer


class CustodianViewSet(viewsets.ModelViewSet):
    queryset = Custodian.objects.all().order_by('custodian_id')
    serializer_class = CustodianSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BranchViewSet,
    CountryViewSet,
    CustodianViewSet,
    DepartmentViewSet,
    CurrencyViewSet,
)

router = DefaultRouter()

router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'custodians', CustodianViewSet, basename='custodian')

urlpatterns = [
    path('', include(router.urls)),
]

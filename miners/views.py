from rest_framework import filters, viewsets
from django.contrib.auth.models import User as Miner
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from lib code
from . import models, serializers

# Create your views here.
class MinerView(viewsets.ReadOnlyModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.MinerSerializer
    queryset = Miner.objects.all().order_by("date_joined")

    # permission_classes = (IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'last_name', 'first_name')
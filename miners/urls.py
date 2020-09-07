from . import views
from rest_framework import routers
from django.urls import path, include

# the router object
router = routers.DefaultRouter()

# add urls
router.register(r'miner', views.MinerView, 'Miner Info')

# all urls that can be visited
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import include, path
from charts.views import ChartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'charts',ChartViewSet)

urlpatterns=[path('',include(router.urls)),
]
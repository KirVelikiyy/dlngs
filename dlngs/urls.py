from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryView

router = DefaultRouter()
router.register(r'dictionaries', DictionaryView, basename='dictionary')

urlpatterns = [
    path('', include(router.urls))
]

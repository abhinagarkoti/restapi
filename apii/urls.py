from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apii import views

router = DefaultRouter()
router.register('Snippet', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
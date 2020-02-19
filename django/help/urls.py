from django.urls import path, include
from rest_framework.routers import DefaultRouter
from help import views

app_name = 'help'

router = DefaultRouter()
router.register(r'write', views.QuestionViewSet, basename='write')
router.register(r'img', views.HelpImageViewSet, basename='img')

urlpatterns = [
    path('', include(router.urls)),
]

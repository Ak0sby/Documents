from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

# DefaultRouter'ди түзүү
router = DefaultRouter()

# Бардык ViewSet'терди каттоо
router.register(r'users', AdminUserViewSet, basename='users')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'references', DocsViewSet, basename='references')


# URL үлгүлөрү
urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Токен алуу API
    path('login/', LoginView.as_view(), name='login'),


]

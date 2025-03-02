from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

# DefaultRouter'ди түзүү
router = DefaultRouter()

# Бардык ViewSet'терди каттоо
router.register(r'users', AdminUserViewSet, basename='users')
router.register(r'spravki', SpravkiViewSet, basename='spravki')
router.register(r'post_cpgu', PostCPGUViewSet, basename='post_cpgu')
router.register(r'treb_mil', TrebMilViewSet, basename='treb_mil')
router.register(r'vl_kart', VLkartViewSet, basename='vl_kart')
router.register(r'aktual', AktualViewSet, basename='aktual')
router.register(r'akt_sud', Akt_SudViewSet, basename='akt_sud')
router.register(r'post_prekr', Post_prekrViewSet, basename='post_prekr')
router.register(r'post_ad', Post_adViewSet, basename='post_ad')
router.register(r'istreb', IstrebViewSet, basename='istreb')


# URL үлгүлөрү
urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Токен алуу API
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
]

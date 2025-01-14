from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions


class RegisterView(APIView):

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:  # Админдин ролу текшерилгенде
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials or not an admin!"}, status=status.HTTP_400_BAD_REQUEST)


class BaseReportViewSet(viewsets.ModelViewSet):
    """
    Отчетторду башкаруу үчүн жалпы базалык класс.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Колдонуучуга тиешелүү отчетторду кайтаруу.
        """
        if self.request.user.is_staff:
            return self.model.objects.all()  # Админ үчүн баарын кайтаруу
        return self.model.objects.filter(user=self.request.user)  # Колдонуучу үчүн өз отчетторун кайтаруу

    def perform_create(self, serializer):
        """
        Отчетту түзгөндө колдонуучуну автоматтык түрдө кошуу.
        """
        serializer.save(user=self.request.user)


class SpravkiViewSet(BaseReportViewSet):
    model = Spravki
    serializer_class = SpravkiSerializer



class PostCPGUViewSet(BaseReportViewSet):
    model = PostCPGU
    serializer_class = PostCPGUSerializer



class TrebMilViewSet(BaseReportViewSet):
    model = TrebMil
    serializer_class = TrebMilSerializer



class VLkartViewSet(BaseReportViewSet):
    model = VLKart
    serializer_class = VLkartSerializer



class AktualViewSet(BaseReportViewSet):
    model = Aktual
    serializer_class = AktualSerializer



class Akt_SudViewSet(BaseReportViewSet):
    model = Akt_SUD
    serializer_class = Akt_SudSerializer



class Post_prekrViewSet(BaseReportViewSet):
    model = Post_prеkr
    serializer_class = Post_prekrSerializer



class Post_adViewSet(BaseReportViewSet):
    model = Post_ad
    serializer_class = Post_adSerializer



class IstrebViewSet(BaseReportViewSet):
    model = Istreb
    serializer_class = IstrebSerializer


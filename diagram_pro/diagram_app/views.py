from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *


class RegisterView(APIView):
    """
    Админ жана суперадмин жаңы колдонуучу кошот (Фамилия, логин, пароль менен).
    """
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    """
    Колдонуучу логин API (Фамилиясыз).
    """
    @swagger_auto_schema(request_body=LoginSerializer)  # Жаңы LoginSerializer колдонулду
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            INN = serializer.validated_data['INN']
            password = serializer.validated_data['password']

            user = authenticate(request, username=INN, password=password)
            if user:
                login(request, user)
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            return Response({"message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(APIView):
    """
    Суперадмин логин API (Фамилия, логин жана пароль менен кирүү).
    """
    @swagger_auto_schema(request_body=AdminLoginSerializer)  # Жаңы AdminLoginSerializer колдонулду
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            INN = serializer.validated_data['INN']
            password = serializer.validated_data['password']
            last_name = serializer.validated_data['last_name']

            user = authenticate(request, username=INN, password=password)

            if user and user.is_staff:  # Админ экени текшерилет
                if user.last_name.lower() == last_name.lower():  # Фамилияны текшерүү
                    login(request, user)
                    return Response({"message": "Admin login successful!"}, status=status.HTTP_200_OK)
                return Response({"message": "Incorrect last name!"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Invalid credentials or not an admin!"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BaseReportViewSet(viewsets.ModelViewSet):
    """
    Отчеттор үчүн базалык ViewSet.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Админ болсо баарын көрөт, колдонуучу өз отчетторун көрөт.
        """
        if self.request.user.is_staff:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Отчет түзүүдө колдонуучуну автоматтык түрдө белгилөө.
        """
        serializer.save(user=self.request.user)


# Ар бир модель үчүн ViewSet'тер
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

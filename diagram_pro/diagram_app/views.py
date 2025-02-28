from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from .serializers import *
from .models import *
from rest_framework.exceptions import PermissionDenied


# class RegisterView(APIView):
#     """
#     Админ жана суперадмин жаңы колдонуучу кошот (Фамилия, логин, пароль менен).
#     """
#     @swagger_auto_schema(request_body=UserSerializer)
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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


# class AdminLoginView(APIView):
#     """
#     Суперадмин логин API (Фамилия, логин жана пароль менен кирүү).
#     """
#     @swagger_auto_schema(request_body=AdminLoginSerializer)  # Жаңы AdminLoginSerializer колдонулду
#     def post(self, request):
#         serializer = AdminLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             INN = serializer.validated_data['INN']
#             password = serializer.validated_data['password']
#             last_name = serializer.validated_data['last_name']
#
#             user = authenticate(request, username=INN, password=password)
#
#             if user and user.is_staff:  # Админ экени текшерилет
#                 if user.last_name.lower() == last_name.lower():  # Фамилияны текшерүү
#                     login(request, user)
#                     return Response({"message": "Admin login successful!"}, status=status.HTTP_200_OK)
#                 return Response({"message": "Incorrect last name!"}, status=status.HTTP_400_BAD_REQUEST)
#
#             return Response({"message": "Invalid credentials or not an admin!"}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['patch'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('password')
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Пароль обновлен!'}, status=status.HTTP_200_OK)
        return Response({'error': 'Введите новый пароль!'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def update_info(self, request, pk=None):
        user = self.get_object()
        user.username = request.data.get('INN', user.username)
        user.last_name = request.data.get('last_name', user.last_name)
        user.save()
        return Response({'message': 'Данные обновлены!'}, status=status.HTTP_200_OK)



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

    def destroy(self, request, *args, **kwargs):
        """
        Колдонуучу өзүнүн гана отчетун өчүрө алат.
        """
        instance = self.get_object()
        if not request.user.is_staff and instance.user != request.user:
            raise PermissionDenied("Сиз бул отчетту өчүрө албайсыз!")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Колдонуучу өзүнүн гана отчетун өзгөртө алат.
        """
        instance = self.get_object()
        if not request.user.is_staff and instance.user != request.user:
            raise PermissionDenied("Сиз бул отчетту өзгөртө албайсыз!")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Колдонуучу өзүнүн гана отчетун жарым-жартылай өзгөртө алат.
        """
        instance = self.get_object()
        if not request.user.is_staff and instance.user != request.user:
            raise PermissionDenied("Сиз бул отчетту өзгөртө албайсыз!")
        return super().partial_update(request, *args, **kwargs)


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

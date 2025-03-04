from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from .serializers import *
from .models import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg import openapi


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
class DocsViewSet(BaseReportViewSet):
    model = Docs
    serializer_class = DocsSerializer


class ReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Жеке колдонуучунун отчет диаграммасын көрсөтүү",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Жеке колдонуучунун отчет диаграммасы",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'spravki': openapi.Schema(type=openapi.TYPE_INTEGER, description="Spravki отчетторунун саны"),
                        'post_cpgu': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post CPGU отчетторунун саны"),
                        'treb_mil': openapi.Schema(type=openapi.TYPE_INTEGER, description="Treb Mil отчетторунун саны"),
                        'vlkart': openapi.Schema(type=openapi.TYPE_INTEGER, description="VL Kart отчетторунун саны"),
                        'aktual': openapi.Schema(type=openapi.TYPE_INTEGER, description="Aktual отчетторунун саны"),
                        'akt_sud': openapi.Schema(type=openapi.TYPE_INTEGER, description="Akt Sud отчетторунун саны"),
                        'post_prekr': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post Prekr отчетторунун саны"),
                        'post_ad': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post Ad отчетторунун саны"),
                        'istreb': openapi.Schema(type=openapi.TYPE_INTEGER, description="Istreb отчетторунун саны"),
                    }
                )
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Аутентификация талап кылынат"
            ),
        }
    )
    @action(detail=True, methods=['get'])
    def get_user_report(self, request, pk=None):
        """
        Жеке колдонуучунун отчет диаграммасын алуу
        """
        user = request.user
        if user.id != int(pk) and not user.is_staff:
            return Response({"detail": "Сиздин бул ишти жасоого укугуңуз жок."}, status=status.HTTP_403_FORBIDDEN)

        # Колдонуучунун өзүнүн отчетторун алуу
        try:
            target_user = User.objects.get(id=pk)  # pk - бул колдонуучунун id
        except User.DoesNotExist:
            return Response({"detail": "Колдонуучу табылган жок."}, status=status.HTTP_404_NOT_FOUND)

        data = self.get_user_report_data(target_user.id)
        return Response(data)

    @swagger_auto_schema(
        operation_description="Бардык колдонуучулардын отчет диаграммасын көрсөтүү",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Бардык колдонуучулардын отчет диаграммасы",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'spravki': openapi.Schema(type=openapi.TYPE_INTEGER, description="Spravki отчетторунун саны"),
                        'post_cpgu': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post CPGU отчетторунун саны"),
                        'treb_mil': openapi.Schema(type=openapi.TYPE_INTEGER, description="Treb Mil отчетторунун саны"),
                        'vlkart': openapi.Schema(type=openapi.TYPE_INTEGER, description="VL Kart отчетторунун саны"),
                        'aktual': openapi.Schema(type=openapi.TYPE_INTEGER, description="Aktual отчетторунун саны"),
                        'akt_sud': openapi.Schema(type=openapi.TYPE_INTEGER, description="Akt Sud отчетторунун саны"),
                        'post_prekr': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post Prekr отчетторунун саны"),
                        'post_ad': openapi.Schema(type=openapi.TYPE_INTEGER, description="Post Ad отчетторунун саны"),
                        'istreb': openapi.Schema(type=openapi.TYPE_INTEGER, description="Istreb отчетторунун саны"),
                    }
                )
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Аутентификация талап кылынат"
            ),
        }
    )
    @action(detail=False, methods=['get'])
    def get_all_users_report(self, request):
        """
        Админдерге бардык колдонуучулардын отчетторун алуу мүмкүнчүлүгү
        """
        user = request.user
        if not user.is_staff:
            return Response({"detail": "Сиздин бул ишти жасоого укугуңуз жок."}, status=status.HTTP_403_FORBIDDEN)

        data = self.get_all_users_report_data()
        return Response(data)

    def get_user_report_data(self, user_id):
        """
        Белгилүү бир колдонуучунун отчетторун кайтаруу
        """
        docs = Docs.objects.filter(user_id=user_id)

        return {
            "spravki": docs.aggregate(models.Sum('spravki'))['spravki__sum'] or 0,
            "post_cpgu": docs.aggregate(models.Sum('postcpgu'))['postcpgu__sum'] or 0,
            "treb_mil": docs.aggregate(models.Sum('trebmil'))['trebmil__sum'] or 0,
            "vlkart": docs.aggregate(models.Sum('vlkart'))['vlkart__sum'] or 0,
            "aktual": docs.aggregate(models.Sum('aktual'))['aktual__sum'] or 0,
            "akt_sud": docs.aggregate(models.Sum('akt_sud'))['akt_sud__sum'] or 0,
            "post_prekr": docs.aggregate(models.Sum('postprekr'))['postprekr__sum'] or 0,
            "post_ad": docs.aggregate(models.Sum('postad'))['postad__sum'] or 0,
            "istreb": docs.aggregate(models.Sum('istreb'))['istreb__sum'] or 0,
        }

    def get_all_users_report_data(self):
        """
        Бардык колдонуучулардын отчетторун кайтаруу
        """
        docs = Docs.objects.all()
        report_data = {
            "spravki": docs.aggregate(models.Sum('spravki'))['spravki__sum'] or 0,
            "post_cpgu": docs.aggregate(models.Sum('postcpgu'))['postcpgu__sum'] or 0,
            "treb_mil": docs.aggregate(models.Sum('trebmil'))['trebmil__sum'] or 0,
            "vlkart": docs.aggregate(models.Sum('vlkart'))['vlkart__sum'] or 0,
            "aktual": docs.aggregate(models.Sum('aktual'))['aktual__sum'] or 0,
            "akt_sud": docs.aggregate(models.Sum('akt_sud'))['akt_sud__sum'] or 0,
            "post_prekr": docs.aggregate(models.Sum('postprekr'))['postprekr__sum'] or 0,
            "post_ad": docs.aggregate(models.Sum('postad'))['postad__sum'] or 0,
            "istreb": docs.aggregate(models.Sum('istreb'))['istreb__sum'] or 0,
        }
        return report_data

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    INN = serializers.CharField(source='username')  # username талаасын INN деп өзгөрттүк

    class Meta:
        model = User
        fields = ('INN', 'password', 'last_name', 'is_superuser')  # INN колдонулду
        extra_kwargs = {'password': {'write_only': True}}  # Пароль жоопто көрүнбөйт

    def validate_INN(self, value):
        """ INN (Логин) 14 орундуу сан болушу керек. """
        if len(value) != 14:
            raise serializers.ValidationError("INN 14 символдон турушу керек!")
        if not value.isdigit():
            raise serializers.ValidationError("INN тек гана сан болушу керек!")
        return value

    def validate_password(self, value):
        """ Паролдун узундугун текшерүү: 15 орундан көп болбошу керек. """
        if len(value) > 15:
            raise serializers.ValidationError("Пароль 15 символдон ашпашы керек!")
        return value

    def validate_last_name(self, value):
        """ Фамилия 60 символдон ашпашы керек. Эгер аз болсо, көйгөй жаратпайт. """
        if len(value) > 60:
            raise serializers.ValidationError("Фамилия 60 символдон ашпашы керек!")
        return value

    def create(self, validated_data):
        """ Колдонуучуну түзүү (INN → username катары колдонулат). """
        validated_data['username'] = validated_data.pop('INN')  # INN'ди username кылып сактайбыз
        password = validated_data.pop('password')  # Паролду бөлүп алабыз
        is_superuser = validated_data.pop('is_superuser', False)  # Админ же жоктугун алабыз

        user = User(**validated_data)  # Колдонуучуну түзөбүз
        user.set_password(password)  # Паролду шифрлейбиз

        if is_superuser:  # Эгер бул супер админ болсо
            user.is_superuser = True
            user.is_staff = True  # Админдер үчүн is_staff да керек

        user.save()
        return user




class LoginSerializer(serializers.Serializer):
      INN = serializers.CharField()
      password = serializers.CharField()


class AdminLoginSerializer(serializers.Serializer):
      INN = serializers.CharField()
      password = serializers.CharField()
      last_name = serializers.CharField()



class SpravkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spravki
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']  # user жана created_at автоматтык түрдө белгиленет


class PostCPGUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCPGU
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']  # user жана created_at автоматтык түрдө белгиленет


class TrebMilSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrebMil
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class VLkartSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLKart
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class AktualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktual
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class Akt_SudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akt_SUD
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class Post_prekrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_prеkr
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class Post_adSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_ad
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class IstrebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Istreb
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # username талаасын INN деп өзгөрттүк

    class Meta:
        model = User
        fields = ('username', 'password', 'last_name', 'is_superuser')  # INN колдонулду
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


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)


    def create(self, validated_data):
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



class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']  # user жана created_at автоматтык түрдө белгиленет


class ReportSerializer(serializers.Serializer):
    spravki = serializers.IntegerField()
    post_cpgus = serializers.IntegerField()
    treb_mils = serializers.IntegerField()
    vlkart = serializers.IntegerField()
    aktual = serializers.IntegerField()
    akt_sud = serializers.IntegerField()
    post_prekr = serializers.IntegerField()
    post_ad = serializers.IntegerField()
    istreb = serializers.IntegerField()

    class Meta:
        fields = ['spravki', 'post_cpgu', 'treb_mil', 'vlkart', 'aktual', 'akt_sud', 'post_prekr', 'post_ad', 'istreb']
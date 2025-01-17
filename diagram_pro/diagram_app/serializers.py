from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_username(self, value):
        """
        Логиндин узундугун текшерүү: 14 сан болушу керек.
        """
        if len(value) != 14:
            raise serializers.ValidationError("Логин 14 символдон турушу керек!")
        if not value.isdigit():
            raise serializers.ValidationError("Логин тек гана сан болушу керек!")
        return value

    def validate_password(self, value):
        """
        Паролдун узундугун текшерүү: 15 орундан көп болбошу керек.
        """
        if len(value) > 15:
            raise serializers.ValidationError("Пароль 15 символдон ашпашы керек!")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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

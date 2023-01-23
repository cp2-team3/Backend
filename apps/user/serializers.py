from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import date
from apps.user.models import User
from django.contrib.auth.models import update_last_login


class SignUpSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    password_check = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User #.models의 User
        fields = ['id', 'nickname', 'name', 'email', 'password', 'password_check', 'sex', 'birth', 'contact']
 
    def validate(self, attrs):
        """
        회원가입 데이터를 검증합니다.
        1. 아이디 중복 체크
        2. 비밀번호
        """

        if User.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError({'id': '이미 존재하는 아이디입니다.'})

        if attrs['password'] != attrs['password_check']:
            raise serializers.ValidationError({'password': '비밀번호와 비밀번호 확인이 일치하지 않습니다.'})

        attrs['created_at'] = date.today()

        return attrs    
    
    def create(self, validated_data):
        """ validated_data를 받아 유저를 생성한 후 토큰을 반환합니다. """        
        password = validated_data.get('password')
        # 유저 생성
        user = User(                
            id = validated_data['id'],
            password = password,
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            sex = validated_data['sex'],
            birth = validated_data['birth'],
            contact = validated_data['contact'],
            email = validated_data['email'],    
        )
        user.set_password(password)
        user.save()
        return user

   
class SignInSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        user = authenticate(**data)
        if user:
            update_last_login(None, user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh = str(token)
            access = str(token.access_token)
            data = {
                'user': user.id,
                'refresh': refresh,
                'access': access,
            }
            return data

        raise serializers.ValidationError("No active account found with the given credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model = User
          fields = '__all__'

    
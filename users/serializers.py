from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)  # 유효한 데이터로 사용자 생성
        password = user.password
        user.set_password(password)  # 사용자 비밀번호 해싱
        user.save()  # 해싱된 비밀번호 저장
        return user
        
    def update(self, validated_data):  # 사용자 정보 변경
        user = super().create(validated_data)  # 유효한 데이터로 사용자 생성
        password = user.password
        user.set_password(password)  #사용자 비밀번호 해싱
        user.save()  # 해싱된 비밀번호 저장
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username  # 사용자 아이디를 보이게 할 거임
        # ...

        return token
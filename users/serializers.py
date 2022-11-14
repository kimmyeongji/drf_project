from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) #비밀번호 해싱
        user.save() #database에 해싱된 비밀번호 저장
        return user

    def update(self, validated_data):
        user = super().update(validated_data)
        password = user.password
        user.set_password(password) #비밀번호 해싱
        user.save() #database에 해싱된 비밀번호 저장
        return user
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): #view.py에서 import하는 내용, simple-jwt의 기본제공 Token...Serializer 상속
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        token['email'] = user.email #token의 사용자 이메일 추가
        token['token_message'] = 'customized token message' #token에 삽입할 메시지 입력
 
        return token
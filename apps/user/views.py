from apps.user.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SignUpSerializer, SignInSerializer, UserSerializer

# Create your views here.

# 회원가입
class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  
class UserSignInView(generics.GenericAPIView):
    """ 로그인 뷰 - 요청을 보낸 사용자를 인증합니다. """
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            access_token = serializer.validated_data['access']
            refresh_token = serializer.validated_data['refresh']
            res = Response(
                {
                    "user": user,
                    "token": {
                        "refresh": refresh_token,
                        "access": access_token,
                    },
                },
                status=status.HTTP_200_OK,
            ) 

            #쿠키데이터 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserWithdrawalView(generics.DestroyAPIView):
    """ 회원탈퇴 뷰 - 요청을 보낸 사용자를 삭제합니다. """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from apps.user.models import User
from apps.board.models import Board

class UserSexStatsView(APIView):
    
    def get(self, request):
        male = User.objects.filter(sex='Male').count()
        female = User.objects.filter(sex='Female').count()
        
        return Response({'남성 유저 수' : male, '여성 유저 수' : female}, status=status.HTTP_200_OK)

class UserAgeStatsView(APIView):

    def get(self, request):
        result = {}
        today = datetime.now().date()
        for i in range(8):
            start_date = today - timedelta(days=365*(i+1)*10)
            end_date = today - timedelta(days=365*i*10)
            count = (User.objects.filter(birth__range=(start_date, end_date)).count())

            result[str(i*10)+'대 유저 수'] = count
        
        result['80대 이상 유저 수'] = User.objects.filter(birth__lte=today-timedelta(days=365*80)).count()
        result['10대 미만 유저 수'] = result.pop('0대 유저 수')
        
        return Response({'result' : result}, status=status.HTTP_200_OK)

class UserJoinTimeStatsView(APIView):

    def get(self, request):
        result = {}
        today = datetime.now().date()
        for i in range(5):
            start_date = today - timedelta(days=365*(i+1))
            end_date = today - timedelta(days=365*i)
            count = (User.objects.filter(date_joined__range=(start_date,end_date)).count())

            result[str(i)+'년 이상 '+str(i+1)+'년 미만 이용 유저 수'] = count
        
        result['5년 이상 이용 유저 수'] = User.objects.filter(date_joined__lte=today-timedelta(days=365*5)).count()

        return Response({'result' : result}, status=status.HTTP_200_OK)

class BoardSexStatsView(APIView):

    def get(self, request):
        male = Board.objects.filter(user__sex='Male').count()
        female = Board.objects.filter(user__sex='Female').count()
        
        return Response({'남성 유저 수' : male, '여성 유저 수' : female}, status=status.HTTP_200_OK)

class BoardAgeStatsView(APIView):

    def get(self, request):
        result = {}
        today = datetime.now().date()
        for i in range(8):
            start_date = today - timedelta(days=365*(i+1)*10)
            end_date = today - timedelta(days=365*i*10)
            count = (Board.objects.filter(user__birth__range=(start_date, end_date)).count())

            result[str(i*10)+'대 유저 수'] = count

        result['80대 이상 유저 수'] = Board.objects.filter(user__birth__lte=today-timedelta(days=365*80)).count()
        result['10대 미만 유저 수'] = result.pop('0대 유저 수')

        return Response({'result' : result}, status=status.HTTP_200_OK)

class BoardJoinTimeStatsView(APIView):

    def get(self, request):
        result = {}
        today = datetime.now().date()
        for i in range(5):
            start_date = today - timedelta(days=365*(i+1))
            end_date = today - timedelta(days=365*i)
            count = (Board.objects.filter(user__date_joined__range=(start_date,end_date)).count())

            result[str(i)+'년 이상 '+str(i+1)+'년 미만 이용 유저 수'] = count
        
        result['5년 이상 이용 유저 수'] = Board.objects.filter(user__date_joined__lte=today-timedelta(days=365*5)).count()

        return Response({'result' : result}, status=status.HTTP_200_OK)
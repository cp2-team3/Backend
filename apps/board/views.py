from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly, IsStaffOrReadOnly
from rest_framework import viewsets
from .models import Board, Comment


from .models import Board
from .serializers import BoardSerializer, CommentSerializer

import logging

# logger = logging.getLogger('json_logger')
logger = logging.getLogger('db')

class BoardView(ListCreateAPIView):
    
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        logger.info("GET access Board List", extra={'request':request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info("POST access Board Creation", extra={'request':request})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        logger.info("GET access Board Detail", extra={'request':request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
            
        logger.info("PUT access Board Detail", extra={'request':request})
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        logger.info("PATCH access Board Detail", extra={'request':request})
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        logger.info("DELETE access Board Detail", extra={'request':request})
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# (댓글) Comment 보여주기, 수정하기, 삭제하기 모두 가능
class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer): #유저 정보 전달
        serializer.save(user = self.request.user)

# (댓글) List Route
CommentViewSet_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# (댓글) Detail Route
CommentViewSet_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})        

from django.contrib.auth.hashers import make_password

from rest_framework                  import status
from rest_framework.test             import APIClient, APITestCase
# from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models  import User
from apps.board.models import Board
# from apps.board.models import Comment
# from django.db import models


class TestBoard(APITestCase):
    '''
        자유게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.user = User.objects.create(
            id       =  "codestates",
            password = make_password("123"),
            nickname = "codestates",
            name     = "aaa",
            email    = "aaa@gmail.com",
            birth    = "2023-01-01",
        )
           
        self.user1 = User.objects.create(
            id       =  "codestates2", #id 다르게
            password = make_password("123"),
            nickname = "codestates",
            name     = "aaa",
            email    = "aaa1@gmail.com", #email 다르게
            birth    = "2023-01-01",
        )
        
        self.board =  Board.objects.create(
            id      = 1,
            user_id = "codestates", #user의 id
            title   = "게시판 제목 1",
            content = "게시판 내용 1",
        )
        
        # self.comment = Comment.objects.create(
        #     id=1,
        #     blog = self.board,
        #     user = self.user ,
        #     created_at = models.DateField(auto_now_add=True),
        #     comment = "댓글 to 게시판 내용 1",
        # )
        
        self.board_url = "/api/board/"
        self.board_comment_url = "/api/board/comment/"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        User.objects.all().delete()
        Board.objects.all().delete()


    # 게시판 리스트 조회(로그인 했을경우)
    def test_board_list_login_success(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.response = self.client.get(self.board_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    

    # 게시판 리스트 조회(로그인 안했을경우)
    def test_board_list_success(self):
        self.response = self.client.get(self.board_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    # 자유게시판 상세페이지 조회(로그인했을경우)
    def test_board_detail_signin_success(self):
       
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.response = self.client.get(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 상세페이지 조회(로그인안했을경우)
    def test_board_detail_success(self):

        self.response = self.client.get(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 작성(로그인했을경우)
    def test_board_create_login_success(self):
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        data = {
            "title"  : "게시판 추가 제목 2",
            "content": "게시판 추가 내용 2"
            
            
        }
        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 자유게시판 글 작성 실패(로그인 안했을경우)
    def test_board_create_fail(self):
        data = {
            "title"  : "게시판 추가 제목 2",
            "content": "게시판 추가 내용 2"
        }

        self.response = self.client.post(self.board_url, data, format='json')
        
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 자유게시판 글 업데이트성공(본인의 글인 경우)
    def test_board_update_login_success(self):
        
       
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        data = {
            "title"  : "공지사항 제목1 수정",
            "content": "공지사항 내용1 수정"
        }

        self.response = self.client.put(f'{self.board_url}{self.board.id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 업데이트실패(본인글이 아닌 경우)
    def test_notice_update_fail(self):
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        
        data = {
            "title": "공지사항 제목1 수정",
            "content": "공지사항 내용1 수정",
        }

        self.response = self.client.put(f'{self.board_url}{self.board.id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."})

    # 자유게시판 작성글 삭제(본인글인경우)
    def test_board_delete_own_success(self):
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.response = self.client.delete(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    # 자유게시판 작성글 삭제(본인글이 아닌경우)
    def test_board_delete_fail(self):
       
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        
        self.response = self.client.delete(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."})
     
    
    # # 자유게시판_코멘트 리스트 조회(로그인 했을경우)
    # def test_board_comment_list_login_success(self):
    #     self.client = APIClient()
    #     self.client.force_authenticate(user=self.user)
        
    #     self.response = self.client.get(self.board_comment_url, format='json')
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    

    # # 자유게시판_코멘트 리스트 조회(로그인 안했을경우)
    # def test_board_comment_list_success(self):
    #     self.response = self.client.get(self.board_comment_url, format='json')
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    
    # # 자유게시판_코멘트 상세페이지 조회(로그인했을경우)
    # def test_board_comment_detail_signin_success(self):
       
    #     self.client = APIClient()
    #     self.client.force_authenticate(user=self.user)
        
    #     self.response = self.client.get(f'{self.board_comment_url}{self.board.id}', format='json')
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # # 자유게시판_코멘트 상세페이지 조회(로그인안했을경우)
    # def test_board_comment_detail_success(self):

    #     self.response = self.client.get(f'{self.board_comment_url}{self.board.id}', format='json')
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    # 댓글 작성 성공    
    # 댓글 작성 실패  
    # 댓글 업데이트성공(본인의 글인 경우)
    # 댓글 업데이트실패(본인글이 아닌 경우)
    # 댓글 삭제(본인글인경우)
    # 댓글 삭제(본인글이 아닌경우)
    
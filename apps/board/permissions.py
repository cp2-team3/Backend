from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    has_permission : 인증된 사용자(로그인한 유저)에 한하여 목록조회/포스트 등록 가능
    ERR01
    """
    message = "[Access Denied: ERR01] 접근 권한이 없습니다."
     
    def has_permission(self, request, view):  
        return bool(
            request.method in permissions.SAFE_METHODS or
            (request.user and
            request.user.is_authenticated)
        )


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    has_object_permission : 작성자 외 읽기 권한만 부여
    GET, OPTION, HEAD 요청일 때는 그냥 허용 (읽기 권한 요청이 들어오면 허용)
    DELETE, PATCH 일 때는 현재 사용자(request.user)와 객체가 참조 중인 사용자(객체(Blog)의 user)가 일치할 때마다 허용 
    """
    message = "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."
    
    def has_object_permission(self, request, view, obj):
         
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user 
    
    
class IsStaffOrReadOnly(permissions.BasePermission):
    """
    운영 등급 회원(is_staff=True) 에게 모든 권한을 허용, 일반 회원은 읽기만 가능
    운영자 : CRUD
    일반 회원 : R
    ERR03
    """
    message = "[Access Denied: ERR03] 게시글 등록, 수정, 삭제 권한이 없습니다."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_superuser)
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # has_permission
    def has_permission(self, request, view): #  인증된 사용자에 한하여 목록조회/포스트 등록 가능
        return request.user and request.user.is_authenticated
    # has_object_permission
    def has_object_permission(self, request, view, obj):
        #  GET, OPTION, HEAD 요청일 때는 그냥 허용 # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # DELETE, PATCH 일 때는 현재 사용자와 객체가 참조 중인 사용자가 일치할 때마다 허용 # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
        return obj.user == request.user 
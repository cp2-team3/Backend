❗️*Django(DRF) 백엔드 서비스*❗️
-----------------------

## *구현 사항*
- 게시판(User + 게시글)
    - 데이터
        - 회원 정보
            - 고객명, 성별, 생년월일, 연락처(email 또는 전화번호), 가입일, 마지막 접속일
    - REST API 기능
        - 게시판
        - 회원가입, 로그인, 회원탈퇴
    - 게시글의 수정권한은 작성자만 가질 수 있습니다.
- 유닛테스트
    - User 앱과 Board 앱에 대한 테스트
- 집계 기능
    - 남녀별, 연령별, 이용시간별
    - 집계 기능을 통해 현재 게시판과 유저에 대한 통계 확인
- 로그 기능
    - 사용자의 게시판 활동에 대한 로그
    - 암호화
    - 문자열 압축, 로그 파일 압축
- 더미데이터 생성
    - 회원가입 더미 데이터
    - 게시글 더미 데이터
- AWS EC2 배포
    - uWSGI, NginX 
    - 메인 페이지
    <img width="500" alt="스크린샷 2023-03-08 오후 9 51 24" src="https://user-images.githubusercontent.com/62207156/223719463-51d0fb8b-bf8a-4013-83e9-8fe6cfa5ff3a.png">
    
    - 회원가입 페이지
    <img width="500" alt="스크린샷 2023-03-08 오후 9 52 11" src="https://user-images.githubusercontent.com/62207156/223719838-20349a5f-e562-4ba1-8b15-4e4b3a22aa99.png">
    
    - 로그인 페이지
    <img width="500" alt="스크린샷 2023-03-08 오후 9 51 59" src="https://user-images.githubusercontent.com/62207156/223719647-6c09d44f-0095-423f-8477-97d49b6c2adc.png">
    
    - 게시판 페이지
    <img width="500" alt="스크린샷 2023-03-08 오후 9 52 35" src="https://user-images.githubusercontent.com/62207156/223720042-2f791cc7-f096-4e27-8d8d-3fb011f9593a.png">
    
    - 집계 페이지
    <img width="500" alt="스크린샷 2023-03-08 오후 9 52 26" src="https://user-images.githubusercontent.com/62207156/223720149-d32c1fb9-6ff9-42b9-affb-3beebd3b4e97.png">

## *기술 스택*
- MySQL
- DRF
- Python
- AWS EC2

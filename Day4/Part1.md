 
## Pystgram 기획  

### 사진 파트

- 개별 사진 보기 : /photos/<사진 ID="">/
- 사진에 좋아요 누르기 : /photos/<사진 ID="">/like/
- 사진에 댓글 달기 : /photos/<사진 ID="">/comment/
- 사진에 달린 댓글 가져오기 : /photos/<사진 ID="">/get_comments/
- 사진에 달린 댓글 지우기 : /photos/<사진 ID="">/comment/<댓글 ID="">/delete/
- 사진에 태그 달기 : /photos/<사진 ID="">/tag/
- 인기 사진 : /popular/
- 이용자 개별 타임라인 : /timeline/
- 특정 이용자가 올린 사진 : /users/<이용자 ID="">/
- 사진 삭제 : /photos/<사진 ID=">/delete/

### USER 파트

- URL: /accounts/registration/ (Django 에서 따로 설정 안하면 쓰게되는 기본 주소이다.)
- 프로필 보기: /users/<이용자 ID="">/
- 팔로잉 페이지: /users/<이용자 ID="">/following
- 팔로워 페이지: /users/<이용자 ID="">/followers
- 구독하기: /users/<이용자 ID="">/follow



### 페이지 구성

**상위 페이지**

- 첫 페이지
- 사진 올리기 
- 타임라인
- 이용자 프로필
- 인기사진

**하위 페이지**

- 첫 페이지 
	- ID/ 비밀번호 찾기
	- 회원가입
	- 로그인 

- 타임라인,사진 올리기, 이용자 프로필, 인기 사진
	- 사진보기
		- 사진 지우기
		- 태그 달기
		- 좋아요 표시
		- 댓글 남기기
		- 댓글 지우기

- 이용자 프로필
	- 로그아웃
	- 회원탈퇴
	- 계정 설정 및 프로필 수정
	- 구독하기 
	- 구독 중인 이용자 목록
	- 구독자 목록


	




























from django.urls import path
from notice.views import nbase_views, notice_views, ncomment_views, nanswer_views

urlpatterns = [
    
    ### 공지 관련
    # http://127.0.0.1:8000/notice/
    
    # 공지 게시판 홈페이지
    path('', nbase_views.notice_index, name="notice_index"), ##
    
    # 공지 게시글 자세히 보기
    # http://127.0.0.1:8000/notice/notice_id/
    path("<int:notice_id>/", nbase_views.notice_detail, name="notice_detail"),
    
    
    
    # 공지 생성 폼
    # http://127.0.0.1:8000/notice/create/
    path("create/", notice_views.notice_create, name="notice_create"), 
    
    # 공지 수정
    # http://127.0.0.1:8000/notice/update/notice_id/
    path("update/<int:notice_id>", notice_views.notice_update, name="notice_update"),
    
    # 공지 삭제
    # http://127.0.0.1:8000/notice/delete/notice_id/
    path("delete/<int:notice_id>", notice_views.notice_delete, name="notice_delete"), # detail과 index로 삭제 후 리다이렉트
    
    
    
    ### 공지게시물의 질문댓글생성 폼 ???????????????????
    # http://127.0.0.1:8000/notice/answer/create/1/
    path("answer/create/<int:notice_id>/", nanswer_views.notice_answer_create, name="notice_answer_create"),
    
    # http://127.0.0.1:8000/notice/answer/update/1/
    path("answer/update/<int:answer_id>/", nanswer_views.notice_answer_update, name="notice_answer_update"),
    
    # http://127.0.0.1:8000/notice/answer/delete/1/
    path("answer/delete/<int:answer_id>/", nanswer_views.notice_answer_delete, name="notice_answer_delete"),
    

    
    ### comment 관련
    # 공지 게시물의 댓글 작성 폼
    # http://127.0.0.1:8000/notice/comment/create/notice/notice_id/
    path("comment/create/notice/<int:notice_id>/", ncomment_views.comment_notice_create, name="comment_notice_create"),
    
    # http://127.0.0.1:8000/notice/comment/update/notice/comment_id/
    path("comment/update/notice/<int:comment_id>/", ncomment_views.comment_notice_update, name="comment_notice_update"),
    
    # http://127.0.0.1:8000/notice/comment/delete/notice/comment_id/
    path("comment/delete/notice/<int:comment_id>/", ncomment_views.comment_notice_delete, name="comment_notice_delete"),
    

    
    # 공지 게시물의 댓글의 댓글답변 작성 폼
    # http://127.0.0.1:8000/notice/comment/create/answer/answer_id/ 
    path("comment/create/answer/<int:answer_id>/", ncomment_views.comment_answer_ncreate, name="comment_answer_ncreate"),
    
    # http://127.0.0.1:8000/notice/comment/update/answer/comment_id/       comment_answer_update
    path("comment/update/answer/<int:comment_id>/", ncomment_views.comment_answer_nupdate, name="comment_answer_nupdate"),
    
    # http://127.0.0.1:8000/notice/comment/delete/answer/comment_id/       comment_answer_delete
    path("comment/delete/answer/<int:comment_id>/", ncomment_views.comment_answer_ndelete, name="comment_answer_ndelete"),

]

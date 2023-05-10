from django.urls import path
from bulletin.views import base_views, bulletin_views, answer_views, comment_views, vote_views

urlpatterns = [
    
    # http://127.0.0.1:8000/bulletin/
    ### bulletin(게시) 사이트 관련
    path("", base_views.bulletin_index, name="bulletin_index"),
    
    # http://127.0.0.1:8000/bulletin/bulletin_id/
    path("<int:bulletin_id>/", base_views.bulletin_detail, name="bulletin_detail"), # detail은 question_detail.html 참조
    
    
    
    # http://127.0.0.1:8000/bulletin/create/
    path("create/", bulletin_views.bulletin_create, name="bulletin_create"), # question_form.html 을 참조
    
    # http://127.0.0.1:8000/bulletin/update/1/
    path("update/<int:bulletin_id>", bulletin_views.bulletin_update, name="bulletin_update"), # question_update.html 을 참조
    
    # http://127.0.0.1:8000/bulletin/delete/1/
    path("delete/<int:bulletin_id>", bulletin_views.bulletin_delete, name="bulletin_delete"), # detail과 index로 삭제 후 리다이렉트
    
    
    
    ### answer 관련
    
    # http://127.0.0.1:8000/bulletin/answer/create/1/
    path("answer/create/<int:bulletin_id>/", answer_views.bulletin_answer_create, name="bulletin_answer_create"),
    
    # http://127.0.0.1:8000/bulletin/answer/update/1/
    path("answer/update/<int:answer_id>/", answer_views.bulletin_answer_update, name="bulletin_answer_update"),
    
    # http://127.0.0.1:8000/bulletin/answer/delete/1/
    path("answer/delete/<int:answer_id>/", answer_views.bulletin_answer_delete, name="bulletin_answer_delete"),
    
    
    
    
    ### comment 관련
    # 'bulletin'에 대한 comment
    # http://127.0.0.1:8000/bulletin/comment/create/bulletin/bulletin_id/
    path("comment/create/bulletin/<int:bulletin_id>/", comment_views.comment_bulletin_create, name="comment_bulletin_create"),
    
    # http://127.0.0.1:8000/bulletin/comment/update/bulletin/comment_id/       comment_question_update
    path("comment/update/bulletin/<int:comment_id>/", comment_views.comment_bulletin_update, name="comment_bulletin_update"),
    
    # http://127.0.0.1:8000/bulletin/comment/delete/bulletin/comment_id/       comment_question_delete
    path("comment/delete/bulletin/<int:comment_id>/", comment_views.comment_bulletin_delete, name="comment_bulletin_delete"),
    
    
    # 'answer'에 대한 comment
    # http://127.0.0.1:8000/bulletin/comment/create/answer/answer_id/       comment_answer_create
    path("comment/create/answer/<int:answer_id>/", comment_views.comment_answer_create, name="comment_answer_create"),
    
    # http://127.0.0.1:8000/bulletin/comment/update/answer/comment_id/       comment_answer_update
    path("comment/update/answer/<int:comment_id>/", comment_views.comment_answer_update, name="comment_answer_update"),
    
    # http://127.0.0.1:8000/bulletin/comment/delete/answer/comment_id/       comment_answer_delete
    path("comment/delete/answer/<int:comment_id>/", comment_views.comment_answer_delete, name="comment_answer_delete"),
    
    
    ### vote
    # http://127.0.0.1:8000/bulletin/bulletin/vote/bulletin_id(1)/
    path("bulletin/vote/<int:bulletin_id>", vote_views.vote_bulletin, name="vote_bulletin"),
    
    # http://127.0.0.1:8000/bulletin/answer/vote/response_id/
    path("answer/vote/<int:answer_id>", vote_views.vote_answer, name="vote_answer"),
]

from django.db import models
from users.models import User


# 공지사항
# notice : 공지내용
class Notice(models.Model):
    title = models.CharField(verbose_name="공지", max_length=200)
    category = models.CharField(verbose_name="카테고리", max_length=50, default="")
    content = models.TextField(verbose_name="공지글")
    image = models.ImageField(blank=True, null=True, verbose_name="공지물이미지")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="글쓴이", related_name="notice_author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True)
    view_cnt = models.BigIntegerField(default=0) # 조회수
    
    def __str__(self) -> str:
        return self.title


# 공지사항 조회수
class NoticeCount(models.Model):
    ip = models.CharField(max_length=30)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.ip



# 공지댓글
class NoticeAnswer(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="질문댓글")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="글쓴이", related_name="question_author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True) # auto_now: 글을 수정할 때마다 자동으로 입력



# 질문댓글에 대한 코멘트
class NoticeComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True) # auto_now: 글을 수정할 때마다 자동으로 입력
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(NoticeAnswer, on_delete=models.CASCADE, null=True, blank=True)
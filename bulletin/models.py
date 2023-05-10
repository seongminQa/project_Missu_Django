from django.db import models
from taggit.managers import TaggableManager
from users.models import User


# 게시글도 쓰고 답변도 달수있는 (질문모델)
# 제목(char), 내용(TextField), 작성날짜, 수정날짜 - DateTimeField
class Bulletin(models.Model):
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(blank=True, null=True, verbose_name="게시물이미지")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자", related_name="author_bulletin")
    # related_name 추가한 이유 -> 테이블의 관계에서 질문에 대한 추천을 하는 사람은 User이고 voter와 author을 구분하기 위함..?
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True) # auto_now: 글을 수정할 때마다 자동으로 입력
    voter = models.ManyToManyField(User, related_name="voter_bulletin", verbose_name="추천수") # 좋아요
    # ManyToMany 필드로 받은 이유, 질문번호 1,2,3,4번에 User 1,2,3,4 각자가 추천을 하는경우.. DB에 테이블을 따로 만들어준다. 질문id에 userid가 들어가게 된다.
    # tags = TaggableManager()
    view_cnt = models.BigIntegerField(default=0) # 조회수
    
    def __str__(self) -> str:
        return self.title


class BulletinCount(models.Model):
    ip = models.CharField(max_length=30)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.ip


class BulletinAnswer(models.Model):
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(blank=True, null=True, verbose_name="답변글이미지")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자", related_name="author_response")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True) # auto_now: 글을 수정할 때마다 자동으로 입력
    voter = models.ManyToManyField(User, related_name="voter_answer", verbose_name="추천수") # 좋아요


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(blank=True, null=True, verbose_name="코멘트이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜") # auto_now_add: 글이 쓰는 처음 등록될 때 자동으로 입력됨
    modified_at = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True) # auto_now: 글을 수정할 때마다 자동으로 입력
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE, null=True, blank=True) # 답변에 대한 댓글일 경우 이 부분은 입력 안됨
    answer = models.ForeignKey(BulletinAnswer, on_delete=models.CASCADE, null=True, blank=True)
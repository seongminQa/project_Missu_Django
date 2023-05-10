from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import NoticeAnswer, NoticeComments, Notice
from ..forms import NoticeAnswerForm, NoticeCommentsForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# 공지사항에 대한 댓글
@login_required(login_url="login")
def comment_notice_create(request, notice_id):
    '''
    CommentForm, get, post,
    성공시 detail로 이동
    '''
    
    notice = get_object_or_404(Notice, id=notice_id)
    
    if request.method=="POST":
        form = NoticeCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.notice = notice
            comment.save()
            # return redirect("detail", question_id=question_id)
            return redirect("{}#comment_{}".format(resolve_url("notice_detail", notice_id=notice_id),comment.id))
    else:
        form = NoticeCommentsForm()
            
    return render(request, "notice/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_notice_update(request, comment_id):
    '''
    댓글 내용 수정 - CommentForm, get, post 성공시 detail
    comment_form.html 사용
    '''
    
    comment = get_object_or_404(NoticeComments, id=comment_id) # comment의 정보를 가져온다.


    if request.method=="POST":
        form = NoticeCommentsForm(request.POST, instance=comment)   # 수정할 때, 반드시 instance가 필요하다!!
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("detail", question_id=comment.question.id)
            return redirect("{}#comment_{}".format(resolve_url("notice_detail", notice_id=comment.notice.id),comment.id))
    else:
        form = NoticeCommentsForm(instance=comment)
    
    return render(request,"notice/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_notice_delete(request, comment_id):
    '''
    댓글 내용 삭제 - CommentForm, get 성공시 detail
    '''
    
    comment = get_object_or_404(NoticeComments, id=comment_id)
    
    comment.delete()
    
    return redirect("notice_detail", notice_id=comment.notice.id) ## 



#########################################################################
@login_required(login_url="login")
def comment_answer_ncreate(request, answer_id):
    '''
    CommentForm, get, post,
    성공시 detail로 이동
    '''
    
    answer = get_object_or_404(NoticeAnswer, id=answer_id)
    
    if request.method=="POST":
        form = NoticeCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()

            return redirect("{}#comment_{}".format(resolve_url("notice_detail", notice_id=answer.notice.id),comment.id))
    else:
        form = NoticeCommentsForm()
            
    return render(request, "notice/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_answer_nupdate(request, comment_id):
    '''
    댓글 내용 수정 - CommentForm, get, post 성공시 detail
    comment_form.html 사용
    '''
    
    comment = get_object_or_404(NoticeComments, id=comment_id) # comment의 정보를 가져온다.


    if request.method=="POST":
        form = NoticeCommentsForm(request.POST, instance=comment)   # 수정할 때, 반드시 instance가 필요하다!!
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("detail", question_id=comment.answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("notice_detail", notice_id=comment.answer.notice.id),comment.id))
    else:
        form = NoticeCommentsForm(instance=comment)
    
    return render(request,"notice/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_answer_ndelete(request, comment_id):
    '''
    댓글 내용 삭제 - CommentForm, get 성공시 detail
    '''
    
    comment = get_object_or_404(NoticeComments, id=comment_id)
    
    comment.delete()
    
    return redirect("notice_detail", notice_id=comment.answer.notice.id)
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import BulletinAnswer, Comment, Bulletin
from ..forms import BulletinAnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url="login")
def comment_bulletin_create(request, bulletin_id):
    '''
    CommentForm, get, post,
    성공시 detail로 이동
    '''
    
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bulletin = bulletin
            comment.save()
            # return redirect("detail", question_id=question_id)
            return redirect("{}#comment_{}".format(resolve_url("bulletin_detail", bulletin_id=bulletin_id),comment.id))
    else:
        form = CommentForm()
            
    return render(request, "bulletin/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_bulletin_update(request, comment_id):
    '''
    댓글 내용 수정 - CommentForm, get, post 성공시 detail
    comment_form.html 사용
    '''
    
    comment = get_object_or_404(Comment, id=comment_id) # comment의 정보를 가져온다.


    if request.method=="POST":
        form = CommentForm(request.POST, instance=comment)   # 수정할 때, 반드시 instance가 필요하다!!
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("detail", question_id=comment.question.id)
            return redirect("{}#comment_{}".format(resolve_url("bulletin_detail", bulletin_id=comment.bulletin.id),comment.id))
    else:
        form = CommentForm(instance=comment)
    
    return render(request,"bulletin/comment_update.html", {"form":form})



@login_required(login_url="login")
def comment_bulletin_delete(request, comment_id):
    '''
    댓글 내용 삭제 - CommentForm, get 성공시 detail
    '''
    
    comment = get_object_or_404(Comment, id=comment_id)
    
    comment.delete()
    
    return redirect("bulletin_detail", bulletin_id=comment.bulletin.id)



#########################################################################
@login_required(login_url="login")
def comment_answer_create(request, answer_id):
    '''
    CommentForm, get, post,
    성공시 detail로 이동
    '''
    
    answer = get_object_or_404(BulletinAnswer, id=answer_id)
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            # return redirect("detail", question_id=answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("bulletin_detail", bulletin_id=answer.bulletin.id),comment.id))
    else:
        form = CommentForm()
            
    return render(request, "bulletin/comment_form.html", {"form":form})



@login_required(login_url="login")
def comment_answer_update(request, comment_id):
    '''
    댓글 내용 수정 - CommentForm, get, post 성공시 detail
    comment_form.html 사용
    '''
    
    comment = get_object_or_404(Comment, id=comment_id) # comment의 정보를 가져온다.


    if request.method=="POST":
        form = CommentForm(request.POST, instance=comment)   # 수정할 때, 반드시 instance가 필요하다!!
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("detail", question_id=comment.answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("bulletin_detail", bulletin_id=comment.answer.bulletin.id),comment.id))
    else:
        form = CommentForm(instance=comment)
    
    return render(request,"bulletin/comment_update.html", {"form":form})



@login_required(login_url="login")
def comment_answer_delete(request, comment_id):
    '''
    댓글 내용 삭제 - CommentForm, get 성공시 detail
    '''
    
    comment = get_object_or_404(Comment, id=comment_id)
    
    comment.delete()
    
    return redirect("bulletin_detail", bulletin_id=comment.answer.bulletin.id)
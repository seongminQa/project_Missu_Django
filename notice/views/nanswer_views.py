from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import NoticeAnswer, NoticeComments, Notice
from ..forms import NoticeAnswerForm, NoticeCommentsForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# 공지에 대한 질문댓글 등록
@login_required(login_url="login")
def notice_answer_create(request, notice_id):
    
    notice = get_object_or_404(Notice, pk=notice_id)

    if request.method=="POST":
        form = NoticeAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.notice = notice            
            answer.author = request.user
            answer.save()
            
            return redirect("{}#answer{}".format(resolve_url("notice_detail", notice_id=notice_id), answer.id)) ## 
        
    else:
        form = NoticeAnswerForm()
        
    return render(request, "notice/notice_detail.html", {"form":form,"notice":notice}) ## 



# 질문댓글 수정
@login_required(login_url="login")
def notice_answer_update(request, answer_id):
    
    answer = get_object_or_404(NoticeAnswer, id=answer_id)

    if request.user != answer.author:
        return redirect("notice_detail", notice_id=answer.notice_id)
    
    if request.method == "POST":
        form = NoticeAnswerForm(request.POST, instance=answer)
        
        if form.is_valid():
            answer = form.save(commit=False) # user정보 추가에 대한 코드
            answer.author = request.user
            answer.modified_at = timezone.now()
            answer.save()

            return redirect("{}#answer_{}".format(resolve_url("notice_detail", notice_id=answer.notice_id),answer.id))
        
    else:
        form = NoticeAnswerForm(instance=answer)
    
    return render(request,"notice/answer_form.html", {"form":form})



# 질문댓글 삭제
@login_required(login_url="login")
def notice_answer_delete(request, answer_id):
    
    answer = get_object_or_404(NoticeAnswer, id=answer_id)
    
    # 삭제하기
    if request.user != answer.author:
        return redirect("notice_detail", notice_id=answer_id)
    
    answer.delete()
    return redirect("notice_detail", notice_id=answer.notice_id)
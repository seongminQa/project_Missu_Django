from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Bulletin, BulletinAnswer
from ..forms import BulletinForm, BulletinAnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# 로그인이 안되어있으면 답변등록 막기
@login_required(login_url="login") # 로그인이 안되어있으면 로그인페이지로 이동시키기
def bulletin_answer_create(request, bulletin_id):
    '''
    답변 등록
    get 비어있는 폼
    post 바인딩 폼
    '''
    bulletin = get_object_or_404(Bulletin, pk=bulletin_id) 
    
    if request.method=="POST":
        form = BulletinAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.bulletin = bulletin
            answer.author = request.user
            answer.save()

            return redirect("{}#answer_{}".format(resolve_url("bulletin_detail", bulletin_id=bulletin_id),answer.id))
    else:
        form = BulletinAnswerForm()
            
    return render(request, "bulletin/bulletin_detail.html", {"form":form,"bulletin":bulletin})


@login_required(login_url="login")
def bulletin_answer_update(request, answer_id):
    '''
    답변 수정
    - ResponseForm 사용(response_form.html), 수정 성공시 detail로 이동
    '''
    
    # 답변 찾기
    answer = get_object_or_404(BulletinAnswer, id=answer_id)
    
    if request.user != answer.author:
        return redirect("bulletin_detail", bulletin_id=answer.bulletin)
    
    if request.method == "POST":
        form = BulletinAnswerForm(request.POST, request.FILES, instance=answer) # 수정할 대상을 데려감 instance=answer   # 수정할 때, 반드시 instance가 필요하다!!
        
        if form.is_valid():
            answer = form.save(commit=False) # user정보 추가에 대한 코드
            answer.author = request.user
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("detail", question_id=answer.question_id)
            return redirect("{}#answer_{}".format(resolve_url("bulletin_detail", bulletin_id=answer.bulletin_id),answer.id))
        
    else:
        form = BulletinAnswerForm(instance=answer)
    
    return render(request,"bulletin/answer_form.html", {"form":form})



@login_required(login_url="login")
def bulletin_answer_delete(request, answer_id):
    '''
    답변 삭제, 삭제 성공 시 detail로 이동
    '''
    
    answer = get_object_or_404(BulletinAnswer, id=answer_id)
    
    # 삭제하기
    if request.user != answer.author:
        return redirect("bulletin_detail", bulletin_id=answer)
    
    answer.delete()
    return redirect("bulletin_detail", bulletin_id=answer.bulletin_id)
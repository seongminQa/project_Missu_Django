from django.shortcuts import render, get_object_or_404, redirect
from ..models import Bulletin, BulletinAnswer
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def vote_bulletin(request, bulletin_id):
    '''
    질문 추천 등록
    성공 시 detail
    질문을 찾은 후, bulletin.voter.add(로그인 사용자)
    '''
    
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    
    # 자신의 글은 추천하지 못하고, 타인이 쓴 글만 추천 가능하게끔
    if bulletin.author != request.user:
        bulletin.voter.add(request.user)
    else:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    
    return redirect("bulletin_detail", bulletin_id=bulletin_id)
        
    
    
@login_required(login_url="login")
def vote_answer(request, answer_id):
    '''
    답변 추천 등록
    성공 시 detail
    답변을 찾은 후, answer.voter.add(로그인 사용자)
    '''
    
    answer = get_object_or_404(BulletinAnswer, id=answer_id)
    
    # 자신의 글은 추천하지 못하고, 타인이 쓴 글만 추천 가능하게끔
    if answer.author != request.user:
        answer.voter.add(request.user)
    else:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    
    return redirect("bulletin_detail", bulletin_id=answer.bulletin_id)
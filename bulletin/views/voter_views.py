from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Bulletin
from django.contrib import messages

# 비동기식 처리에 대한 응답
from django.http import JsonResponse

def bulletin_voter(request):
    '''
    비동기식 요청 - 좋아요 클릭 여부
    '''
    
    # 글번호 가져오기
    bulletin_id = request.POST['id']
    
    # 글번호에 해당하는 게시물 찾기
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    
    if bulletin.author != request.user:
        bulletin.voter.add(request.user)
    else:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
        
    # 로그인 사용자가 현재 게시물에 좋아요 누른 정보가 있는지 확인
    is_liked = bulletin.voter.filter(id=request.user.id).exists()
    
    if is_liked:
        bulletin.voter.remove(request.user)
        is_liked = False
    else:
        bulletin.voter.add(request.user)
        is_liked = True
        
    return JsonResponse({"voter":bulletin.voter.count(), "is_liked":is_liked})
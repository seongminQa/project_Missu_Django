from django.shortcuts import render, get_object_or_404, redirect
from ..models import Bulletin
from ..forms import BulletinForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# 로그인이 안되어있으면 답변등록 막기
@login_required(login_url="login") # 로그인이 안되어있으면 로그인페이지로 이동시키기
def bulletin_create(request):
    '''
    get 비어있는 폼
    post 바이딩 폼
    '''
    
    if request.method == "POST":
        form = BulletinForm(request.POST, request.FILES)
        if form.is_valid():
            bulletin = form.save(commit=False) # user정보 추가에 대한 코드
            bulletin.author = request.user
            bulletin.save()
            
            return redirect("bulletin_detail", bulletin_id=bulletin.id)
    else:
        form = BulletinForm()
    
    return render(request,"bulletin/bulletin_form.html", {"form":form})



# 질문 수정
@login_required(login_url="login")
def bulletin_update(request, bulletin_id):
    '''
    게시물 수정 - form 사용
    '''
    
    bulletin = get_object_or_404(Bulletin, id=bulletin_id) # 수정할 대상을 찾아서 가져가야함
    
    
    if request.method == "POST":
        form = BulletinForm(request.POST, request.FILES, instance=bulletin) # 수정할 대상을 데려감 intance=question
        if form.is_valid():
            bulletin = form.save(commit=False) # user정보 추가에 대한 코드
            bulletin.author = request.user
            bulletin.modified_at = timezone.now()
            bulletin.save()
            return redirect("bulletin_detail",bulletin_id=bulletin_id)
    else:
        form = BulletinForm(instance=bulletin)
    
    return render(request,"bulletin/bulletin_update.html", {"form":form})
        
        
        

# 질문내용 삭제
@login_required(login_url="login")
def bulletin_delete(request, bulletin_id):
    '''
    bulletin_id 값과 일치한 게시물 삭제 후 전체 리스트
    '''
    
    # 삭제할 질문 찾기
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    
    
    # 삭제하기
    if request.user != bulletin.author:
        return redirect("bulletin_detail", bulletin_id=bulletin_id)
    
    bulletin.delete()
    
    return redirect("bulletin_index")
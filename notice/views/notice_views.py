from django.shortcuts import render, get_object_or_404, redirect
from ..models import Notice
from ..forms import NoticeForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# 관리자만 공지글 생성가능
# 공지글 생성 ## 관리자만 가능하게끔
@login_required(login_url="login")
def notice_create(request):
    
    if request.method == "POST":
        form = NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            notice = form.save(commit=False) # user정보 추가에 대한 코드
            notice.author = request.user
            notice.save()
            return redirect("notice_detail", notice_id = notice.id)
    else:
        form = NoticeForm()
    
    return render(request,"notice/notice_form.html", {"form":form})



# 공지 수정
@login_required(login_url="login")
def notice_update(request, notice_id):
    
    notice = get_object_or_404(Notice, id=notice_id) # 수정할 대상을 찾아서 가져가야함
    
    if request.method == "POST":
        form = NoticeForm(request.POST,request.FILES, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False) # user정보 추가에 대한 코드
            notice.author = request.user
            notice.modified_at = timezone.now()
            notice.save()
            return redirect("notice_detail", notice_id=notice_id)
    else:
        form = NoticeForm(instance=notice)
    
    return render(request,"notice/notice_update.html", {"form":form})


# 공지 삭제
@login_required(login_url="login")
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    
    
    # 삭제하기
    if request.user != notice.author:
        return redirect("notice_detail", notice_id=notice_id)
    
    notice.delete()
    
    return redirect("notice_index")
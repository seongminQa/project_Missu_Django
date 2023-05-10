from django.shortcuts import render, redirect,get_object_or_404
from ..models import Notice, NoticeCount
from django.db.models import Q, Count
from tools.utils import get_client_ip
from django.core.paginator import Paginator



def notice_index(request):
    '''
    Notice 전체목록 최신날짜 작성순서로 보여주기위한 함수 정의
    '''
    
    # 현재 페이지 번호
    page = request.GET.get('page',1)
    
    # 검색어 받기
    keyword = request.GET.get('keyword','') # request.GET['keyword']
    
    lists = Notice.objects.order_by("-created_at") # 최신순으로 정렬하기
        
    
    # 전체 리스트에서 검색어가 들어간 리스트만 추출하기
    # Q --> OR 조건으로 데이터 조회할 때 사용
    # distinct() --> 중복 제거
    if keyword:
        lists = lists.filter(Q(title__icontains = keyword) |
                             Q(content__icontains = keyword) |
                             Q(category__icontains = keyword)).distinct()
    
    
    paginator = Paginator(lists, 10) # 10개 씩 나눠서 넣음
    
    page_obj = paginator.get_page(page)
    
    return render(request, "notice/notice_list.html",{"lists":page_obj, "page":page, "keyword":keyword})


def notice_detail(request, notice_id):
    '''
    notice_id 에 맞는 공지 상세 추출
    조회수 ip 추가
    '''
    # 현재 페이지 번호
    page = request.GET.get('page',1)
    
    # 검색어 받기
    keyword = request.GET.get('keyword','') 
    # request.GET['keyword']
    
    notice = get_object_or_404(Notice, id=notice_id)
    
    
    # ip 가져오기
    ip = get_client_ip(request)
    
    # 현재 질문에 대한 조회수 찾기
    cnt = NoticeCount.objects.filter(ip=ip, notice=notice).count()
    
    if cnt == 0:
        qc = NoticeCount(ip=ip, notice=notice)
        qc.save()
        
        if notice.view_cnt:
            notice.view_cnt += 1
        else:
            notice.view_cnt = 1
        notice.save()
    
    
    
    return render(request,"notice/notice_detail.html",{"notice":notice, "page":page, "keyword":keyword})
from django.shortcuts import render, get_object_or_404
from ..models import Bulletin, BulletinCount, Comment, BulletinAnswer
from django.core.paginator import Paginator
from django.db.models import Q, Count
from tools.utils import get_client_ip
from django.contrib.auth.decorators import login_required


def bulletin_index(request):
    '''
    Community 전체목록 최신날짜 작성순서로 보여주기 위한 함수 정의
    '''
    
    # 현재 페이지 번호
    page = request.GET.get('page',1)
    
    # 검색어 받기
    keyword = request.GET.get('keyword','') # request.GET['keyword']
    
    # 정렬기준 받기
    so = request.GET.get('so','recent') # sort 기준 : recent(기본), recommend, popular(인기순-> 댓글이 많은 경우)
    
    
    
    if so == "recommend": # 추천순
        lists = Bulletin.objects.annotate(num_voter = Count('voter')).order_by("-num_voter","-created_at")
    elif so == "popular": # 인기순
        lists = Bulletin.objects.annotate(num_answer = Count('bulletinanswer')).order_by("-num_answer", "-created_at")
    else: # 최신순
        lists = Bulletin.objects.order_by("-created_at") # 최신순으로 정렬하기
        
    
    # 전체 리스트에서 검색어가 들어간 리스트만 추출하기
    # Q --> OR 조건으로 데이터 조회할 때 사용
    # distinct() --> 중복 제거
    if keyword:
        # lists = lists.filter(title__icontains = keyword)
        lists = lists.filter(Q(title__icontains = keyword) |
                             Q(content__icontains = keyword) |
                             Q(author__nickname__icontains = keyword) |
                             Q(bulletinanswer__author__nickname__icontains = keyword)).distinct()
    
    
    paginator = Paginator(lists, 10) # 10개 씩 나눠서 넣음
    
    page_obj = paginator.get_page(page)
    
    return render(request, "bulletin/bulletin_list.html",{"lists":page_obj, "page":page, "keyword":keyword, "so":so})


def bulletin_detail(request, bulletin_id):
    '''
    bulletin_id 에 맞는 질문 상세 추출
    조회수 증가 : ip 얻어내기
    '''
    # bulletin 페이지 나누기 값
    
    # 원본 게시물
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    
    # 페이지 번호
    page = request.GET.get('page',1)
    # 검색어 받기
    keyword = request.GET.get('keyword','') # request.GET['keyword']    
    # 정렬기준 받기
    so = request.GET.get('so','recent') # sort 기준 : recent(기본), recommend, popular(인기순-> 댓글이 많은 경우)
    
    # 상세보기에서 필요한 페이지 나누기 정보(comment)
    comment_page = request.GET.get('comment_page',1)
    # 원본 게시물의 전체 댓글 리스트 추출
    commentlists = Comment.objects.filter(bulletin = bulletin_id).order_by("created_at")
    paginator = Paginator(commentlists, 5)
    page_obj = paginator.get_page(comment_page)
    print("comment",page_obj,"comment_page",comment_page)
    
    # ip 가져오기
    ip = get_client_ip(request)
    
    # 현재 질문에 대한 조회수 찾기
    cnt = BulletinCount.objects.filter(ip=ip, bulletin=bulletin).count()
    
    if cnt == 0:
        qc = BulletinCount(ip=ip, bulletin=bulletin)
        qc.save()
        
        if bulletin.view_cnt:
            bulletin.view_cnt += 1
        else:
            bulletin.view_cnt = 1
        bulletin.save()
    
    context = {
        # 상세보기
        "bulletin":bulletin, 
        "page":page, 
        "keyword":keyword, 
        "so":so, 
        
        # comment
        "commentlists":page_obj,      # comment 정보
        "comment_page":comment_page,  # comment 에서 현재 페이지 보기
        
    }
    
    return render(request,"bulletin/bulletin_detail.html",context)

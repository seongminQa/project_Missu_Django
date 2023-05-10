from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from music import views
# from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # 홈페이지
    path('',views.music_home,name="home"),
    path('melon/<int:id>/',views.melon_detail, name="melon_detail"),
    path('bugs/<int:id>/',views.bugs_detail, name="bugs_detail"),
    path('genie/<int:id>/',views.genie_detail, name="genie_detail"),
    # 유저
    path("users/",include('users.urls')),
    # django-allauth 에서 제공하는 url 가져오기
    path('accounts/',include('allauth.urls')),

    # 공지게시판
    path('notice/', include('notice.urls')),
    
    # 자유게시판
    path("bulletin/", include("bulletin.urls")),
    
    # # 커뮤니티
    # path("community/", include("community.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
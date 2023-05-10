from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # http://127.0.0.1:8000/users/
    
    # 로그인/로그아웃 
    # users/login/  name= login
    path("register/", views.register, name='register'),
    path("login/",auth_views.LoginView.as_view(template_name = "users/login.html",success_url=reverse_lazy('home')),name="login"),
    # (template_name = "home.html",success_url=reverse_lazy('home.html')),name="login"),

    # users/logout/ name = logout
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("profile/",views.ProfileEdit.as_view(),name="profile_edit"),
    path("profile/delete/",views.UserProfileImageDelete.as_view(),name="user_profile_delete"),
    path("profile/update/",views.UserProfileImageUpdate.as_view(),name="user_profile_update"),

    # PasswordChangeView : 비밀번호 변경, 바뀐 비밀번호로 업데이트 하고, 세션도 계속 유지
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="users/password_change.html",success_url = reverse_lazy("home")),name="password_change"),

    # 클래스 뷰
    path("password_reset/",views.UserPasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/",views.UserPasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",views.UserPasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset/done/",views.UserPasswordResetCompleteView.as_view(),name="password_reset_complete"),



    # # users/
    # path('recovery/id/', views.RecoveryIdView.as_view(), name='recovery_id'),
    # path('recovery/id/find/', views.ajax_find_id_view, name='ajax_id'),
]

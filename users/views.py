from pipes import Template
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.generic.base import TemplateView
from .forms import RegisterForm
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
# from community.models import Community
from users.models import Profile,User
from bulletin.models import Bulletin
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum

class BaseView(View):
  """
  클라이언트로부터 요청을 받아 JsonResponse 로 응답하는 뷰
  """

  @staticmethod
  def response(result={},status=200):
    return JsonResponse(result,status=status)
    # 요즘 웹개발에서 많이 쓰이는 방식 = JsonResponse (데이터만 넘기는 방식, html XX)


def register(request):

  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      # 회원가입 완료 후 로그인 처리도 해주고 싶다면?
      email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password1")

      # db 확인(사용자의 입력값과 데이터베이스 내용과 확인)
      user = authenticate(request,email=email,password=password)

      # 세션에 정보 저장
      if user is not None:
        login(request, user)
        return redirect("home")
      # return redirect('login')
  else:
    form = RegisterForm()

  return render(request,"users/register.html",{"form":form})


@method_decorator(login_required,name='dispatch')
class ProfileEdit(TemplateView):
  template_name = "users/profile.html"

  def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)

      # 로그인 사용자의 게시물 개수
      context["contents"] = Bulletin.objects.filter(author = self.request.user)
      # 로그인 사용자 게시물이 추천받은 횟수
      context["voters"] = Bulletin.objects.filter(author = self.request.user).aggregate(voters=Sum('voter'))
      # 사용자가 작성한 게시물의 조회수
      context["view_cnts"] =Bulletin.objects.filter(author = self.request.user).aggregate(view_cnts=Sum('view_cnt'))

      return context

@method_decorator(login_required,name='dispatch')
class UserProfileImageUpdate(BaseView):
  """
  사용자 프로필 사진을 사용자가 선택한 이미지로 변경
  """
  def post(self,request):

    # 사용자가 보낸 이미지 가져오기
    image = request.FILES['file']
    
    profile = get_object_or_404(Profile,user = request.user)
    profile.image = image
    profile.save()

    return self.response({"error":False,"message":"Successfully"},status=200)


class UserProfileImageDelete(BaseView):
  """
  사용자 프로필 사진을 default.png 변경
  """
  def get(self,request):
    """
    현재 로그인 사용자의 이미지 profile/default.png로 변경
    """
    profile = get_object_or_404(Profile,user = request.user)
    profile.image = "profile/default.png"
    profile.save()

    return self.response({"error":False,"message":"Successfully"},status=200)


# 비밀번호 reset 담당 클래스 뷰
class UserPasswordResetView(PasswordResetView):
  # 이메일을 입력할 수 있는 화면
  template_name = "users/password_reset_form.html"
  # 이메일이 올바른 경우 그 다음 작업을 진행할 경로 지정
  success_url = reverse_lazy("password_reset_done")
  # 이메일로 전송될 페이지 지정
  email_template_name = "users/password_reset_email.txt"

  def form_valid(self, form):
    # 사용자가 입력한 이메일이 실제 존재하는지 확인 후 없으면 에러 메세지 전송
    # 존재한다면 유효성 검증 

    if User.objects.filter(email=self.request.POST.get('email')).exists():
      return super().form_valid(form)
    else:
      messages.info(self.request,"이메일을 확인해 주세요")
      return redirect("password_reset")


class UserPasswordResetDoneView(PasswordResetDoneView):
  template_name = "users/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = "users/password_reset_confirm.html"

class UserPasswordResetCompleteView(PasswordResetCompleteView):
  template_name = "users/password_reset_complete.html"

# def logout_message_required(function):
#     def wrap(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             messages.info(request, "접속중인 사용자입니다.")
#             return redirect('home')
#         return function(request, *args, **kwargs)
#     return wrap

# @method_decorator(logout_message_required, name='dispatch')
# class RecoveryIdView(View):
#     template_name = 'users/recovery_id.html'
#     form = RecoveryIdForm

#     def get(self, request):
#         if request.method=='GET':
#             form = self.recovery_id(None)
#         return render(request, self.template_name, {'form':form})

# import json
# def ajax_find_id_view(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     result_id = User.objects.get(name=name, email=email)       
#     return HttpResponse(json.dumps({"result_id": result_id.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")

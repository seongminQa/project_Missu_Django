from django import forms
from .models import Notice, NoticeAnswer, NoticeComments
        
        
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title','content','category','image']
        
        
class NoticeAnswerForm(forms.ModelForm):
    class Meta:
        # 모델 연결
        model = NoticeAnswer
        # fields
        fields = ['content']
        
        
class NoticeCommentsForm(forms.ModelForm):
    class Meta:
        model = NoticeComments
        fields = ['content']
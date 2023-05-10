from django import forms
from .models import BulletinAnswer, Bulletin, Comment
        
        
class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ['title','content','image']


class BulletinAnswerForm(forms.ModelForm):
    class Meta:
        # 모델 연결
        model = BulletinAnswer
        # fields
        fields = ['content','image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
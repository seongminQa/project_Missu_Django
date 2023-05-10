from django.db import models

class MelonWeekTop(models.Model):
    """
    모델을 크롤링할 데이터에 맞출 준비
    """
    rank = models.IntegerField(verbose_name="순위")
    image = models.ImageField(blank=True, null=True, verbose_name="앨범커버")
    title = models.CharField(max_length=200,verbose_name="곡명")
    musician = models.CharField(max_length=150,verbose_name="가수")
    album = models.CharField(max_length=300,verbose_name="앨범명")
    released_at = models.CharField(max_length=200,verbose_name="발매일")
    genre = models.CharField(max_length=200,verbose_name="장르/스타일")
    released_cop = models.CharField(max_length=150,verbose_name="발매사")
    planned_cop = models.CharField(max_length=150,verbose_name="기획사")

    def __str__(self):
        return self.title

class GeniWeekTop(models.Model):
    """
    모델을 크롤링할 데이터에 맞출 준비
    """
    rank = models.IntegerField(verbose_name="순위")
    image = models.ImageField(blank=True,null=True,verbose_name="앨범커버")
    title = models.CharField(max_length=200,verbose_name="곡명")
    musician = models.CharField(max_length=150,verbose_name="가수")
    album = models.CharField(max_length=300,verbose_name="앨범명")
    released_at = models.CharField(max_length=200,verbose_name="발매일")
    genre = models.CharField(max_length=200,verbose_name="장르/스타일")
    released_cop = models.CharField(max_length=150,verbose_name="발매사")
    planned_cop = models.CharField(max_length=150,verbose_name="기획사")
    
    def __str__(self):
        return self.title

class BugsWeekTop(models.Model):
    """
    모델을 크롤링할 데이터에 맞출 준비
    """
    rank = models.IntegerField(verbose_name="순위")
    image = models.ImageField(blank=True,null=True,verbose_name="앨범커버")
    musician = models.CharField(max_length=200,verbose_name="가수")
    title = models.CharField(max_length=200,verbose_name="곡명")
    album = models.CharField(max_length=300,verbose_name="앨범명")
    released_at = models.CharField(max_length=200,verbose_name="발매일")
    genre = models.CharField(max_length=200,verbose_name="장르/스타일")
    released_cop = models.CharField(max_length=150,verbose_name="발매사")
    planned_cop = models.CharField(max_length=150,verbose_name="기획사")
    
    def __str__(self):
        return self.title
    

from django.shortcuts import render,redirect,get_object_or_404
from music.models import MelonWeekTop,BugsWeekTop,GeniWeekTop

# Create your views here.
def music_home(request):
  """

  """
  melon = MelonWeekTop.objects.filter(rank__lte = 10)
  bugs = BugsWeekTop.objects.filter(rank__lte = 10)
  genie = GeniWeekTop.objects.filter(rank__lte = 10)
  
  return render(request, "home.html",{"melon":melon,"bugs":bugs,"genie":genie})

def melon_detail(request,id):
    melon = get_object_or_404(MelonWeekTop,id=id)

    return render(request,"music/melon_detail.html",{"melon":melon})

def bugs_detail(request,id):
    bugs = get_object_or_404(BugsWeekTop,id=id)

    return render(request,"music/bugs_detail.html",{"bugs":bugs})
def genie_detail(request,id):
    genie = get_object_or_404(GeniWeekTop,id=id)

    return render(request,"music/genie_detail.html",{"genie":genie})

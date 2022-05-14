from django.shortcuts import render
from .models import Page

def index(request):
  object_list = Page.objects.all()
  return render(request,'Blog/home.html',{'object_list':object_list})

def read(request, page_id):
  object_detail = Page.objects_or_404(id = page_id)
  return render(request, 'Blog/page_detail.html', {'object_detail': object_detail})

  def create(request):
    if request.method=='POST':
      form=PageForm(request.POST)
      new_Page=form.save()
      return redirect('page-read', page_id=new_page.id)
    else:
      form=PageForm()
      return render(request, 'Blog/page_create.html',{'form':form})
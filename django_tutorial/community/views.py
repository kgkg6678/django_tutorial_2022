from django.shortcuts import render
from community.forms import Form
from .models import Article 
# Create your views here.
def write(request):
    # form 데이터를 입력하고 확인, 데이터 저장 요청
    if request.method == 'POST':      #POST 는 대문자로 
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    #빈 form 페이지 요청 
    else :
        form= Form()
    
    return render(request, 'write.html', {'form': form})

# 글작성 목록 보여주기 
def articleList(request) :
    article_list =  Article.objects.all()    
    return render(request, 'list.html', {'article_list':article_list})
    
    
def viewDetail(request, num=1):
    article_detail = Article.objects.get(id=num)  id 대신 pk
    # article_detail = get_objects_or_404(Article, pk=num)
    return render(request, 'view_detail.html', {'article_detail' : article_detail} )
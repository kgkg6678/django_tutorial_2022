from django.shortcuts import render
from community.forms import Form

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

    
    
    
    

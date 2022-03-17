from django.shortcuts import redirect, render
from .models import CountryData
from .forms import CountryDataForm
# Create your views here.

def dashboard(request):
    #각 나라와 인구 숫자를 가져오기
    data =CountryData.objects.all()
    
    #add 버튼 클릭, 값 입력 요청 처리 
    if request.method == 'POST':
    # db 입력
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')

    # form 출력
    else :    
        form = CountryDataForm()
    
    # 그래프 반영  
    
    #폼 객체 생성 
    
    
    #랜더링 전달 데이터와 폼 객체 저장 
    return render(request, 'dashboard/dashboard.html', {'dataset': data, 'form' : form})









    #데이터  
    #db데이터 가져오기
    #데이터 필터링 
    #form 처리 
    #return render(request, '렌더링할 템플릿파일', {'html_템플릿에 전달할 데이터 키 ': 데이터 })
    
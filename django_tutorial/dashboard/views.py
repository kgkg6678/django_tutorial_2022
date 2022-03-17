from django.shortcuts import render
from .models import CountryData
# Create your views here.

def dashboard(request):
    #각 나라와 인구 숫자를 가져오기
    data =CountryData.objects.all()
    

    return render(request, 'dashboard/dashboard.html', {'dataset': data})









    #데이터  
    #db데이터 가져오기
    #데이터 필터링 
    #form 처리 
    #return render(request, '렌더링할 템플릿파일', {'html_템플릿에 전달할 데이터 키 ': 데이터 })
    
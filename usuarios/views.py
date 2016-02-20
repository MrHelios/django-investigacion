from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    if request.method == 'POST':
        respuesta = request.POST.get('algo','')
        return render(request,'HTML/resp-index.html',{'respuesta':respuesta})
    else:
        return render(request,'HTML/index.html')

    return render(request,'HTML/index.html')    

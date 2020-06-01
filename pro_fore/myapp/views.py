from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':199}
    return render(request,'myapp/index.html',context_dict)

def other(request):
    return render(request,'myapp/other.html')

def relative(request):
    return render(request,'myapp/relative_url_temp.html')

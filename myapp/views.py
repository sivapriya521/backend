from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return render(requests,'index.html')
# context should be dictionary,to change content depending on log in
def counter(request):
    #variable text name of textarea
    #thhis txt stores datas typed in txtbox
    text=request.GET['text']
    no_word=len(text.split())
    return render(request,'counter.html',{'amount':no_word})
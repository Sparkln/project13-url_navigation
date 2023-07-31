from django.shortcuts import render

# Create your views here.
def url_navigation(request):
    d = {'name':'surya', 'age':23, 'hobbies':['palying games','suffering interner']}
    return render(request, 'url_navigation.html', d)

def url_2(request):
    d = {'a':20, 'b':30, 'c':50}
    return render(request, 'url_2.html', d)
from django.shortcuts import render

def t3(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/t3.html', context)

def magazin(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/magazin.html', context)

def korzina(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/korzina.html', context)

# Create your views here.

from django.shortcuts import render

def t3(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/t3.html', context)

def magazin(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'fourth_task/magazin.html', context)

def korzina(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/korzina.html', context)
# Create your views here.

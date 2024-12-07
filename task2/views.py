from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
def func_templates(request):
    return render(request, 'second_task/func.html')

class ClassTemplates(TemplateView):
    template_name = 'second_task/class.html'
# Create your views here.

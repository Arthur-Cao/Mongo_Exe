from django.shortcuts import render
from .models import TestModel

# Create your views here.

def display(request):
    entry = TestModel(test_key='one')
    entry.test_value = 'Wang'
    entry.save()
    example = TestModel.objects.all()
    # for entry in TestModel.objects:
    #     print(entry.test_key)
    context = {'values': example}
    return render(request, 'list.html', context)

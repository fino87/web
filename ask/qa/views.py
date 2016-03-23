from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def test(request, *args, **kwargs):
    template = loader.get_template('qa/index.html')
    context = RequestContext(request, {
        'test_key': 'test_value',
    })
    return HttpResponse(template.render(context))

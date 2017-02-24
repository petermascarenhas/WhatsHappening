from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .integrator import SearchApi
# Create your views here.

def index(request):
    searchApi = SearchApi()
    output_list = searchApi.make_request()
    result_dict = {}
    results = []
    for result in output_list:
        if result not in result_dict:
            result_dict[result] =1
            results.append(result)
    context = {'results':results}
    template = loader.get_template('Results/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request,'Results/index.html',context)
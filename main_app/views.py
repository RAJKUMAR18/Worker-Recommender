from django.shortcuts import render

from django.http import HttpResponseRedirect

import random

from .utils import vectorizer, BuildAndTrain
from .forms import Query
# Create your views here.
def index(request):
    return render(request, 'index.html')

def help(request):
    return render(request, 'help.html')

def query(request):
    if request.method == 'POST':
        form = Query(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/query/')
    else:
        form = Query()

    return render(request, 'query.html',{'form':form})

def result(request):
    if request.method == 'POST':
        print('request method is post')
        query_data = Query(request.POST)
        if query_data.is_valid():
            print('form data validated')
            name = query_data.cleaned_data['name']
            mob_number = query_data.cleaned_data['mob_number']
            location = query_data.cleaned_data['location']
            service = query_data.cleaned_data['service']
            certification = query_data.cleaned_data['certification']
            age_prefernce = query_data.cleaned_data['age_prefernce']
            gender = query_data.cleaned_data['gender']
            types = query_data.cleaned_data['types']
            availability = query_data.cleaned_data['availability']
            wage_preference = query_data.cleaned_data['wage_preference']
            exprience = query_data.cleaned_data['exprience']
            clients_attended = random.randint(0,2)
            doorstep_service = query_data.cleaned_data['doorstep_service']
            reference = query_data.cleaned_data['reference']
            liscenced = random.randint(0, 1)
            shopping_liscence = random.randint(0, 1)

            context = {
            'name':name, 'mob_number':mob_number,
            'location':location, 'service':service,'certification':certification,
            'age_prefernce':age_prefernce,'gender':gender,'types':types,
            'availability':availability,'wage_preference':wage_preference,'exprience':exprience,
            'clients_attended':clients_attended,'doorstep_service':doorstep_service,
            'reference':reference,'liscenced':liscenced,'shopping_liscence':shopping_liscence
            }
            print('context generated')
            print('building model')
            vectorized_user_query = vectorizer(list(context.values()))
            print('user query vectorized')
            bnt = BuildAndTrain()
            kneighborsOfUserQuery, finalCluster = bnt.modelling(service=service, userquery=vectorized_user_query)
            print('done')
            context['clusterDF'] = list()
            for i in range(len(kneighborsOfUserQuery[1])):
                context['clusterDF'].append(finalCluster.iloc[kneighborsOfUserQuery[1][i]])
            return render(request, 'result.html', context=context)
        else:
            return render(request, 'result.html', context={'formerror':query_data.errors})

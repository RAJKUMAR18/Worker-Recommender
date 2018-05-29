from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import itertools
import pandas as pd
from .utils import vectorizer, BuildAndTrain
from .forms import Query
from django.views.generic import DetailView
# from .beauty import prettify

global_context = dict()
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

    return render(request, 'query.html', {'form': form})


def result(request):
    if request.method == 'POST':
        print('request method is post')
        query_data = Query(request.POST)
        if query_data.is_valid():
            bnt = BuildAndTrain()
            print('form data validated')
            name = query_data.cleaned_data['your_name']
            mob_number = query_data.cleaned_data['mob_number']
            location = query_data.cleaned_data['location']
            service = query_data.cleaned_data['service']
            certification = query_data.cleaned_data['certification']
            age_prefernce = query_data.cleaned_data['age_prefernce']
            gender = query_data.cleaned_data['gender']
            types = query_data.cleaned_data['types']
            availability = query_data.cleaned_data['availability']
            wage_preference = query_data.cleaned_data['wage_preference']
            experience = query_data.cleaned_data['experience']
            clients_attended = random.randint(0, 5)
            doorstep_service = query_data.cleaned_data['doorstep_service']
            reference = query_data.cleaned_data['reference']
            liscenced = random.randint(0, 1)
            shopping_liscence = random.randint(0, 1)

            print('context generated')
            
            context = {
                'uname': name,
                'mob_number': mob_number,
                'location': location, # 2
                'service': service, # 3
                'certification': certification, # 4
                'age_prefernce': age_prefernce, # 5
                'gender': gender, # 6
                'types': types, # 7        
                'availability': availability, # 8
                'wage_preference': wage_preference, # 9
                'experience': experience, # 10
                'clients_attended': clients_attended, # 11
                'doorstep_service': doorstep_service, # 12
                'reference': reference,# 13
                'liscenced': liscenced, # 14 
                'shopping_liscence': shopping_liscence,# 15
            }

            vectorized_user_query = vectorizer(list(context.values()))
            print('user query vectorized')
            # print(vectorized_user_query)
            finalCluster = bnt.modelling(service=service, userquery=vectorized_user_query)
            print('done')

            context = {
                'uname': name,
                'mob_number': mob_number,
                'location': ['Ambegaon', 'Aundh', 'Balewadi', 'Baner', 'Bavdhan', 'Bibewadi',
            'Camp', 'Chinchwad', 'Dattawadi', 'Deccan', 'Dhankawadi',
            'Dhayari', 'Dhole Patil Road', 'Erandwane',
            'Fatimanagar', 'Fursungi', 'Ganeshkhind', 'Ghorpadi',
            'Gultekdi', 'Hadapsar', 'Hinjewadi',
            'Katraj', 'Khadakwasla', 'Khadki', 'Kharadi', 'Kondhwa',
            'Koregaon Park', 'Kothrud', 'Mundhwa', 'Nigdi', 'Parvati',
            'Pashan', 'Paud Road', 'Pimplesaudagar', 'Sahakarnagar',
            'Salisbury Park', 'Saswad', 'Shivajinagar', 'Singhgad Road',
            'Swargate', 'Vishrantwadi', 'Vitthalwadi', 'Wagholi', 'Wanowrie'][int(location)], # 2
                'service': ['Accountant', 'Brick mason', 'Carpenter', 'Cashier',
            'Childcare Worker', 'Cook', 'Delivery Boy', 'Driver',
            'Electrician', 'Hairdresser', 'Janitor', 'Maid', 'Mechanic',
            'Mehndi Artist', 'Painter', 'Plumber', 'Receptionist',
            'Salesperson', 'Security Guard', 'Tailor', 'Waiter',
            'Waitress', 'Worker'][int(service)], # 3
                'certification': certification, # 4
                'age_prefernce': [(0, '18-20'), (1, '21-25'), (2, '26-30'), (3, '30-35')][int(age_prefernce)][1], # 5
                'gender': ['Female', 'Male'][int(gender)], # 6
                'types': ['Full Time', 'Part Time'][int(types)], # 7        
                'availability': [(0, 'Afternoon'), (1, 'Evening'), (2, 'Morning'),
             (3, 'Whole Day')][int(availability)][1], # 8
                'wage_preference': ['1000-5000', '5001-8000', '8001-10000'][int(wage_preference)], # 9
                'experience': ['0-2', '3-6', '6-10'][int(experience)], # 10
                'clients_attended': ['0 - 10', '11 - 20', '21 - 30', '31 - 40', '41 + '][int(clients_attended)], # 11
                'doorstep_service': [(0, 'No'), (1, 'Yes')][int(doorstep_service)][1], # 12
                'reference': [False, True][int(reference)],# 13
                'liscenced': ['False', 'True'][int(liscenced)], # 14 
                'shopping_liscence': ['False', 'True'][int(shopping_liscence)],
            }
            context['clusterDF'] = None
            context['clusterDF'] = finalCluster
            print(type(context['clusterDF']))
            # context['clusterDF'] = finalCluster.to_html(classes=['w3-table-all',], border=0, index=True)
            context['phoneNo'] = finalCluster['phoneNo'].values.tolist()
            # print(finalCluster.columns)
            context['name'] = finalCluster['name'].values.tolist()
            context['wlocation'] = finalCluster['location'].values.tolist()
            context['woccupation'] = finalCluster['occupation'].values.tolist()
            genders = finalCluster['gender'].values.tolist()
            context['zipped'] = zip(context['name'], context['phoneNo'], context['wlocation'], context['woccupation'], genders, context['clusterDF'].index.tolist())
            # print(finalCluster)
            for k,v in context.items():
                global_context[k] = v
            return render(request, 'result.html', {str(k):v for k,v in context.items()})
            # return render(request, 'result.html', {'contacts': contacts})
        else:
            return render(request, 'result.html'
                          , context={'formerror': query_data.errors})


def detail(request, wid):
    # print(type(request))
    # print(global_context)
    # print(type(global_context['clusterDF']))
    workerInstance = global_context['clusterDF'].loc[int(wid)]
    workerInstance = workerInstance.to_dict()
    # print(workerInstance)

    # print(workerInstance)
    # print(workerInstance.values.tolist())
    # print(type(workerInstance))
    return render(request, 'worker-detail.html', {str(k):v for k, v in workerInstance.items()})
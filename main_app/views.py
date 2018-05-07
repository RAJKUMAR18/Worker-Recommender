from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
import pandas as pd
from .utils import vectorizer, BuildAndTrain
from .forms import Query
# from .beauty import prettify

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
            classes = bnt.unpickleLoader('clsofclos')
            # print(classes)
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
            clients_attended = random.randint(0, 2)
            doorstep_service = query_data.cleaned_data['doorstep_service']
            reference = query_data.cleaned_data['reference']
            liscenced = random.randint(0, 1)
            shopping_liscence = random.randint(0, 1)

            print('context generated')
            
            context = {
                'name': name, 'mob_number': mob_number,
                'location': location, 'service': service,
                'certification': certification, 'types': types,
                'age_prefernce': age_prefernce, 'gender': gender,
                'availability': availability,
                'wage_preference': wage_preference,
                'experience': experience, 'clients_attended': clients_attended,
                'doorstep_service': doorstep_service, 'reference': reference,
                'liscenced': liscenced, 'shopping_liscence': shopping_liscence,
            }

            vectorized_user_query = vectorizer(list(context.values()))
            print('user query vectorized')
            
            kneighborsOfUserQuery, finalCluster = bnt.modelling(
                service=service
                , userquery=vectorized_user_query)

            # pretty_result = prettify(classes, kneighborsOfUserQuery[1][0], finalCluster)

            print('done')
            
            # location = str(classes['location'][0][int(location)])
            # shopping_liscence = str(classes['shoppingliscence'][0][int(shopping_liscence)])
            # liscenced = str(classes['liscenced'][0][int(liscenced)])
            # reference = str(classes['references'][0][int(reference)])
            # doorstep_service = str(classes['doorstepService '][0][int(doorstep_service)])
            # clients_attended = str(classes['clientsAttended'][0][int(clients_attended)])
            # service = str(classes['occupation'][0][int(service)])
            # certification = str(classes['certification'][0][int(certification)])
            # types = str(classes['type'][0][int(types)])
            # age_prefernce = str(classes['age'][0][int(age_prefernce)])
            # wage_preference = str(classes['minimumWage'][0][int(wage_preference)])
            # availability = str(classes['availability'][0][int(availability)])
            # gender = str(classes['gender'][0][int(gender)])
            # experience = str(classes['experience'][0][int(experience)])

            # context = {
            #     'name': name, 'mob_number': mob_number,
            #     'location': location, 'service': service,
            #     'certification': certification, 'types': types,
            #     'age_prefernce': age_prefernce, 'gender': gender,
            #     'availability': availability,
            #     'wage_preference': wage_preference,
            #     'experience': experience, 'clients_attended': clients_attended,
            #     'doorstep_service': doorstep_service, 'reference': reference,
            #     'liscenced': liscenced, 'shopping_liscence': shopping_liscence,
            # }
            temp_df = pd.read_csv(str(service) + '.csv')
            context['clusterDF'] = None
            # context['clusterDF'] = finalCluster.iloc[kneighborsOfUserQuery[1][0]].to_html()
            
            combined = temp_df.append(finalCluster.iloc[kneighborsOfUserQuery[1][0]])
            combined[~combined.index.duplicated(keep=False)]
            final = finalCluster.iloc[kneighborsOfUserQuery[1][0]].append(combined)
            
            context['clusterDF'] = final.to_html()

            return render(request, 'result.html', context=context)
        else:
            return render(request, 'result.html'
                          , context={'formerror': query_data.errors})

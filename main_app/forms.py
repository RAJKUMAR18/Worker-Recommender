from django import forms

class Query(forms.Form):

    LOCS = ['Ambegaon', 'Aundh', 'Balewadi', 'Baner', 'Bavdhan', 'Bibewadi',
       'Camp', 'Chinchwad', 'Dattawadi', 'Deccan', 'Dhankawadi', 'Dhayari',
       'Dhole Patil Road', 'Erandwane', 'Fatimanagar', 'Fursungi',
       'Ganeshkhind', 'Ghorpadi', 'Gultekdi', 'Hadapsar', 'Hinjewadi',
       'Katraj', 'Khadakwasla', 'Khadki', 'Kharadi', 'Kondhwa',
       'Koregaon Park', 'Kothrud', 'Mundhwa', 'Nigdi', 'Parvati', 'Pashan',
       'Paud Road', 'Pimplesaudagar', 'Sahakarnagar', 'Salisbury Park',
       'Saswad', 'Shivajinagar', 'Singhgad Road', 'Swargate',
       'Vishrantwadi', 'Vitthalwadi', 'Wagholi', 'Wanowrie']
    LOCATIONS = [(x, y) for x, y in zip(range(len(LOCS)), LOCS)]
    OCCS = ['Accountant', 'Brick mason', 'Carpenter', 'Cashier',
       'Childcare Worker', 'Cook', 'Delivery Boy', 'Driver', 'Electrician',
       'Hairdresser', 'Janitor', 'Maid', 'Mechanic', 'Mehndi Artist',
       'Painter', 'Plumber', 'Receptionist', 'Salesperson',
       'Security Guard', 'Tailor', 'Waiter', 'Waitress', 'Worker']
    OCCUPATIONS = [(x, y) for x, y in zip(range(len(OCCS)), OCCS)]
    DOORSTEP = [(0,'No'),(1,'Yes')]
    AGES = [(0,'18-20'),(1,'21-25'),(2,'26-30'),(3,'30-35')]
    AVAIL = [(0,'Afternoon'),(1,'Evening'),(2,'Morning'),(3,'Whole Day')]
    WAGERANGE = ['1000-5000','5001-8000','8001-10000']
    MINWAGE = [(x,y) for x, y in zip(range(len(WAGERANGE)), WAGERANGE)]
    EXP = ['0-2','3-6','6-10']
    EXPE = [(x,y) for x,y in zip(range(len(EXP)),EXP)]
    CERT = [False,  True]
    CERTIFICATIONS = [(x,y) for x,y in zip(range(len(CERT)), CERT)]
    GEN = ['Female', 'Male']
    GENDERS = [(x,y) for x,y in zip(range(len(GEN)), GEN)]
    TYP = ['Full Time', 'Part Time']
    TYPE = [(x,y) for x,y in zip(range(len(TYP)), TYP)]
    REF = [False,  True]
    REFER = [(x,y) for x,y in zip(range(len(REF)),REF)]

    name = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class':'form-control'}))
    mob_number = forms.CharField(min_length=10,max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.ChoiceField(choices=LOCATIONS,widget=forms.Select(attrs={'class' : 'dropdown'}))
    service = forms.ChoiceField(choices=OCCUPATIONS,widget=forms.Select(attrs={'class' : 'dropdown'}))
    doorstep_service =forms.ChoiceField(choices=DOORSTEP, widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    age_prefernce = forms.ChoiceField(choices=AGES, widget=forms.RadioSelect())
    availability = forms.ChoiceField(choices=AVAIL, widget=forms.RadioSelect(),
    required=False)
    wage_preference = forms.ChoiceField(choices=MINWAGE)
    exprience = forms.ChoiceField(choices=EXPE)
    certification = forms.ChoiceField(choices=CERTIFICATIONS, widget=forms.RadioSelect())
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.RadioSelect(), required=True)
    types = forms.ChoiceField(choices=TYPE, widget=forms.RadioSelect())
    reference = forms.ChoiceField(choices=REFER, widget=forms.RadioSelect())

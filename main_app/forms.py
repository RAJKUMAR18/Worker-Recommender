from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class Query(forms.Form):

    def __init__(self, *args, **kwargs):
        super(Query, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'query-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'result'

        self.helper.add_input(Submit('submit', 'Submit'))

    LOCS = ['Ambegaon', 'Aundh', 'Balewadi', 'Baner', 'Bavdhan', 'Bibewadi',
            'Camp', 'Chinchwad', 'Dattawadi', 'Deccan', 'Dhankawadi',
            'Dhayari', 'Dhole Patil Road', 'Erandwane',
            'Fatimanagar', 'Fursungi', 'Ganeshkhind', 'Ghorpadi',
            'Gultekdi', 'Hadapsar', 'Hinjewadi',
            'Katraj', 'Khadakwasla', 'Khadki', 'Kharadi', 'Kondhwa',
            'Koregaon Park', 'Kothrud', 'Mundhwa', 'Nigdi', 'Parvati',
            'Pashan', 'Paud Road', 'Pimplesaudagar', 'Sahakarnagar',
            'Salisbury Park', 'Saswad', 'Shivajinagar', 'Singhgad Road',
            'Swargate', 'Vishrantwadi', 'Vitthalwadi', 'Wagholi', 'Wanowrie']

    OCCS = ['Accountant', 'Brick mason', 'Carpenter', 'Cashier',
            'Childcare Worker', 'Cook', 'Delivery Boy', 'Driver',
            'Electrician', 'Hairdresser', 'Janitor', 'Maid', 'Mechanic',
            'Mehndi Artist', 'Painter', 'Plumber', 'Receptionist',
            'Salesperson', 'Security Guard', 'Tailor', 'Waiter',
            'Waitress', 'Worker']

    LOCATIONS = [(x, y) for x, y in zip(range(len(LOCS)), LOCS)]
    OCCUPATIONS = [(x, y) for x, y in zip(range(len(OCCS)), OCCS)]
    DOORSTEP = [(0, 'No'), (1, 'Yes')]
    AGES = [(0, '18-20'), (1, '21-25'), (2, '26-30'), (3, '30-35')]
    AVAIL = [(0, 'Afternoon'), (1, 'Evening'), (2, 'Morning'),
             (3, 'Whole Day')]
    WAGERANGE = ['1000-5000', '5001-8000', '8001-10000']
    MINWAGE = [(x, y) for x, y in zip(range(len(WAGERANGE)), WAGERANGE)]
    EXP = ['0-2', '3-6', '6-10']
    EXPE = [(x, y) for x, y in zip(range(len(EXP)), EXP)]
    CERT = [False, True]
    CERTIFICATIONS = [(x, y) for x, y in zip(range(len(CERT)), CERT)]
    GEN = ['Female', 'Male']
    GENDERS = [(x, y) for x, y in zip(range(len(GEN)), GEN)]
    TYP = ['Full Time', 'Part Time']
    TYPE = [(x, y) for x, y in zip(range(len(TYP)), TYP)]
    REF = [False, True]
    REFER = [(x, y) for x, y in zip(range(len(REF)), REF)]

    your_name = forms.CharField(label='Your Name',
                                max_length=12,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'w3-input \
                                        w3-border-blue w3-light-grey\
                                        w3-leftbar'
                                        }))

    mob_number = forms.CharField(label='Mobile Number',
                                 min_length=10,
                                 max_length=10,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'w3-input\
                                         w3-border-blue w3-light-grey\
                                         w3-leftbar'
                                         }))

    location = forms.ChoiceField(label='Location',
                                 choices=LOCATIONS,
                                 widget=forms.Select(
                                     attrs={
                                         'class': 'w3-container\
                                          w3-dropdown-click'
                                     }
                                 ),
                                 initial=0)

    service = forms.ChoiceField(label='Service',
                                choices=OCCUPATIONS,
                                widget=forms.Select(
                                    attrs={
                                        'class': 'w3-container w3-cell\
                                         w3-dropdown-click',
                                    }
                                ),
                                initial=0)

    doorstep_service = forms.ChoiceField(label='Door Step',
                                         choices=DOORSTEP,
                                         widget=forms.RadioSelect(),
                                         initial=0)

    age_prefernce = forms.ChoiceField(label='Age',
                                      choices=AGES,
                                      widget=forms.RadioSelect(),
                                      initial=0)

    availability = forms.ChoiceField(label='Availability',
                                     choices=AVAIL,
                                     widget=forms.RadioSelect(),
                                     required=True,
                                     initial=0)

    wage_preference = forms.ChoiceField(choices=MINWAGE, initial=1)

    experience = forms.ChoiceField(choices=EXPE, initial=1)

    certification = forms.ChoiceField(choices=CERTIFICATIONS,
                                      widget=forms.RadioSelect(),
                                      initial=0)

    gender = forms.ChoiceField(choices=GENDERS,
                               widget=forms.RadioSelect(), required=True,
                               initial=0)

    types = forms.ChoiceField(choices=TYPE, widget=forms.RadioSelect(),
                              initial=0)

    reference = forms.ChoiceField(choices=REFER, widget=forms.RadioSelect(),
                                  initial=0)

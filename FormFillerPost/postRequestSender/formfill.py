from bs4 import BeautifulSoup
#import requests
import random

class FormFiller:
    def __init__(self,htmlPath='',urlUniverse='',search_queries=[]):
        # use HTML path is file has to be opened. Suggestion : Use urlUniverse, it takes the HTML directly
        if(len(htmlPath)>0):
            self.html=open(htmlPath,'r',encoding='utf-8').read()
        else:
            self.html=urlUniverse

        #print(self.html)
        #self.html=self.html.lower()
        self.html_bs=BeautifulSoup(self.html,'html.parser')
        #find inputs starts here
        self.potential_inputs=self.html_bs.find_all(['input','textarea'])

        self.forms_on_page=self.html_bs.find_all(['form'])

        #print(self.forms_on_page)


        self.email_list=open('postRequestSender/email_list.csv','r').read()
        self.email_list=self.email_list.split('\n')      ## List of Emails

        self.name_list=open('postRequestSender/name_list.csv','r').read()
        self.name_list=self.name_list.split('\n')        ## List of names / usernames

        self.pass_list=open('postRequestSender/pass_list.csv','r').read()
        self.pass_list=self.pass_list.split('\n')        ## List of passwords

        self.search_list = []
        self.search_list = ['bat','cricket','book','amazon','car']
        for each_query in search_queries:
            self.search_list.append(each_query)
        self.other_hidden=[]
        self.other_hidden_dict={}
        form_inputs=[]

        for some_var in range(len(self.forms_on_page)):
            input_tags_form = self.forms_on_page[some_var].find_all(['input'])
            for iterable_input in input_tags_form:
                form_inputs.append(iterable_input)

        for input_tag_all in self.potential_inputs:
            if(input_tag_all not in form_inputs):
                self.other_hidden.append(input_tag_all)
        
        for hidden_iter in self.other_hidden:
            try:
                self.other_hidden_dict[hidden_iter.attrs['name']]=hidden_iter['value']
            except:
                pass
    

    def addSearchQuery(self,search_queries=[]):
        # allows addition of search query
        for each_query in search_queries:
            self.search_list.append(each_query)
    
    @property
    def clearSearchQuery(self):
        # allows clearing the seach query
        self.search_list = []


    def scrapeWebPage(self):
        # the parser and interpreter, returns a list of [ 'Action' , 'Request Type', 'Unfilled', 'Reqest Data to be sent' ] for each form on the webpage
        search_tags= ['search','find','look','seek','explore','scout','examine','check','inspect','locate']
        names_finder=['tag','alias','head','name','username','user']
        mail_finder=['mail','post','deliver','send','sent','forward','dispatch','ship','address']
        password_finder=['pass','password','key','access','token','secret','sign','code','catchword','signal','ticket','cipher','identification','countersign','buzz','motto','clue','login','cred','crypt','answer','open sesame','inside','message','evidence','pin']
        gender_finder=['gender','sex']

        self.post_requests=[]
        typeOfForm = 'F'



        for form_i in self.forms_on_page:
            temp_request=[]
                    
            current_form_details=[]

            self.name_candidates=[]
            self.password_candidates=[]
            self.email_candidates=[]
            self.gender_candidates=[]
            
            self.required_data = []
            self.req_uncommon_data={}

            self.action_form=[]
            self.action_candidates=[]

            self.hidden_inputs=[]
            
            self.checkbox = []
            self.radio=[]

            self.select_tags=[]

            current_form_method = ''
            
            if('action' in form_i.attrs):
                self.action_form.append(form_i.attrs['action'])
                
                current_form_details.append(form_i.attrs['action'])
            else:
                current_form_details.append('No Action')
                #current_form_details.append({})

            for each_search in search_tags:
                if(each_search in current_form_details[0]):
                    typeOfForm = 'S'
                    continue

            if('method' in form_i.attrs):
                try:
                    # if method attribute has no value then it goes to except
                    if(form_i.attrs['method'].lower() != ''):
                        # if method isn't empty, give the method
                        current_form_method = form_i.attrs['method'].lower()
                    else:
                        current_form_method = 'post'
                except:
                    # if method attribute exists, but without value
                    current_form_method = 'post'
            else:
                # method does not exist so.post
                current_form_method = 'post'
            
            current_form_details.append(current_form_method)
            current_form_details.append(self.other_hidden_dict)
            
            self.potential_inputs=form_i.find_all(['input','select'])

            #all_input_names = []



            self.select_tags = form_i.find_all(['select'])
            
            select_tag_dictonary ={}







            for current_input in self.potential_inputs:
                if(current_input in self.select_tags):
                    each_select_tag = current_input
                    each_select_attrs = each_select_tag.attrs

                    if('name' in each_select_attrs):
                        if(each_select_attrs['name'] not in select_tag_dictonary):
                            select_tag_dictonary[each_select_attrs['name']]=[]

                    options_in_each_select = []
                    options_in_each_select = each_select_tag.find_all(['option'])
                    option_values=[]
                    for each_option in options_in_each_select:
                        #print(each_option.attrs)
                        if('value' in each_option.attrs):
                            if(each_option['value'] != ''):
                                option_values.append(each_option.attrs['value'])
                            #print(option_values)
                        else:
                            pass
                            #select_tag_dictonary[each_select_attrs['name']]='0'
                    total_options = len(option_values)
                    if(total_options>80):
                        total_options=80
                    select_tag_dictonary[each_select_attrs['name']]=random.choice(option_values[int(total_options/10):total_options])
                    #print(select_tag_dictonary)

                else:
                    attributes_current_input=current_input.attrs
                    
                    if('type' in attributes_current_input):
                        if('hidden' in attributes_current_input['type'].lower()):
                            self.hidden_inputs.append(current_input)
                            continue
                        if('checkbox' in attributes_current_input['type'].lower()):
                            self.checkbox.append(current_input)
                            continue
                        if('radio' in attributes_current_input['type'].lower()):
                            self.radio.append(current_input)
                            continue
                    if('required' in attributes_current_input):
                        self.required_data.append(current_input)


                    
                    #placeholder-prediction
                    if('placeholder' in attributes_current_input):
                        if(attributes_current_input['placeholder'].lower() in search_tags):
                            typeOfForm='S'
                        for name_i in names_finder:
                            if(name_i in attributes_current_input['placeholder'].lower()):
                                self.name_candidates.append(current_input)         
                        for mail_i in mail_finder:
                            if(mail_i in attributes_current_input['placeholder'].lower()):
                                self.email_candidates.append(current_input)
                        for pass_i in password_finder:
                            if(pass_i in attributes_current_input['placeholder'].lower()):
                                self.password_candidates.append(current_input)
                        for gender_i in gender_finder:
                            if(gender_i in attributes_current_input['placeholder'].lower()):
                                self.gender_candidates.append(current_input)

                    #name-prediction
                    if('name' in attributes_current_input):
                        for search_i in search_tags:
                            if(search_i in attributes_current_input['name'].lower()):
                                typeOfForm='S'

                        for gender_i in gender_finder:
                            if(gender_i in attributes_current_input['name'].lower()):
                                continue
                                #self.gender_candidates.append(current_input)

                        if(attributes_current_input['name'].lower() in ['password','pass','key','user']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                self.email_candidates.remove(current_input)
                            if(current_input in self.password_candidates):
                                continue    
                            self.password_candidates.append(current_input)

                        if('mail' in attributes_current_input['name'].lower()):
                                    self.email_candidates.append(current_input)
                        if(attributes_current_input['name'].lower() in ['email','email','user']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                self.password_candidates.remove(current_input)    
                            self.email_candidates.append(current_input)

                        elif(attributes_current_input['name'].lower() in names_finder):
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                continue
                            if(current_input in self.name_candidates):
                                continue
                            self.name_candidates.append(current_input)
                        else:
                            _=1



                    #type-prediction
                    if('type' in attributes_current_input):
                        if('action' in attributes_current_input['type'].lower()):
                            self.action_candidates.append(current_input)

                        if(attributes_current_input['type'] not in ['password','email','text','hidden','reset','submit','search','button','image','text']):
                            self.req_uncommon_data[current_input]=attributes_current_input['type']

                        if(attributes_current_input['type'].lower() in ['password']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                self.email_candidates.remove(current_input)
                            if(current_input in self.password_candidates):
                                continue    
                            self.password_candidates.append(current_input)

                        elif(attributes_current_input['type'].lower() in ['email']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                self.password_candidates.remove(current_input)    
                            self.email_candidates.append(current_input)

                        elif(attributes_current_input['type'].lower() in ['text']):
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                continue
                            if(current_input in self.name_candidates):
                                continue
                            self.name_candidates.append(current_input)
                        else:
                            self.name_candidates.append(current_input)
                            _=1

                    
                    #value-prediction
                    if('value' in attributes_current_input):
                        if(attributes_current_input['value'].lower() in ['password','pass','key','user']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                self.email_candidates.remove(current_input)
                            if(current_input in self.password_candidates):
                                continue    
                            self.password_candidates.append(current_input)

                        elif(attributes_current_input['value'].lower() in ['email','email','user']):
                            if(current_input in self.name_candidates):
                                self.name_candidates.remove(current_input)
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                self.password_candidates.remove(current_input)    
                            self.email_candidates.append(current_input)

                        elif(attributes_current_input['value'].lower() in names_finder):
                            if(current_input in self.email_candidates):
                                continue
                            if(current_input in self.password_candidates):
                                continue
                            if(current_input in self.name_candidates):
                                continue
                            #self.name_candidates.append(current_input)
                        else:
                            self.name_candidates.append(current_input)
                            _=1
                #end-for-current-input
            #find inputs stops .... we have the inputs located
        

            hidden_dictonary = {}       # Thiis has the hidden input tags in name : value format
            other_hidden_stuff=[]       # Since it was hidden , it might be useful
            for data_hidden in self.hidden_inputs:
                if('name' in data_hidden.attrs):
                    if('value' in data_hidden.attrs):
                        if(data_hidden.attrs['value'] != ''):
                            hidden_dictonary[data_hidden.attrs['name']]=data_hidden.attrs['value']
                        else:
                            #hidden_dictonary[data_hidden.attrs['name']]='0'
                            pass
                    else:
                        #hidden_dictonary[data_hidden.attrs['name']]='0'
                        pass

                else:
                    other_hidden_stuff.append(data_hidden.attrs)        ## List of dictonaries

            checkbox_list={}
            for checkbox_i in self.checkbox:
                if(checkbox_i.attrs['name'] not in checkbox_list):
                    checkbox_list[checkbox_i.attrs['name']]=checkbox_i.attrs['value']
                else:
                    _=1

            radio_list={}
            for radio_i in self.radio:
                if(radio_i.attrs['name'].lower() not in radio_list):
                    radio_list[radio_i.attrs['name'].lower()] = radio_i.attrs['value']


            username_name=[]        # Username names for post request
            password_name=[]        # Password names for post request
            email_name=[]           # E - Mail names for post request

            

            gender=[]
            gender_type=['M','F']
            gender_type=gender_type[random.randint(0,1)]
            cant_fill = []
            for gender_i in self.gender_candidates:
                gender.append([gender_i.attrs['name'],gender_type])

            for name_var in self.name_candidates:
                if('name' in name_var.attrs):
                    if('type' in name_var.attrs):
                        if(name_var.attrs['type'].lower() == 'submit'):
                            continue
                    username_name.append(name_var.attrs['name'])
                else:
                    cant_fill.append(name_var)

            for email_var in self.email_candidates:
                if('name' in email_var.attrs):
                    email_name.append(email_var.attrs['name'])
                else:
                    cant_fill.append(email_var)

            for pass_var in self.password_candidates:
                if('name' in pass_var.attrs):
                    password_name.append(pass_var.attrs['name'])
                else:
                    cant_fill.append(pass_var)


            request_bodies=[]

            request_no=0
            
            request_body_dict={}

            action_list=[]      ## action to be carried out in post request
            url_list=[]         ## the url in post request
            validate_list=[]    ## .php file name // Validation .php file

            
            for url_i in self.action_form:
                if('.php' in url_i):
                    validate_list.append(url_i)
                    action_list.append(url_i)
                else:
                    url_list.append(url_i)
                    action_list.append(url_i)



            for hidden_name in hidden_dictonary:
                request_body_dict[hidden_name]=hidden_dictonary[hidden_name]
            


            random_number=random.randint(0,len(self.name_list)-1)
            
            for name_i in username_name:
                if(typeOfForm=='S'):
                    request_body_dict[name_i]  =self.search_list[random.randint(0,len(self.search_list)-1)]
                else:
                    request_body_dict[name_i]=self.name_list[random_number]


            for email_i in email_name:
                request_body_dict[email_i]=self.email_list[random_number]

            for pass_i in password_name:
                request_body_dict[pass_i]=self.pass_list[random_number]


            for select_i in select_tag_dictonary:
                if('pronoun' not in select_i):
                    request_body_dict[select_i] = select_tag_dictonary[select_i]

            for gender_i in gender:
                request_body_dict[gender_i[0]]=gender_i[1]

            for radio_i in radio_list:
                request_body_dict[radio_i]=radio_list[radio_i]

            for checkbox_i in checkbox_list:
                request_body_dict[checkbox_i]=checkbox_list[checkbox_i][random.randint(0,len(checkbox_list[checkbox_i])-1)]
            

            temp_req_dict={}
            for request_name in request_body_dict:
                if('age' in request_name):
                    age_addition=''
                    bday_recognize=['day','birth','bday','birthday','bdate']
                    age_allowed=0
                    for select_tag_i in select_tag_dictonary:
                        for birth_i in bday_recognize:
                            if(birth_i in select_tag_i.lower()):
                                age_allowed=1
                                continue
                        
                        if(age_allowed==1):
                            age_addition = age_addition+select_tag_dictonary[select_tag_i]+','
                            age_allowed=0

                    age_addition=age_addition[:-1]
                    temp_req_dict[request_name] = age_addition


                else:
                    if('gender' in request_name and len(request_body_dict)>1):
                        continue
                    temp_req_dict[request_name]=request_body_dict[request_name]
                
            arranged_request={}

            for input_i in self.potential_inputs:
                if('name' in input_i.attrs):
                    if(input_i.attrs['name'] in temp_req_dict):
                        arranged_request[input_i.attrs['name']]=temp_req_dict[input_i.attrs['name']]
                    else:
                        continue
                        print("\n Data not filled for ")
                        print(str(input_i))
                else:
                    continue
                    print("\n No name found for input tag : ")
                    print(str(input_i))

            if(typeOfForm =='S'):
                current_form_details[1]='get'
            #current_form_details.append(cant_fill)
            current_form_details.append(arranged_request)
            ##print(arranged_request)
            #print(select_tag_dictonary)
            self.post_requests.append(current_form_details)
        
        
        
        return self.post_requests

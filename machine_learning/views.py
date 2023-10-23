from django.shortcuts import render

import joblib


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def user_entry(request):
    return render(request,'user_entry.html')
def last_result(request):
     if request.method == 'POST':

        age = request.POST.get('age')
        print(age)
        department = request.POST.get('department')
        print(department)
        distance = request.POST.get('distance')
        print(distance)
        gender = request.POST.get('gender')
        
        print(gender)
        job_satisfaction = request.POST.get('job_satisfaction')
        print(job_satisfaction)
        marital_status = request.POST.get('marital_status')
        print(marital_status)
        overtime = request.POST.get('overtime')
        print(overtime)
        salary_hike = request.POST.get('salary_hike')
        print(salary_hike)
        years_promotion = request.POST.get('years_promotion')
        print(years_promotion)
        print('a')
        import os
        import pickle
        print('vijay...')
        loaded_model = joblib.load('/Users/sukhpreetsingh/Documents/david_machine/david/ml/model_david.pkl 1.48.03 AM 1.52.13 AM')
        print('david')
        print(loaded_model )
        #now we will convert the string into integers
        gender_dict={'female':2,'male':1}
        department_dict={'Sales':1,'Research & Development':2,'Human Resources':3}
        marital_status_dict={'single':1,'married':2,'divorced':3}
        new_gender=gender_dict.get(gender)
        print(new_gender)
       
        new_department=department_dict.get(department)
        print(new_department)
        new_maritial=marital_status_dict.get(marital_status)
        
       
        over_time={'yes':1,'no':2}
        over_time_new=over_time.get(overtime)
        print(over_time_new)
        # Convert the elements in input_data to the corresponding types
        input_data = [
        [int(age), int(new_department), float(distance), int(new_gender), int(job_satisfaction),
        int(new_maritial), int(over_time_new), float(salary_hike), int(years_promotion)]]


        print(input_data)
        prediction = loaded_model.predict(input_data)
        print('....david....')
        print(prediction)
        a=prediction[0]
        if a==0:
            new_variable='no'
        else:
            new_variable='yes'
            
        context = {
            'age': age,
            'department': department,
            'distance': distance,
            'gender': gender,
            'job_satisfaction': job_satisfaction,
            'marital_status': marital_status,
            'overtime': overtime,
            'salary_hike': salary_hike,
            'years_promotion': years_promotion,
            'prediction_flag': new_variable,
        }
        
        return render(request, 'last_page.html', context)    



       

# Construct the absolute path to the model file
        
# Load the model
        

    



   

    
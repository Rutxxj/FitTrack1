from django.shortcuts import render,redirect
import json
import requests
from .forms import CreateUserForm,WeightMeasurementForm,FoodForm,BMRForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import WeightMeasurement,Food,FoodLog,UserProfile,BMRMeasurement
from django.utils import timezone
from django.contrib import messages
from django.db.models import Sum

#gYfQIby6xn84SiFD2e1HXQ==CZe4Z78BmEy7u8Uq
# Create your views here.

def index(req):
    pass
    return render(req,"base.html")

def calorie(req):
    
    if req.method == "POST":
        query= req.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_req = requests.get (api_url + query,headers={'X-Api-Key':'5UUgUqry0HJVQhtOA41i1Q==4VK2UiBxSmhBwjT9'})
        try:
            api =json.loads(api_req.content)
            print(api_req.content)
        except Exception as e:
            api ="Oops There was an error"
            print(e)
        return render (req,'findcalories.html',{'api':api})
    else:
        return render (req,'findcalories.html',{'query':'Enter valid'})

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register(req):
    form = CreateUserForm()
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(req, "User Created Successfully")
                return redirect('/login')
            else:
                raise ValueError("""Incorrect Password Format 
                                 Password must contain Include uppercase and lowercase letters,
                                 Include numbers,
                                 Include symbols""")
        except ValueError as e:
            messages.error(req, str(e))
    context = {'form': form}
    return render(req, "register.html", context)

def login_view(req):
    if req.method == 'POST':
        try:
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                messages.success(req, "Login Successfully")
                return redirect("/")
            else:
                raise ValueError("Invalid username or password.")
        except ValueError as e:
            messages.error(req, str(e))
            return redirect("/login")
    else:
        return render(req, 'login.html')

def logout_view(req):
    try:
        logout(req)
        messages.success(req, "You have logged Out Successfully")
    except Exception as e:
        messages.error(req, str(e))
    return redirect("/")


@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightMeasurementForm(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            return redirect('add_weight')
    else:
        form = WeightMeasurementForm()
    user_weight_log = WeightMeasurement.objects.filter(user=request.user).order_by('date')
    return render(request, 'user_profile.html', {'form': form,
        'user_weight_log': user_weight_log})

@login_required
def weight_log_delete(request, weight_id):
    weight_recorded = WeightMeasurement.objects.filter(id=weight_id)

    if request.method == 'POST':
        weight_recorded.delete()
        return redirect('add_weight')

    return render(request, 'weight_log_delete.html')

def food_list_view(request):
    foods = Food.objects.all()        
    return render(request, 'index.html', {'foods': foods,'title': 'Food List'})

@login_required
def food_add_view(request):
    if request.method == 'POST':
        food_form = FoodForm(request.POST, request.FILES)
        if food_form.is_valid():
            new_food = food_form.save(commit=False)
            new_food.user = request.user
            new_food.save()
            return render(request, 'food_add.html', {'food_form': FoodForm(),'success': True})
        else:
            return render(request, 'food_add.html', {'food_form': FoodForm()})
    else:
        return render(request, 'food_add.html', {'food_form': FoodForm()})

def daydate(request):
    today = timezone.now()
    day = today.strftime("%A")  
    date = today.strftime("%Y-%m-%d")  
    context = {'day': day, 'date': date}  
    return render(request,'food_log.html',context)

@login_required
def food_log_view(request):
    if request.method == 'POST':
        foods = Food.objects.all()
        food = request.POST['food_consumed']
        food_consumed = Food.objects.get(food_name=food)
        user = request.user
        food_log = FoodLog(user=user, food_consumed=food_consumed)
        food_log.save()
    else:
        foods = Food.objects.all()
    user_food_log = FoodLog.objects.filter(user=request.user)
    total_calories = user_food_log.aggregate(total_calories=Sum('food_consumed__calories'))['total_calories'] or 0
    total_proteins = user_food_log.aggregate(total_proteins=Sum('food_consumed__protein'))['total_proteins'] or 0
    total_fats = user_food_log.aggregate(total_fats=Sum('food_consumed__fat'))['total_fats'] or 0

    return render(request, 'food_log.html', {
        
        'foods': foods,
        'user_food_log': user_food_log,
        'total_calories': total_calories,
        'total_proteins': total_proteins,
        'total_fats': total_fats,
        
    })

@login_required
def food_log_delete(request, food_id):
    food_consumed = FoodLog.objects.filter(id=food_id)
    if request.method == 'POST':
        food_consumed.delete()
        return redirect('food_log_view')
    return render(request, 'food_log_delete.html')

def calculate_bmr_formula(age, weight, height, gender):
    if gender == 'M': 
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'F':  
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Must be 'M' or 'F'.")

    return bmr

@login_required
def calculate_bmr(request):
    if request.method == 'POST':
        form = BMRForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            gender = form.cleaned_data['gender']
            
            
            bmr = calculate_bmr_formula(age, weight, height, gender)
            
            
            bmr_entry = BMRMeasurement(user=request.user, bmr=bmr)
            bmr_entry.save()
            
            return redirect('calculate_bmr')
    else:
        form = BMRForm()
    
    user_bmr_log = BMRMeasurement.objects.filter(user=request.user)
    return render(request, 'calculate.html', {'form': form, 'user_bmr_log': user_bmr_log})

@login_required
def bmr_log_delete(request, bmr_id):
    bmr_recorded = BMRMeasurement.objects.filter(id=bmr_id)

    if request.method == 'POST':
        bmr_recorded.delete()
        return redirect('calculate_bmr')

    return render(request, 'bmr_log_delete.html')
    





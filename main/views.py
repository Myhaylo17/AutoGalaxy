from django.shortcuts import get_object_or_404
from .models import Car
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import FordRental
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.db import connections
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

@csrf_exempt
def ford_rent_car(request):
    if request.method == "POST":
        rental_duration = request.POST.get("rental_duration")
        payment_method = request.POST.get("payment_method")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone_number")
        rental_date = request.POST.get("rental_date")
        car_model = request.POST.get("car_model")
        price = request.POST.get("price")

        if not rental_duration or not payment_method:
            return JsonResponse({
                "success": False,
                "error": "Rental duration and payment method are required"
            })

        rental = FordRental.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone,
            rental_date=rental_date,
            rental_duration=rental_duration,
            payment_method=payment_method,
            car_model=car_model,
            price=price
        )

        return JsonResponse({"success": True, "id": rental.id})


def login_s(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Перевірка користувача
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Вітаємо, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Неправильний логін або пароль.')
                return redirect('login')
        else:
            messages.error(request, 'Форма заповнена некоректно.')
            return redirect('login')

    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html')

def register(request):
    print("Виконується register")
    if request.method == 'POST':
        username = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Перевіряємо, чи користувач вже існує у базі users_db
        if User.objects.using('users_db').filter(username=username).exists():
            messages.error(request, "Такий логін вже існує!")
            return redirect('register')

        # Створюємо користувача у базі users_db
        user = User.objects.db_manager('users_db').create_user(
            username=username,
            email=email,
            password=password
        )
        user.save(using='users_db')

        # Закриваємо з’єднання, щоб уникнути блокувань у MySQL
        connections['users_db'].close()

        messages.success(request, "Реєстрація успішна! Тепер увійдіть.")
        return redirect('login')

    return render(request, 'main/register.html')


def home(request):
    popular_cars = [
        ##First line

        {'make': 'Audi', 'model': 'A6', 'year': 2022, 'description': 'Luxury sedan', 'price': 55000},
        {'make': 'BMW','model': 'i8', 'year': 2022,'description': 'Luxury sport car with excellent performance.', 'price': 140000,},
        {'make': 'Audi','model': 'Q8','year': 2022,'description': 'Luxury  car with excellent performance.','price': 150000,},
        {'make': 'Audi','model': 'etron','year': 2023,'description': 'Electric SUV with advanced features.','price': 100000,},
        {'make': 'Porsche','model': '911 GT3','year': 2018,'description': 'Sporty, elegant, high-speed dream car.','price': 350000,},
        {'make': 'Volkswagen','model': 'golf','year': 2021,'description': 'Compact, practical,versatile hatchback.','price': 23000,},

        ##Second line
        {'make': 'Mercedes','model': 'benz','year': 2016,'description': 'Super comfortly car','price': 115000,},
        {'make': 'Tesla','model': 'Model X','year': 2021,'description': 'Electric SUV with excellence.','price': 50000,},
        {'make': 'Audi','model': 'Q5','year': 2023,'description': 'Luxury SUV with versatile performance.','price': 60000,},
        {'make': 'Volkswagen','model': 'jetta','year': 2020,'description': 'Compact sedan with great performance.','price': 30000,},
        {'make': 'Porsche','model': '911','year': 2017,'description': 'Iconic sports car with great power.','price': 275000,},
        {'make': 'BMW','model': 'x5','year': 2021,'description': 'Luxury SUV with powerful performance.','price': 50000,},

        ##Third line
        {'make': 'Volkswagen','model': 'Pasat','year': 2022,'description': 'Reliable sedan with great performance.','price': 32000,},
        {'make': 'Tesla','model': 'Model s','year': 2018,'description': 'Luxury electric sedan with top power.','price': 30000,},
        {'make': 'Porsche','model': 'Taycan','year': 2022,'description': 'Sport car','price': '220000', },
        {'make': 'Tesla','model': 'Model 3','year': 2019,'description': 'Electric sedan with strong performance.','price': 30000,},
        {'make': 'BMW','model': 'I7','year': 2023,'description': 'Luxury electric sedan with strong power.','price': 110000,},
        {'make': 'Ford','model': 'Ranger','year': 2023,'description': 'Durable pickup with top performance.','price': 75000,},


    ]
    return render(request, 'main/about.html', {'popular_cars': popular_cars})



def bmw_page(request):
    return render(request, 'main/bmw.html')


def mercedes_page(request):
    return render(request, 'main/mercedes.html')

def audi_page(request):
    return render(request, 'main/audi.html')

def ford_page(request):
    return render(request, 'main/Ford.html')

def porsche_page(request):
    return render(request, 'main/Porsche.html')

def tesla_page(request):
    return render(request, 'main/Tesla.html')

def volswagen_page(request):
    return render(request, 'main/Volswagen.html')
def about_us_page(request):
    return render(request, 'main/about_us.html')
def car_enter(request):
    return  render(request, 'main/car_enter.html')


def car_list(request):
    cars = Car.objects.all()  # Отримуємо всі машини
    return render(request, 'car_enter.html', {'cars': cars})



def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    # Логіка покупки (наприклад, створення замовлення)
    # Після успішної покупки перенаправляємо користувача
    return redirect('success_page')


def purchase_car(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення після успішної покупки
    else:
        form = PurchaseForm()
    return render(request, 'buying_car.html', {'form': form})


def reserve_bmw(request):
    # Ця функція відобразить шаблон, розташований за шляхом 'main/reserve_bmw.html'.
    # Вам потрібно буде створити цей HTML-файл у директорії 'templates/main/'
    # всередині вашого додатку 'main'.
    return render(request, 'main/reserve_bmw.html', {})
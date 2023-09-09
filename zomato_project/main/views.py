from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password
from .models import Category,Foods
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.db.models import Q









# Create your views here.


def index(request):
    return render (request,'index.html')
    

def Relations(request):
    return render (request,'relations.html')


def login(request):
    return render (request,'login.html')

def signup(request):
    
     return render (request,'signup.html')
 
def getapp(request):
    
     return render (request,'getapp.html')

 
def verification(request):
    
    return render (request,'verification.html')

def cart(request):

 return render (request,'cart.html')

def gpay(request):

 return render (request,'gpay.html')

def cod(request):

 return render (request,'cod.html')




    
    



def getapp(request):
    if request.method == 'POST':
        message = request.POST.get('message', ' https://play.google.com/store/apps/details?id=com.application.zomato&hl=en_IN&gl=US, CLICK THIS LINK  TO DOWNLOAD ZOMATO ')
        email = request.POST['email']
        
        send_mail(
            'GET ZOMATO APP',
            message,
            settings.EMAIL_HOST_USER,  
            [email],
            fail_silently=False
        )
    return render(request, 'getapp.html')
 

def generate_verification_code():
    return str(random.randint(1000, 9999))


def signup(request):
    if request.method == 'POST':
        message = request.POST.get('message', generate_verification_code())
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password'] 
        

        
        
        
        request.session['email'] = email
        request.session['verification_message'] = message
        request.session['User_name'] = name
        request.session['password'] = password
        
        
        
        send_mail(
            'verification code',
            message,
            settings.EMAIL_HOST_USER,  
            [email],
            fail_silently=False
        )
        return redirect('verification')
     
    return render (request, 'signup.html')



    
def verification(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')

       
        expected_code = request.session.get('verification_message')
        user_name = request.session.get('User_name')
        password = request.session.get('password')
        email = request.session.get('email')
        
        user=User.objects.create_user(username=user_name,password=password,email=email)

        
        
        if entered_code == expected_code:
            
            
            
            user.save()
            return redirect('yes')
        else:
            
            messages.info(request,"Verification Code is Incorrect")
            return redirect('verification')

    return render(request, 'verification.html')



def login(request):
    if request.method == 'POST':
    
        password = request.POST['password']
        user_name = request.POST['name']
        user=auth.authenticate(username=user_name, password=password) 
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request,"Username Or Password is Incorrect")
            return redirect('login')
    return render(request, 'login.html')



def Cuisines(request):
    category = Category.objects.filter(status=0)
    
    
    
    return render(request, 'cuisines.html', {"category": category})






def yes(request):
    user = request.session.get('User_name')
    return render(request, 'yes.html', {'user': user})



def foodview(request, cate_slug, food_slug):
    try:
       
        category = get_object_or_404(Category, slug=cate_slug, status=0)
    except Category.DoesNotExist:
        
        messages.error(request, "Error")
        return redirect("food")

    
    foo = Foods.objects.filter(slug=food_slug, status=0)

    
    if not foo.exists():
        messages.error(request, "No such product found")
        return redirect('food_category')

    if request.method == 'POST':
        
        quantity = int(request.POST.get('quantity',0))

        
        if quantity <= 0:
              total_price = 0
        else:
           
            first_price = foo.first().price * quantity
            total_price = first_price + 54
            name = foo.first().name if foo.exists() else None
            image = foo.first().food_image.url
            price = foo.first().price
            
            request.session['first_price'] = first_price
            request.session['price'] = price
            request.session['image'] = image
            request.session['name'] = name
            request.session['quantity'] = quantity
            request.session['total_price'] = total_price

           
            return redirect('cart', cate_slug=cate_slug, food_slug=food_slug)

    
    total_price = request.session.get('total_price', 0)

    
    return render(request, 'foodsview.html', {"foo": foo, "total_price": total_price})










def cart(request, cate_slug, food_slug):
    if request.method == 'POST':
        email = request.POST['email']
        payment_method = request.POST.get('payment-method')
        message = request.POST.get('message', 'HI your Order is on the way, stay patient while our delivery partner does their job, THANK YOU From Zomato')

        if payment_method == 'gpay':
            return redirect('gpay')  
        elif payment_method == 'cod':
            send_mail(
                'Zomato',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            return redirect('cod')


    
    first_price = request.session.get('first_price')
    name = request.session.get('name')
    total_price = request.session.get('total_price')
    quantity = request.session.get('quantity')
    category_slug = cate_slug
    food_slug = food_slug

    context = {
        'total_price': total_price,
        'quantity': quantity,
        'name': name,
        'first_price': first_price,
        'category_slug': category_slug,
        'food_slug': food_slug,
    }

    return render(request, 'cart.html', context)









def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')  
        
        
        matched_categories = Category.objects.filter(name__icontains=search_query, status=0)
        
        
        for category in matched_categories:
            if(Category.objects.filter(slug=category.slug, status=0).exists()):
                return redirect('food', slug=category.slug)
        
        context = {
            'categories': matched_categories  
        }
        
        return render(request, 'search.html', context)

def food(request, slug):
    foods = Foods.objects.filter(category__slug=slug, status=0)
    
    context = {
        'foods': foods
    }
    
    return render(request, 'foods.html', context)

    

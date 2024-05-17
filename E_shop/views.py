from msilib.schema import PublishComponent
from django.shortcuts import redirect,render
from E_shop.settings import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRECT
from store_app.models import Product,Categories,Filter_Price,Brand,contact_us,Order,orderitem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

import razorpay

client = razorpay.Client(auth=(RAZORPAY_KEY_ID ,RAZORPAY_KEY_SECRECT))

def base(request):
    
     
     return render(request,'base.html')

def home(request):
    product = Product.objects.filter(status='publish')
  
    data = {
        'product':product,
    }
    return render(request,'index.html',data)

def product(request):
     product = Product.objects.filter(status='publish')
     categories = Categories.objects.all()
     filter_price = Filter_Price.objects.all()
     brand = Brand.objects.all()

     CATID = request.GET.get('categories')
     
     if CATID:
        product = Product.objects.filter(categories = CATID)
     else:
        product = Product.objects.filter(status = 'publish')  
     context = {
         'product':product,
         'categories':categories,
         'filter_price':filter_price,
         'brand':brand
    }
     return render(request,'product.html',context)


def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name = query)

    context = {
        'product':product
    }
    return render(request,'search.html',context)

def product_single(request,id):
    prod = Product.objects.filter(id=id).first()
    context = {
        'prod':prod,
    }
    return render(request,'product_single.html',context) 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        subject = subject
        message = message
        email_from = 'vishvpatel3182@gmail.com'
        to = 'vishv31802.com'
        try:
            send_mail(subject,message,email_from,[to])
            contact.save()
            return redirect('home')
        except:
            return redirect('contact')
    return render(request,'contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('register')

    return render(request,'register.html')

def login(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(username=username,password=password)

         if user is not None:
             auth_login(request,user)
             return redirect('home')
         
         else:
             return redirect('login')
         
     return render(request,'register.html')


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'cart_details.html')

def check_out(request):
    #amount = request.POST.get('amount')
  
    
    payment = client.order.create({
        "amount":'500',
        "currency":"INR",
        "payment_capture":"1"
    })
    
    order_id = payment['id']
    context = {
        'order_id':order_id,
        'payment':payment
    }
    return render(request,'checkout.html',context)

def placeorder(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        order_id = request.POST.get('order_id')
        cart = request.session.get('cart')

       
        new = Order(
            firstname=firstname,
            country=country,
            address=address,
            city=city,
            postcode=postcode,
            phone=phone,
            order_id=order_id
          
        )
        new.save()
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a*b
            print(total)
            item = orderitem(
               user = User,
               order = new,
               product = cart[i]['name'],
               image = cart[i]['image'],
               quantity = cart[i]['quantity'],
               price = cart[i]['price'],
               total = total
            )
            item.save()
    return render(request,'placeorder.html')

def thank(request):
    return render(request,'thank.html')

def your_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)
    order = orderitem.objects.filter(user=user)
    print(order)
    return render(request,'your_order.html')


def wishlist(request):
    return render(request,'wishlist.html')



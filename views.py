from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from datetime import datetime
from home.models import Contact,Product,Cart,CartItem,Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('message')
        date = datetime.today()
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)
        contact.save()
        messages.success(request,'Your message has been received. We will get back you shortly.')
    return render(request,'contact.html')

@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,product_id=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item,created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        cart_item.quantity +=1
    cart_item.save()
    messages.success(request,'Item added to cart successfully.')
    return index(request)

def cart_details(request):
    cart = get_object_or_404(Cart,user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price for item in cart_items)
    context = {'cart_items':cart_items,'total_price':total_price}
    return render(request,'cart.html',context)

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Cart,Products,Category,Images_product
from django.db.models import Q

# Create your views here.


def login_page(request):
    if request.method=="POST":
            username=request.POST.get("user")
            password=request.POST.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")    
            else:
                messages.error(request,"invalid credentials")
                return redirect("signup")
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
            username=request.POST.get("user") 
            password=request.POST.get("password") 
            if username=="" or password=="" :
                if username=="":
                    messages.error(request,"user name are not be null")
                else:
                    messages.error(request,"password are not be null")
            elif username==password:
                messages.error(request,"user name and password are not equal ")

            elif len(password)<6:
                messages.error(request,"password must contain atleast 6 characters") 
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request,"user already taken")
                    return render(request,"signup.html")
                else:
                    user=User.objects.create_user(username=username,password=password)
                    user.save()
                    messages.success(request,"submitted successfully")
                    return redirect("login_page")
    return render(request,"signup.html")


def len_ct(request):
    task=Category.objects.prefetch_related("Products").all()
    return render(request,"home.html",{"product":task})
 
def home(request):
    task=Category.objects.prefetch_related("Products").all()
    tk=Cart.objects.filter(user=request.user)
    v=len(tk)
    return render(request,"home.html",{"product":task,"len_cart":v})


def add_content(request,id): 
    f=Products.objects.get(id=id) 
    pic=f.pic.url
    title=f.title
    content=f.content
    cost=f.cost
    print(pic)
    k=Cart(user=request.user,pic=pic,title=title,content=content,cost=cost)  
    k.save() 
    return redirect("home")

def cart(request): 
    task=Cart.objects.filter(user=request.user)
    v=task.count
    sum=0
    for i in task:
        sum=i.cost+sum 
    return render(request,"cart.html",{"products":task , "sum":sum , "len_cart":v})


def delete_content(request,id): 
    d=Cart.objects.get(user=request.user,id=id) 
    d.delete() 
    return redirect("cart") 

def product_detail(request,id):
    f=Products.objects.get(id=id)
    g=f.images.all()
    return render(request,"productdetails.html",{"products":f ,"moreimg":g})    

     
def search_item(request):
    if request.method=="POST":
        item_search=request.POST.get("item_search")
        if request.user.is_authenticated: 
            task=Cart.objects.filter(user=request.user)
            v=task.count
            items=Products.objects.filter( Q(title__icontains=item_search) or Q(content__icontains=item_search) )
            return render(request,"search_item.html",{"products":items,"len_cart":v})   
        else: 
            items=Products.objects.filter(Q(title__icontains=item_search) or Q(content__icontains=item_search))
            return render(request,"search_item.html",{"products":items}) 
    return render(request,"home.html")  
 

def add_search_data(request):
    f=Products.objects.get(id=id)
    title=f.title
    content=f.content 
    cost=f.cost
    k=Cart(user=request.user,title=title,content=content,cost=cost)  
    k.save() 
    return render(request,"search_item.html")   
 
def logout_page(request):  
    logout(request)
    return redirect("len_ct")




 
    
              
 
                

 
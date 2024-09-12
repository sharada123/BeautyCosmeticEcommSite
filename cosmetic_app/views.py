from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Product,Cart,Order
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
import random
import razorpay
from django.core.mail import send_mail
# Create your views here.
def home(request):
    #print(request.user.is_authenticated)
    p=Product.objects.filter(is_active=True)
    context={}
    context['products']=p

    return render(request,'index.html',context)

def product_details(request,pid):
    p=Product.objects.filter(id=pid)
    context={}
    context['products']=p
    return render(request,'product_details.html',context)

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        # print(uname,"-",upass,"-",ucpass)
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Fields cannot be empty"
        elif upass!=ucpass:
            context['errmsg']="Password and confirm password didn't matched"
        else:
            try:
                u=User.objects.create(username=uname,password=upass,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="User Created Successfully"
            except Exception:
                context['errmsg']="User with same name already Exist!!"
        return render(request,'register.html',context)
    else:
        return render(request,'register.html')


def user_login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Fields cannot be  empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            print(u)
            if u is not None:
                login(request,u)
                return redirect("/")
            else:
                context['errmsg']="Invalid Username and Password"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("/")

def catfilter(request,cv):
    q1=Q(is_active=True)
    q2=Q(cat=cv)
    p=Product.objects.filter(q1 & q2)
    context={}
    context['products']=p
    return render(request,'index.html', context)

def sort(request,sv):
    if sv=='0':
        col='price'
    else:
        col='-price'
    p=Product.objects.filter(is_active=True).order_by(col)
    context={}
    context['products']=p
    return render(request,'index.html',context)

def range(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(price__lte=max)
    q2=Q(price__gte=min)
    q3=Q(is_active=True)
    p=Product.objects.filter(q1 & q2 & q3)
    context={}
    context['products']=p
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def search(request):
    search = request.GET.get('search', '')
    context = {}
    try:
        if search:
            q1 = Q(name__icontains=search)
            q2 = Q(pdetails__icontains=search)
            p = Product.objects.filter(q1 | q2)
            if p.exists():
                context['success'] = "Search Result Done!!!"
            else:
                context['errmsg'] = "Product not found!!!"
        else:
            context['errmsg'] = "Product not found!!!"
            p = Product.objects.none()  # Empty queryset to avoid errors

        context['products'] = p
        context['search'] = search

    except Exception as e:
        context['errmsg'] = "An error occurred: {}".format(e)

    return render(request, 'searchproduct.html', context)

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id 
        u=User.objects.filter(id=userid)
        p=Product.objects.filter(id=pid)
        #check product exits or not
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])
        c=Cart.objects.filter(q1 & q2)
        n=len(c)
        context={}
        context['products']=p
        if n==1:
            context['errmsg']="Product already exist!!!"
        else:
            c=Cart.objects.create(uid=u[0],pid=p[0])
            c.save()
            context['success']="Product added successfully to cart!!"
            
        return render(request,'product_details.html',context)
    else:
        return redirect("/login")

def cart(request):
    #u=request.user.id   # id of logged in user 
    context={}
    if request.user.is_authenticated:
        c=Cart.objects.filter(uid=request.user.id) # retrives details of logged in user
        if c:
            s=0
            np=len(c)
            for x in c:       #loop for calculate total price of all products of that logged in user
                s+=x.pid.price
            print(s)
            context['total']=s
            context['data']=c
            context['n']=np
        else:
            context['msg']="Empty cart!! Add Products to Cart."
        return render(request,'cart.html',context)
    else:
        return redirect('/login')

def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect("/viewcart")

def updateqty(request,qv,cid):
    c =Cart.objects.filter(id=cid)
    #print(c)
    print(c[0].qty)
    if qv == '1':
        t=c[0].qty+1
        c.update(qty=t)
        # print(t)
    else:
        if c[0].qty > 1:
            t=c[0].qty-1
            c.update(qty=t)
    return redirect('/viewcart')

def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)
    #print(oid)
    for x in c:
        o=Order.objects.create(order_id=oid, uid=x.uid,pid=x.pid,qty=x.qty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=userid)
    #print(orders)
    context={}
    context['data']=orders
    s=0
    np=len(orders)
    for x in orders:
        s=s+x.pid.price*x.qty
    context['total']=s
    context['n']=np
    return render(request,'placeorder.html',context)

def removeorder(request,oid):
    o=Order.objects.filter(id=oid)
    #print(o)
    o.delete()
    return redirect('/placeorder')

def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    context={}
    np=len(orders)
    for x in orders:
        s=s+ x.pid.price*x.qty
        oid=x.order_id
    client = razorpay.Client(auth=("rzp_test_pjmfONoAV5hhRJ", "2qLFlWxOv0vaA1jxWEEHwbcA"))
    data = { "amount": s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    # print(payment)
    uemail=request.user.email
    context['uid']=request.user.id
  
    context['data']=payment
    context['uemail']=uemail
    return render(request,'pay.html',context)
    

def sendusermail(request,uemail,uid):
    o=Order.objects.filter(uid=uid)
    msg=""
    print(o[0].pid.name)
    for x in o:
        # msg+=f"Your order is placed for {x.pid.name} and price for that product is {x.pid.price}"
        # print(msg)
        msg += f"""
        Thanks for visiting Estore...
        Product Name : {x.pid.name} and 
        Product Price : {x.pid.price}
        
        """
    send_mail(
        "Ekart order placed successfully!!",
        msg,
        "sharadagadadhe111@gmail.com",
        [uemail],
        fail_silently=False,
    )
    return HttpResponse("Mail sent successfully")
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import product1,sales
from home import utils
import numpy as np

# Create your views here.
def index(request):
    if(request.user.is_authenticated) and request.user.role =="MANAGER" : return HttpResponse("success")
    return redirect("/login")

def loginuser(request):
    if request.method=="POST" : 
        un=request.POST.get('username')
        pw=request.POST.get('pass')
        print(un,pw)
        user = authenticate(username=un,password=pw)
        print(user)
        if user is not None :
            login(request,user)
            return redirect("/check")
    return render(request,'login.html')


def logoutuser(request):
    if request.user.is_authenticated :
        logout(request)
        return render(request,"logout.html")
    return redirect("/login")
    

def safe1(request) : 
     if request.user.is_authenticated and request.user.role=="MANAGER":
        return redirect("/gp2")
     elif request.user.is_authenticated and request.user.role=="CUSTOMER":
        return redirect("/product1")
        
     return redirect("/login")


def safe2(request) : 
    if request.user.is_authenticated and request.user.role=="MANAGER":
        return redirect("/gp")
    elif request.user.is_authenticated and request.user.role=="CUSTOMER":
        return redirect("/product2")
    return redirect("/login")
       
     
def check(request) : 
    if request.user.is_authenticated :
        return render(request,'check.html')
    return redirect("/login")


def pc2(request):
    if request.user.is_authenticated and request.user.role=="CUSTOMER":
        cc = {
            "pname":"Mango Juice"
        }
        if request.method=="POST":
              username=request.user.username

              for i in product1.objects.all() :
                  if(i.username==username and i.pname=="Mango") : return redirect("/check")
              taste=int(request.POST.get('taste'))
              freshness=int(request.POST.get('freshness'))
              h_cnt=int(request.POST.get('h_cnt'))
              flv=int(request.POST.get('flv'))
              delivery=int(request.POST.get('delivery'))
              pname="Mango"
              contact=product1(username=username,taste=taste,freshness=freshness,h_cnt=h_cnt,flv=flv,delivery=delivery,pname=pname)
              contact.save()
        return render(request, 'product1.html',cc)
    return redirect("/login")


def pc1(request):
    if request.user.is_authenticated and request.user.role=="CUSTOMER":
        cc = {
            "pname":"Orange Juice"
        }
        if request.method=="POST":
              username=request.user.username

              for i in product1.objects.all() :
                  if(i.username==username and i.pname=="Orange") : return redirect("/check")
              taste=int(request.POST.get('taste'))
              freshness=int(request.POST.get('freshness'))
              h_cnt=int(request.POST.get('h_cnt'))
              flv=int(request.POST.get('flv'))
              delivery=int(request.POST.get('delivery'))
              pname="Orange"
              contact=product1(username=username,taste=taste,freshness=freshness,h_cnt=h_cnt,flv=flv,delivery=delivery,pname=pname)
              contact.save()
        return render(request, 'product1.html',cc)
    return redirect("/login")


def graph(request):
    if request.user.is_authenticated and request.user.role=="MANAGER":
        # Bar Graph
        x = [1,2,3,4,5]
        t = [ i.taste  for i in product1.objects.all() if i.pname=="Mango"]
        t = np.mean(t)
        f = [ i.freshness for i in product1.objects.all() if i.pname=="Mango"]
        f = np.mean(f)
        h = [ i.h_cnt for i in product1.objects.all() if i.pname=="Mango"]
        h = np.mean(h)
        tex = [ i.flv for i in product1.objects.all() if i.pname=="Mango"]
        tex = np.mean(tex)
        d = [ i.delivery for i in product1.objects.all() if i.pname=="Mango"]
        d = np.mean(d)
        y = [t,f,h,tex,d]
        name = ['taste','freshness','health count','flavour and texture','delivery']
        chart = utils.get_plot(x,y,name,1)

        # Line Chart 
        x2 = [1,2,3,4,5,6,7,8,9,10,11,12]
        mo = ['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
        y2 = []
        for i in mo: 
            temp = [j.total_sal for j in sales.objects.all() if (j.month == i and j.pname2 == "Mango")]
            temp = np.sum(temp)
            y2.append(temp)
        c2 = utils.get_plot(x2,y2,mo,2)

        # pie chart 
        x3=[1,2]
        lab = ['Orange','Mango']
        y3 = []
        for i in lab: 
            temp = [j.total_sal for j in sales.objects.all() if j.pname2 == i]
            temp = np.sum(temp)
            y3.append(temp)
        c3 = utils.get_plot(x3,y3,lab,3)


        return render(request, 'gp.html', {'chart' : chart,'abc' : c2, 'pie' : c3})
    
def graph2(request):
    if request.user.is_authenticated and request.user.role=="MANAGER":
        # Bar Graph
        x = [1,2,3,4,5]
        t = [ i.taste  for i in product1.objects.all() if i.pname=="Orange"]
        t = np.mean(t)
        f = [ i.freshness for i in product1.objects.all() if i.pname=="Orange"]
        f = np.mean(f)
        h = [ i.h_cnt for i in product1.objects.all() if i.pname=="Orange"]
        h = np.mean(h)
        tex = [ i.flv for i in product1.objects.all() if i.pname=="Orange"]
        tex = np.mean(tex)
        d = [ i.delivery for i in product1.objects.all() if i.pname=="Orange"]
        d = np.mean(d)
        y = [t,f,h,tex,d]
        name = ['taste','freshness','health count','flavour and texture','delivery']
        chart = utils.get_plot(x,y,name,1)

        # Line Chart 
        x2 = [1,2,3,4,5,6,7,8,9,10,11,12]
        mo = ['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
        y2 = []
        for i in mo: 
            temp = [j.total_sal for j in sales.objects.all() if (j.month == i and j.pname2 == "Orange")]
            temp = np.sum(temp)
            y2.append(temp)
        c2 = utils.get_plot(x2,y2,mo,2)

        # pie chart 
        x3=[1,2]
        lab = ['Orange','Mango']
        y3 = []
        for i in lab: 
            temp = [j.total_sal for j in sales.objects.all() if j.pname2 == i]
            temp = np.sum(temp)
            y3.append(temp)
        c3 = utils.get_plot(x3,y3,lab,3)


        return render(request, 'gp.html', {'chart' : chart,'abc' : c2, 'pie' : c3})
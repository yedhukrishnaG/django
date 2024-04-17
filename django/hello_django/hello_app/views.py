from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore
from django.db.models import Sum # type: ignore
# Create your views here.
from django.shortcuts import render,redirect  # type: ignore
from .models import Basicinfo,Dashboard,Login

def print_hello(request):
    return HttpResponse("hello world")


def print_hello_world(request):
    if(request.POST):
         print(request.POST.get('f_name'))
         print(request.POST.get('l_name'))
         f_name = request.POST.get('f_name')
         l_name = request.POST.get('l_name')
         info = Basicinfo(f_name= f_name,l_name=l_name)
         info.save()
    return render(request,'hello.html')



def create(request):
    if(request.POST):
         print(request.POST.get('f_name'))
         print(request.POST.get('l_name'))
         f_name = request.POST.get('f_name')
         l_name = request.POST.get('l_name')
         info = Basicinfo(f_name= f_name,l_name=l_name)
         info.save()
    return render(request,'create.html')


def edit(request,pk):
    if(request.POST):
        instance= Basicinfo.objects.get(pk=pk)
        instance.f_name = request.POST.get('f_name')
        instance.l_name = request.POST.get('l_name')
        #instance = Basicinfo(f_name= instance.f_name,l_name=instance.l_name)
        instance.save()
        data_set = Basicinfo.objects.all()
        return render(request,'list.html',{'data':data_set})
        # return render(request,'list.html')
    else:
        instance= Basicinfo.objects.get(pk=pk)
        return render(request,'create.html',{'data':instance})
    
def editnew(request,pk):
    if(request.POST):
        instance = Basicinfo.objects.get(pk=pk)
        instance.f_name = request.POST.get('f_name', request.POST.get('f_name_original'))
        instance.l_name = request.POST.get('l_name', request.POST.get('l_name_original'))
        instance.gender = request.POST.get('gender', request.POST.get('gender_original'))
        if(instance.gender == "M"):
            instance.value = True
        else:
            instance.value = False  
        instance.save()
        data_set = Basicinfo.objects.all()
        # return render(request, 'list.html', {'all_data': data_set})
        # return render(request,'list.html')
        return redirect('list') 
    else:
        instance= Basicinfo.objects.get(pk=pk)
        all_data= Basicinfo.objects.all()
        return render(request,'list.html',{'data':instance,'id_value':instance.id,'all_data':all_data,'selected':True})    

def delete(request,pk):
    instance= Basicinfo.objects.get(pk=pk)
    instance.delete()
    data_set = Basicinfo.objects.all()
    return redirect('list') 
    # return render(request,'list.html',{'all_data':data_set})

def list(request):
    data_set = Basicinfo.objects.all()
   
    return render(request,'list.html',{'all_data':data_set})

def menu(request):
    return render(request,'menu.html')

def old_view(request):
    return render(request,'nonbt.html')

def report(request):
    data_set = Dashboard.objects.all()
    total_stock_level = data_set.aggregate(total_stock_level=Sum('stock_level'))['total_stock_level']

    return render(request,'report.html',{'data_set':data_set,'total_stock_level':total_stock_level})

def homepage(request):
    row_count = Dashboard.objects.count()
    total_stock_level = Dashboard.objects.all().aggregate(total_stock_level=Sum('stock_level'))['total_stock_level']

    return render(request,'homepage.html',{'row_count':row_count,'total_stock_level':total_stock_level})

def dashboard(request):

    return render(request,'dashboard.html',)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Query the Login table to find the user
        try:
            user = Login.objects.get(username=username)
            # Check if the password matches
            if user.password == password:
                # Password matches, proceed with login
                # You may want to set session variables or use Django's authentication system here
                return redirect('homepage')  # Redirect to home page after successful login
            else:
                # Password does not match
                return render(request, 'login.html', {'error_message': 'Invalid password'})
        except Login.DoesNotExist:
            # User not found in the Login table
            return render(request, 'login.html', {'error_message': 'Invalid username'})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Query the Login table to find the user
        info = Login(username=username ,password=password)
        info.save()
    return render(request, 'signup.html')  

def addrow(request):
    if(request.POST):
         
         
         article_number = request.POST.get('article_number')
         article_title = request.POST.get('article_title')
         stock_level = request.POST.get('stock_level')
         earliest_expiration_date = request.POST.get('earliest_expiration_date')
         batch_amount = request.POST.get('batch_amount')
         reorder_level = request.POST.get('reorder_level')
         maximum_level = request.POST.get('maximum_level')
        
         info = Dashboard(article_number= article_number,article_title=article_title,stock_level= stock_level,earliest_expiration_date=earliest_expiration_date,batch_amount= batch_amount,reorder_level=reorder_level,maximum_level= maximum_level,)
         info.save()
    return render(request,'addrow.html')



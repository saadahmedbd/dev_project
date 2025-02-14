from pyexpat.errors import messages
from django.shortcuts import render, redirect



from . forms import CreateUserForm, LoginForm, createRecordForms,updateRecordForms

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record

# Create your views here.
#home page
def home (request):
   # return HttpResponse("hello this is my web project")
   return render (request,'webapp/index.html')

#register a user
def register(request):
   form =CreateUserForm()

   if request.method == "POST":
      form =CreateUserForm(request.POST)

      if form.is_valid():
         form.save()

         return redirect('login')
   context ={"form": form}
   return render (request, 'webapp/register.html', context=context)

# login form 

def login(request):

   form =LoginForm()

   if request.method == "POST":
      form = LoginForm (request, data=request.POST)

      if form.is_valid():
         username =request.POST.get("username")
         password =request.POST.get("password")

         user = authenticate(request, username=username, password=password)

         if user is not None:
            auth.login(request, user)

            return redirect('dashboard')

   context = {'form':form}
   return render (request, 'webapp/login.html', context=context)         

# - DashBoard

@login_required(login_url ='login')
def dashboard(request):

   my_records = Record.objects.all()
   context ={'records':my_records}
   return render(request, 'webapp/dashboard.html', context=context)


# - create user record

@login_required (login_url='login')
def createUserRecord(request):

   form =createRecordForms()

   if request.method == "POST":

      form =createRecordForms(request.POST)

      if form.is_valid():

         form.save()

        
         return redirect("dashboard")
      
   context = {'form':form}
   return render (request, "webapp/create_record.html", context=context)
   

# -update user record

@login_required(login_url='login')
def updateUserRecord(request, pk):  #pk=primary key
   record=Record.objects.get(id=pk)

   form=updateRecordForms(instance=record)

   if request.method =="POST":
      form =updateRecordForms(request.POST, instance=record)

      if form.is_valid():
         form.save()

         return redirect('dashboard')
   context ={'form':form}
   return render(request, 'webapp/update_record.html', context=context)
       
   

# - view / view a singular record

def singularRecord(request, pk):
   
   all_record = Record.objects.get(id=pk)

   context = {'record':all_record}

   return render(request, 'webapp/view_record.html', context=context)


# - delete a record

@login_required(login_url="login")
def deleteRecord(request, pk):

   record= Record.objects.get(id=pk)

   record.delete()

   return redirect("dashboard")




# user logout

def logout(request):

   auth.logout(request)

   return redirect('login')
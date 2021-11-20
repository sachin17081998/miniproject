from django.shortcuts import render
from gallary.forms import *
from gallary.models import *
from django.contrib.auth.models import User


#login includes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required#decorator whic we can use in any view that requires login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages 

searchtext=""
status= image.objects.all()

def index(request,pk):
    
    ob=get_object_or_404(User,pk=pk)
    customer={'pk':pk,'name':ob.username,'email':ob.email,'address':ob.user_data.address,'contact':ob.user_data.contact}
    img=image.objects.all().order_by('?')
    allusers=User.objects.all()
  
    nature=image.objects.filter(category__icontains='nature')
    fashion=image.objects.filter(category__icontains='fashion')
    cars=image.objects.filter(category__icontains='car')
    bikes=image.objects.filter(category__icontains='bike')
    marriage=image.objects.filter(category__icontains='marriage')
    events=image.objects.filter(category__icontains='event')
    food=image.objects.filter(category__icontains='food')
    animals=image.objects.filter(category__icontains='animals')
    return render(request,'index.html',{'user':customer,'images':img,'alluser':allusers,'nature':nature,
                                        'fashion':fashion,'animals':animals,'cars':cars,'bikes':bikes,'marriage':marriage,
                                        'events':events,'food':food,'img':status,'searchtext':searchtext})
# Create your views here.


def login(request):
    registered=False
   
    if request.method=="POST":
        
        user_info=userform(data=request.POST)
        user_profile_form=profile_form(data=request.POST)
        if user_profile_form.is_valid() and user_info.is_valid():
            user=user_info.save()
            user.set_password(user.password)
            user.save()
            profile=user_profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print(user_profile_form.errors,user_info.errors)
    else:
        user_info=userform()
        user_profile_form=profile_form()            
    
    return render(request,'login.html',{'user_form':user_info,'profile_form':user_profile_form,'registered':registered})         


# #login view
def user_login(request):
    if request.method=='POST':
     
        #print(p)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                #p=user_profile.objects.get(user.pk)
                #print(p)
                # user_id=user.pk
                # u=user_profile.objects.get(user.id)
                # print(u)
                print("success")
                return redirect('index',pk=user.pk)
                
            else:
                return HttpResponse('Account is not Active')
        else:
            error="*invalid username or password"
            return render(request,'LoginView_form.html',{'error':error}) #HttpResponse("Invalid Username or Password")    
    else:
        return render(request,'LoginView_form.html')  

#user profile
def user_profile(request,pk):
    ob=get_object_or_404(User,pk=pk)
    customer={'pk':pk,'name':ob.username,'email':ob.email,'address':ob.user_data.address,'contact':ob.user_data.contact}
    images=image.objects.all().filter(username=ob.username)
    # print(images)
    # for i in images:
    #     print(i.img)
    return render(request,'user.html',{'user':customer,'image':images})


# image uplpad.
def image_view(request):

	if request.method == 'POST':
		form = imgForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = imgForm()
	return render(request, 'upload_img.html', {'form':form})


def success(request):
	return HttpResponse('successfully uploaded')


def success2(request):
	return redirect(contactView)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout'))






def contactView(request,pk):
    ob=get_object_or_404(User,pk=pk)
    if request.method == 'GET':
        form = ContactForm()
        form.fields["to"].initial = ob.email
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to=form.cleaned_data['to']
            try:
                send_mail(subject, message,settings.EMAIL_HOST_USER, [to])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponse(alert('mail sent'));
            return redirect ('mailsent')
        
    return render(request, "email.html", {'form': form,'to':ob})

def mailsent(request):
    
    messages.success(request, "Message sent." )
    # return HttpResponse('Success! Thank you for your message.')
    return redirect('contactView')

def search(request):
    if request.method == 'GET': # this will be GET now      
        cate =  request.GET.get('search') # do some research what it does       
        
        global status 
        status= image.objects.filter(category__icontains=cate)
        # print(len(status)) 
        i=0
        if len(status)==0:
            while i<len(cate)/2:
                status= image.objects.filter(category__icontains=cate[:len(cate)-i])
                i+=1
                if len(status)>0:
                    break
        
        if len(status)==0:
            global searchtext
            searchtext="Sorry, but It looks like we don have the searched image.Try using some similary keywords..."        
                
            
            # return render(request)
            
        return redirect(request.META['HTTP_REFERER'])
   
# def addto_cart(request,prod,cust,cat):
#     cartob=cart()
#     if cat=='female':
#         prodob=get_object_or_404(women,productId=prod)
#     elif cat=='male':
#         prodob=get_object_or_404(men,productId=prod)
#     elif cat=='kids':
#         prodob=get_object_or_404(kids,productId=prod)    
        
#     # userob=get_object_or_404(women,Username=prod)
#     cartob.productId=prod
#     cartob.productName=prodob.productName
#     cartob.customerId=cust
#     cartob.cost=prodob.price
#     cartob.image=prodob.image
#     cartob.save()
    
#     msg="<br><br><br><center><h1>Item Successfully Added</h1></center>"
#     return HttpResponse(msg)

# def show_cart2(request,cust):
#     # p={'ob':pk}
#     # return redirect('cart.html',prod=prod)
#     customer=get_object_or_404(User,username=cust)
#     print("iddddd="+str(customer.id))
#     prodob=cart.objects.all().filter(customerId=cust)
#     print(prodob)
#     return render(request, 'cart.html',
#                   {'customer':cust,"orders":prodob,'custid':customer.id})    
    

# def delete_product(request,pk,cust):
#     query = cart.objects.get(id=pk)
#     query.delete()
#     return show_cart2(request,cust)

# def place_order(request,cust):
#     cart.objects.filter(customerId=cust).delete()
    
#     return show_cart2(request,cust)

def return_home(request,pk):
    return index(request,pk)
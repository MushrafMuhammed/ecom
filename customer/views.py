from django.shortcuts import render, redirect

from customer.models import Customer


def cus_loginfun(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['user_password']
        try:
            customer = Customer.objects.get(
                email=username, 
                password=password
            )
            request.session['customer_sessionId'] = customer.id
            return redirect('customer:master')
        except:
            msg = 'invalid password or username'

    return render(request, 'customer_temp/login.html', { 'error_message' : msg })


def cus_signupfun(request):
    if request.method == 'POST':
        name = request.POST['c_name']
        email = request.POST['c_email']
        address = request.POST['c_address']
        phone = request.POST['c_mobile']
        password = request.POST['c_password']
        
        newCustomer = Customer(
            name=name,
            email=email,
            address=address,
            phone=phone,
            password=password,
        )
        newCustomer.save()

    return render(request, 'customer_temp/signup.html')


def cus_masterfun(request):
    return render(request, 'customer_temp/master.html')


def cus_productsfun(request):
    return render(request, 'customer_temp/products.html')


def cus_orderfun(request):
    return render(request, 'customer_temp/order.html')


def cus_changepasswordfun(request):
    return render(request, 'customer_temp/chgpassword.html')


def cus_profilefun(request):
    if 'customer_sessionId' in request.session:
        currentuser = Customer.objects.get(
            id=request.session['customer_sessionId']
        )
        return render(request, 'customer_temp/profile.html', {'user_details': currentuser})
    else:
        return redirect('customer:login')


def cus_supportfun(request):
    return render(request, 'customer_temp/support.html')


def cus_logoutfun(request):
    del request.session['customer_sessionId']
    return redirect('customer:login')
    # return render(request, 'customer_temp/login.html')


# Create your views here.

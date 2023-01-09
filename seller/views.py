import random
from django.shortcuts import render,redirect

from seller.models import Seller,Product
from django.core.mail import send_mail
from django.conf import settings

def sel_loginfun(request) :
    msg = ''
    if request.method == 'POST' :
        seller_username = request.POST['s_username']
        seller_password = request.POST['s_password']

        try :
            seller = Seller.objects.get(
                 username = seller_username,
                 password = seller_password
            )
            request.session['seller_sessionID'] = seller.id
            return redirect('seller:sel_loghome')
        except :
            msg = 'invalid username or password !'

    return render(request, 'seller_temp/login.html', {'errorMessage' : msg })

def sel_signupfun(request) :
    if request.method == 'POST' :
        seller_name = request.POST['s_name']
        seller_email = request.POST['s_email']
        seller_phone = request.POST['s_phone']
        seller_address = request.POST['s_address']
        seller_holderName = request.POST['s_holder']
        seller_ifscCode = request.POST['s_ifsc']
        seller_bankBranch = request.POST['s_branch']
        seller_accountNumber = request.POST['s_acnumber']
        seller_photo = request.FILES['s_photo']
        seller_username = random.randint(1111,9999)
        seller_password = 'sel-' + seller_name.lower() + str (seller_username)
        message = 'Hai Your username is ' + str(seller_username) + 'and temporary password is ' + seller_password
        
        newseller = Seller(   
            name = seller_name,
            email = seller_email,
            phone = seller_phone,
            address = seller_address,
            holder_name = seller_holderName,
            ifc_code = seller_ifscCode,
            bank_branch = seller_bankBranch,
            account_number = seller_accountNumber,
            photo = seller_photo,
            username = seller_username,
            password = seller_password,  
        )
        send_mail(
            'username and temporary pawword ',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email],
            fail_silently = False
        )
        newseller.save()
    return render(request, 'seller_temp/signup.html')

def sel_masterfun(request) :
    return render(request, 'seller_temp/master.html')

def sel_homefun(request) :
    return render(request, 'seller_temp/seller_home.html')

def sel_loghome(request) :
    return render(request, 'seller_temp/sel_loghome.html')

def sel_addproduct(request) :
    if request.method =="POST" :
        pro_category = request.POST['category']
        pro_name = request.POST['name']
        pro_number = request.POST['pro_no']
        pro_description = request.POST['description']
        pro_price = request.POST['price']
        pro_currentStock = request.POST['currentStock']
        pro_image = request.FILES['img']

        newProduct = Product(
            Category = pro_category,
            P_Name = pro_name,
            P_No = pro_number,
            P_Description = pro_description,
            P_Price = pro_price,
            P_CurrentStock = pro_currentStock,
            p_photo =pro_image
        )
        newProduct.save()
    return render(request, 'seller_temp/addProduct.html')

def sel_profile(request) :
    if "seller_sessionID" in request.session :
        current_seller = Seller.objects.get(
            id = request.session['seller_sessionID']
        )
        return render(request, 'seller_temp/profile.html', {'seller_details': current_seller})
    else:
        return redirect('seller:login')
    # return render(request, 'seller_temp/profile.html')

def sel_myproducts(request) :
    seller_product = Product.objects.filter(
        id = request.session["seller_sessionID"]
    )

    return render(request, 'seller_temp/myProducts.html', { 'productList' : seller_product })




    # if 'seseller_sessionID' in request.session :
    #     current_products = Product.objects.filter(
    #         id = request.session['seller_sessionID']
    #     )
    #     return render(request, 'seller_temp/myProduct.html', {'product_list': current_products})
    # else:
    #     msg = "Please login your Account"
    

def sel_changePassword(request) :
    return render(request, 'seller_temp/changePassword.html')

def sel_editProfile(request) :
    return render(request, 'seller_temp/editProfile.html')

def sel_logout (request) :
    del request.session['seller_sessionID']
    return redirect('common:common')

    

# Create your views here.

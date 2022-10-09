from django.shortcuts import render

# Create your views here.
def shop_home(request):
    return render(request,'shop/home.html')

def shop_contact(request):
    return render(request,'shop/contact.html')

    
def shop_about(request):
    return render(request,'shop/about.html')


def shop_buy(request):
    return render(request,'shop/buy.html')

    
def shop_allproduct(request):
    return render(request,'shop/allproduct.html')

       
def shop_offer(request):
    return render(request,'shop/offer.html')





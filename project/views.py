from django.shortcuts import render,redirect
from .models import Sign,Submit
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.

def first(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        print("username",username)
        print("email",email)
        print("password",password)
        if Sign.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
        else:
            Sign.objects.create_user(username=username,email=email,password=password)
            messages.error(request,'SignUp Successfull')
            return redirect('second')
    return render(request,'first.html')


def second(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login Success')
            return redirect('third')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request,'second.html')


def third(request):
    return render(request,'third.html')


def fourth(request):
    if request.method == "POST":
        patient_name=request.POST.get("patient_name")
        address=request.POST.get("address")
        gender=request.POST.get("gender")
        place=request.POST.get("place")
        disease=request.POST.get("disease")
        print("patient_name",patient_name)
        print("address",address)
        print("gender",gender)
        print("place",place)
        print("disease",disease)
        if Submit.objects.filter(patient_name=patient_name).exists():
            messages.error(request,'Patient Name already exist')
        else:
            Submit.objects.create(patient_name=patient_name,address=address,gender=gender,place=place,disease=disease)
            messages.success(request,'Submit Successfull')
            return redirect('fifth')
    return render(request,'fourth.html')


def fifth(request):
    return render(request,'fifth.html')


def sixth(request):
    return render(request,'sixth.html')


def seventh(request):
    return render(request,'seventh.html')


def eight(request):
    return render(request,'eight.html')


def nineth(request):
    return render(request,'nineth.html')


def tenth(request):
    return render(request,'tenth.html')


def eleventh(request):
    return render(request,'eleventh.html')


def twovelth(request):
    return render(request,'twovelth.html')


def thirteenth(request):
    return render(request,'thirteenth.html')


def fourteenth(request):
    return render(request,'fourteenth.html')


def fifteenth(request):
    return render(request,'fifteenth.html')


def sixteenth(request):
    return render(request,'sixteenth.html')


def seventeenth(request):
    return render(request,'seventeenth.html')


def eighteenth(request):
    return render(request,'eighteenth.html')


def nineteenth(request):
    return render(request,'nineteenth.html')


def twentieth(request):
    return render(request,'twentieth.html')


def twentifirst(request):
    return render(request,'twentifirst.html')


def payment(request):

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID,
              settings.RAZORPAY_KEY_SECRET)
    )

    payment_data = {
        "amount": 50000,   # Amount in paise = 500 INR
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    order = client.order.create(data=payment_data)

    context = {
        'order_id': order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': payment_data['amount'],
        'currency': payment_data['currency'],
    }

    return render(request, 'payment.html', context)


@csrf_exempt
def success(request):

    if request.method == "POST":

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID,
                  settings.RAZORPAY_KEY_SECRET)
        )

        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            return render(request, 'success.html')

        except:
            return HttpResponseBadRequest()
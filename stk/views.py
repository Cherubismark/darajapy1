from django.shortcuts import render, redirect
import requests
from .credentials import MpesaAccessToken, MpesaPassword

# Create your views here.

def home(request):
    return render(request, 'index.html')

def stk_push(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')

        access_token = MpesaAccessToken.validated_token

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        headers = {"Authorization": "Bearer %s" % access_token}

        request = {
            "BusinessShortCode" : MpesaPassword.shortcode,
            "Password" : MpesaPassword.decoded_password ,
            "Timestamp" : MpesaPassword.timestamp,
            "TransactionTYpe" : "CustomerPaybillOnline",
            "Amount" : amount,
            "PartyA" : phone,
            "PartyB": MpesaPassword.shortcode,
            "PhoneNumber" : phone,
            "CallBackURL" : "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountREfference" : "Linc Softwares",
            "TransactionDesc" : "Linc Softwares Payment"

        }
        response = request.post(api_url, jsoon=request, headers=headers)

        return redirect ('thanks')

def thank_you(request):
            return render (request, 'thank_you.html')

 

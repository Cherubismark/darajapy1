import json
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

class Credentials:
    consumer_key = "U050WjVmgqsiED5o1hnVEcOsJT7MDAIM7ofRxSUFIQuHzlYL"
    consumer_secret = "NNA9yDszHn8gsx878DYBY509xgSuI9saH0cqhC19XvEknnQitUEfmUj7W5TE1bT4"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

class MpesaAccessToken:
        token = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
        access_token = json.loads(token.text)
        validated_token = access_token['access_token']


class MpesaPassword:
        timestamp = datetime.now().strftime('%y%m%d%H%M%S')
        shortcode = "174379"
        passkey = Credentials.passkey


        encode_str = timestamp + shortcode + passkey

        encoded = base64.b64encode(encode_str.encode())

        decoded_password = encoded.decode('utf-8')




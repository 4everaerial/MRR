import time
import requests
import hmac_sha1

def rent_rig(rent_id, price):
        api_base = "https://www.miningrigrentals.com/api/v2/"
        endpoint = "/rental"
        api_key = '<api key>'
        api_secret = '<api secret>'

        nonce = str(int(time.time()) * 1000)

        #String to sign is api_key + nonce + endpoint
        sign_string = api_key + nonce + endpoint

        #Sign the string using a sha1 hmac
        digest = hmac_sha1.make_digest(sign_string, api_secret)

        headers = {'x-api-nonce': nonce, 'x-api-key': api_key, 'x-api-sign': digest}
        params = {'rig': int(rent_id), 'length': float(3), 'profile': 111671, 'currency': 'ETH', 'rate.price': float(price)}

        request_url = api_base + endpoint
        r = requests.put(request_url, headers=headers, params=params).json()
        print(r)

def get_balance():
        api_base = "https://www.miningrigrentals.com/api/v2/"
        endpoint = "/account/balance"
        api_key = '<api key>'
        api_secret = '<api secret>'

        nonce = str(int(time.time()) * 1000)

        # String to sign is api_key + nonce + endpoint
        sign_string = api_key + nonce + endpoint

        # Sign the string using a sha1 hmac
        digest = hmac_sha1.make_digest(sign_string, api_secret)

        headers = {'x-api-nonce': nonce, 'x-api-key': api_key, 'x-api-sign': digest}
        request_url = api_base + endpoint
        r = requests.get(request_url, headers=headers).json()
        print(r)


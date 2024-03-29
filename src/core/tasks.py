from django.core.mail import send_mail
from kavenegar import *
import random
import redis
from celery import shared_task
from config.secrets import API_KEY



@shared_task
def send_opt_sms(phone: str, expiry_time: int):
    code = random.randint(100000, 999999)
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.setex(phone, expiry_time, str(code))
    try:
        api = KavenegarAPI(API_KEY)
        params = {
        'receptor': phone,
        'template': 'verify',
        'token': code,
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


@shared_task
def send_opt_email(email: str, expiry_time: int):
    code = random.randint(100000, 999999)
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.setex(email, expiry_time, str(code))
    send_mail("Email Verification", f"hi. Your verification code is {code}",
              'smrazavi19911370@gmail.com', (email,))

import time
import jwt

SECRET_KEY = ('fncjncjerncwiucwnc=====340-2023')
ALG0 = 'HS256'
ACCESS_TOKEN_EXPIRE = 5
REFRESH_TOKEN_EXPIRE = 30

def encodeJWT(data):
    payload_access = {
        "data":data,
        "expiry": time.time() + ACCESS_TOKEN_EXPIRE    
    }
    payload_refresh = {
        "data":data,
        "expiry": time.time() + REFRESH_TOKEN_EXPIRE
    }
    access_token = jwt.encode(payload_access, SECRET_KEY, algorithm = ALGO)
    refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algorithm=ALGO)
    return {"access":access, "refresh":refresh_token}

def decodeJWT(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithm=ALGO)
        if decoded['expiry'] >= time.time():
            # если еще не истек срок
            return decoded 
        return {}
    except:
        return {}


def refreshJWT(refresh):
    decoded = decodeJWT(refresh)
    if decoded:
        return encodeJWT(decoded['data'])
    return {}
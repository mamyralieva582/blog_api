import time 
from jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email":"dnjc@gmail.com", "username":"katana", "id":1}

# получаем токины
jwt_token = encodeJWT(user) # {'access_token': cerfhbcwhwe, 'refresh_token': frejvnrjhbgt}

# проходит время
time.sleep(6)

# прилитает декодированный токен, если время не истекло, если время жизни истекло, прилетает пустой dict
decoded = decodeJWT(jwt_token['access_token'])

# оьновляем старые токены на новые
new_jwt_token = refreshJWT(jwt_token['refresh_token'])
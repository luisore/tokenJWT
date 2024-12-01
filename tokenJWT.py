import jwt
import datetime


CLAVE_SECRETA = "patata"

datos = {"username": "luis",
         "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
         }

token = jwt.encode(datos, CLAVE_SECRETA,algorithm='HS256')

print(token)
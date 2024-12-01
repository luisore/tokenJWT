

import jwt

CLAVE_SECRETA = "patata"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imx1aXMiLCJleHAiOjE3MzMwNjg0NjV9.VKoCQsmGWIw-6Ah71NY8sBVc8PmsKwYYI9_yzrWEqnk"

try:
    decoded_token = jwt.decode(token,
    CLAVE_SECRETA, algorithms=["HS256"])
    print(decoded_token)
except jwt.InvalidTokenError:
    print("Token invalido")
except jwt.ExpiredSignatureError:
    print("Token expirado")

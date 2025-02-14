## **JSON Web Token (JWT)**
✅ **JWT is a compact, URL-safe token format used for authentication and data exchange.**  
✅ **It allows secure, stateless authentication** (no need for a session in a database).  

### **Structure of a JWT**
A JWT consists of **three parts**, separated by dots (`.`):
```
Header.Payload.Signature
```

Example:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzAwMDAwMDB9.FxPT8V1qlbZcFyMqChfLOPtD7GoMVq7bQclWKn4eQ_U
```

### **JWT Components**
| **Part** | **Description** | **Example (Decoded)** |
|---------|----------------|------------------|
| **Header** | Contains algorithm & token type | `{ "alg": "HS256", "typ": "JWT" }` |
| **Payload** | Contains claims (user data) | `{ "user_id": 1, "exp": 1670000000 }` |
| **Signature** | Ensures integrity | HMACSHA256(header + payload, secret) |

### **Verifying a JWT**
- The **server checks the signature** to confirm it wasn’t tampered with.
- JWTs **expire (`exp` claim)**, reducing security risks.

### **Common Use Cases**
✅ **User authentication** (login systems).  
✅ **API authorization** (secure REST APIs).  
✅ **Session management** (JWT instead of cookies).  

### **Installing `PyJWT`**
```bash
pip install PyJWT
```

### **Generating a JWT Token**
```python
import jwt
import datetime

SECRET_KEY = "your_secret"

def generate_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

token = generate_jwt(1)
print(token)
```

### **Verifying a JWT Token**
```python
def verify_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

print(verify_jwt(token))
```

✅ **Used in Flask/FastAPI authentication systems** to secure API endpoints.

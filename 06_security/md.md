# **Authentication & Security in Python: JWT, OAuth, SSO, 2FA**

Python provides libraries to **implement authentication, authorization, and security mechanisms** like **JWT, OAuth, SSO, and 2FA** in web applications and APIs.

---

## **1. JSON Web Token (JWT) in Python**
✅ **Used for stateless authentication in APIs.**  
✅ **Saves session information in a signed token instead of a database.**  
✅ **Commonly used with Flask, FastAPI, and Django.**

### **1.1 Installing `PyJWT`**
```bash
pip install PyJWT
```

### **1.2 Generating a JWT Token**
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

### **1.3 Verifying a JWT Token**
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

---

## **2. OAuth in Python**
✅ **OAuth is used for delegated authentication (e.g., "Login with Google").**  
✅ **Python supports OAuth via the `authlib` and `requests-oauthlib` libraries.**  
✅ **Used in Django, Flask, FastAPI for social login.**

### **2.1 Installing OAuth Libraries**
```bash
pip install authlib requests-oauthlib
```

### **2.2 OAuth Authentication with Google (Flask Example)**
```python
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "random_secret_key"
oauth = OAuth(app)

# Configure Google OAuth
google = oauth.register(
    name="google",
    client_id="your-client-id",
    client_secret="your-client-secret",
    access_token_url="https://oauth2.googleapis.com/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_kwargs={"scope": "email profile"}
)

@app.route("/login")
def login():
    return google.authorize_redirect(redirect_uri=url_for("callback", _external=True))

@app.route("/callback")
def callback():
    token = google.authorize_access_token()
    user_info = google.get("https://www.googleapis.com/oauth2/v1/userinfo").json()
    return f"Hello {user_info['name']}"

if __name__ == "__main__":
    app.run(debug=True)
```

✅ **This example allows users to log in via Google OAuth in a Flask app.**

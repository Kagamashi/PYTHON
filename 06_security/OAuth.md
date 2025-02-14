## **OAuth (Open Authorization)**
✅ **OAuth is an open standard for delegated authorization.**  
✅ **Allows users to grant limited access to their resources (e.g., GitHub, Google) without sharing passwords.**  

### **How OAuth Works**
1. **User requests access** (e.g., logs in via Google).
2. **OAuth server authorizes** and provides an **access token**.
3. **Client uses the token** to access protected resources.

### **OAuth Grant Types**
| **Grant Type** | **Use Case** |
|--------------|-------------|
| **Authorization Code** | Secure, best for web apps (redirect-based login) |
| **Client Credentials** | Machine-to-machine authentication (no user involved) |
| **Password Grant** | Not recommended (requires user’s password) |
| **Implicit Grant** | Deprecated due to security risks |

### **OAuth vs JWT**
| **Feature** | **OAuth** | **JWT** |
|------------|---------|--------|
| **Purpose** | Authorization | Authentication |
| **Stateful?** | Yes (depends on an OAuth provider) | No (stateless) |
| **Best For** | Access control (APIs) | Token-based authentication |

✅ **OAuth is commonly used for third-party authentication (Google, GitHub login).**  

### **Installing OAuth Libraries**
```bash
pip install authlib requests-oauthlib
```

### **OAuth Authentication with Google (Flask Example)**
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

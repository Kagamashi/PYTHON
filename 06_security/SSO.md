## **Single Sign-On (SSO)**
✅ **SSO allows users to log in once and access multiple applications.**  
✅ **Reduces password fatigue and improves security.**  

### **How SSO Works**
1. **User logs into the Identity Provider (IdP)**.
2. **IdP generates a session/token**.
3. **User can access multiple services without logging in again.**

### **Common SSO Protocols**
| **Protocol** | **Description** |
|-------------|----------------|
| **SAML (Security Assertion Markup Language)** | XML-based, used in enterprises (Okta, Microsoft Entra ID) |
| **OAuth 2.0 / OpenID Connect (OIDC)** | Used for modern web & mobile authentication |
| **Kerberos** | Used in Windows Active Directory |

✅ **SSO is commonly used in corporate environments (Google Workspace, Microsoft 365).**  

### **Using `django-allauth` for SSO in Django**
```bash
pip install django-allauth
```

Modify `settings.py`:
```python
INSTALLED_APPS = [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1
```

✅ **Users can log in using Google, GitHub, or other OAuth providers in Django.**

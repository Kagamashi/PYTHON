## **Two-Factor Authentication (2FA)**
✅ **2FA enhances security by requiring two authentication factors.**  
✅ **Prevents unauthorized access even if a password is stolen.**  

### **Types of 2FA Factors**
| **Factor** | **Example** |
|-----------|------------|
| **Something You Know** | Password, PIN |
| **Something You Have** | SMS code, Authenticator app (Google Authenticator) |
| **Something You Are** | Biometrics (fingerprint, Face ID) |

### **How 2FA Works**
1. **User enters a password** (first factor).
2. **User verifies via a second factor** (OTP, push notification).
3. **Access is granted** only if both factors are correct.

### **Common 2FA Methods**
- **Time-Based One-Time Password (TOTP)**: Apps like **Google Authenticator**.
- **SMS-based authentication** (less secure).
- **Push notifications** (e.g., **Duo, Authy**).
- **Biometric authentication** (fingerprint, Face ID).

✅ **2FA is recommended for securing accounts, especially admin and financial accounts.**

### **Installing `pyotp` for OTP-based 2FA**
```bash
pip install pyotp
```

### **Generating and Verifying OTPs**
```python
import pyotp

# Generate a new secret key
secret = pyotp.random_base32()
print(f"Secret Key: {secret}")

# Generate a Time-Based OTP (TOTP)
totp = pyotp.TOTP(secret)
print(f"Current OTP: {totp.now()}")

# Verifying OTP
otp_entered = input("Enter OTP: ")
if totp.verify(otp_entered):
    print("OTP Verified")
else:
    print("Invalid OTP")
```

✅ **This works with Google Authenticator or Authy for OTP-based login.**
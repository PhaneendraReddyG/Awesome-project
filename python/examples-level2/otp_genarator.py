import random
import string
import time
import sys

def generate_otp(length=6, alphanumeric=True):
    if alphanumeric:
        characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    else:
        characters = string.digits  # Only 0-9

    otp = ''.join(random.choices(characters, k=length))
    return otp

# Example Usage
otp_length = 6  # Change as needed
otp = generate_otp(otp_length, alphanumeric=False)  # Set False for numeric OTP
print("Generated OTP:", otp)

current_time = time.strftime("%H:%M:%S")
print("current time:", current_time)

print(sys.version)

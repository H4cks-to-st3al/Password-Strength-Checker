import re

def strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[a-z]',password):
        return False
    
    if not re.search(r'[A-Z]',password):
        return False
    
    if not re.search(r'\d',password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    
    return True

password = input('Enter your Strong Password: ')
valid=strong_password(password)

if valid :
    print("Your Password is Strong!")

else:
    print("Your Password is Weak!")
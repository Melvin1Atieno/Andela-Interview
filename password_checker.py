import re

def check_password(password):
    """ chek password method"""
    passwords = password.split(",")
    for password in passwords:
        if len(password) < 6:
            errormsg = "minimum length should be 6 characters"
            passwords.remove(password)
        if len(password) > 12:
            errormsg = "maximum password length 12"
            passwords.remove(password)
        if not re.search(r'[a-z]+',password):
            errormsg = "password must have atleast 1 letter between a-z"
            passwords.remove(password)
        if not re.search (r'[A-Z]+',password):
            errormsg = "password must have atleast one letter between A-Z"
            passwords.remove(password)
        if not re.search(r'[0-9]', password):
            errormsg = "password must have atleast one number between 0-9"
            passwords.remove(password)
        if not re.search(r'\W+', password):
            errormsg = "password must have atleast one character from #$@"
            passwords.remove(password)
    if passwords:
        return ",".join(passwords)
    else:
        return errormsg
    # else:
    #     return errormsg

    
        

myname = "ABd12341"


print(check_password(myname))
        
        
        






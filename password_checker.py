import re

def check_password(password):
    """ chek password method"""
    passwords = password.split(",")
    valid_passwords = ""
    for password in passwords:
        if len(password) < 6:
            errormsg = "minimum length should be 6 characters"
            passwords.remove(password)
        elif len(password) > 12:
            errormsg = "maximum password length 12"
            password.remove(password)
        elif not re.search(r'[a-z]+',password):
            errormsg = "password must have atleast 1 letter between a-z"
            passwords.remove(password)
        elif not re.search (r'[A-Z]+',password):
            errormsg = "password must have atleast one letter between A-Z"
            passwords.remove(password)
        elif not re.search(r'[0-9]', password):
            errormsg = "password must have atleast one number between 0-9"
            passwords.remove(password)
        elif not re.search(r'\W+', password):
            errormsg = "password must have atleast one character from #$@"
            passwords.remove(password)
        else:
            passwords = "".join(passwords)
    if errormsg:
       return errormsg
    else:
        return passwords

    
        

myname = "myname"

print(check_password(myname))
        
        
        






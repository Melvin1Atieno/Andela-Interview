import re

def check_password(password):
    """ chek password method"""
    valid_passwords = []
    passwords = password.split(",")
    for password in passwords:
        if len(password) < 6:
            errormsg = "minimum length should be 6 characters"
        elif len(password) > 12:
            errormsg = "maximum password length 12"
        elif not re.search(r'[a-z]',password):
            errormsg = "password must have atleast 1 letter between a-z"
        elif not re.search (r'[A-Z]',password):
            errormsg = "password must have atleast one letter between A-Z"
        elif not re.search(r'[0-9]', password):
            errormsg = "password must have atleast one number between 0-9"
        elif not re.search(r'[#$@]', password):
            errormsg = "password must have atleast one character from #$@"
        else:
            valid_passwords.append(password)
    if valid_passwords:
        return ",".join(valid_passwords)
    else:
        return errormsg


        


        
        
        






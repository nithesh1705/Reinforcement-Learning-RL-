import re

def phonenumber(number):

    regex = '[6-9]{1}[0-9]{9}'

    if(re.fullmatch(regex, number)):
        return True
    else:
        return False


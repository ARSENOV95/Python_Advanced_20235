class PasswordTooShortError(Exception):
    '''Password must contain at least 8 characters'''
    pass

class PasswordTooCommonError(Exception):
    '''Password must be a combination of digits, letters, and special characters'''
    pass

class PasswordNoSpecialCharactersError(Exception):
    '''PasswordNoSpecialCharactersError'''
    pass
class PasswordContainsSpacesError(Exception):
    '''Password must not contain empty spaces'''
    pass

def validate(password: str):
    special_chars = ("@","*","&", "%")
    is_all_digits = password.isdigit()
    is_all_string = password.isalpha()
    is_all_special = all(chr in special_chars for chr in password)

    if len(password) < 8:
        raise PasswordTooShortError('Password must contain at least 8 characters')
    
    if is_all_digits or is_all_string or is_all_special:
        raise PasswordNoSpecialCharactersError('Password must be a combination of digits, letters, and special characters')

    if not any(chr in special_chars for char in password): #check if any of the chars are special
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character') 
    
    #cnt_special = sum(1 for chr in password if chr in special_chars) #check if any of the chars are special V2
    #if cnt_special < 1:
    #    raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character') 
    
    if " " in password:
        raise PasswordContainsSpacesError('Password must not contain empty spaces')
    
while (current_password := input()) != 'Done':

    validate(current_password)

    print('Password is valid')



    
        
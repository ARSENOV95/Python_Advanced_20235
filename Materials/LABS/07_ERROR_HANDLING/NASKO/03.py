class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARS = ("@","*", "&","%")


def password_too_common(pwd :str,special_chars):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    #only_special = sum(x for x in pwd if x in special_chars)
    only_specials = all(x in special_chars for x in pwd)
    return only_digits or only_letters or only_specials

while True:
    password = input()

    if password == 'Done':
        break

    if len(password) < 8:
        raise PasswordTooShortError('Password must contain at least 8 character') 
    
    if password_too_common(password,SPECIAL_CHARS):
        raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')
    
    if not any(x in SPECIAL_CHARS for x in password):
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')
    
    if ' ' in password:
        raise PasswordContainsSpacesError('Password must not contain empty spaces')
    
    print('Password is valid')
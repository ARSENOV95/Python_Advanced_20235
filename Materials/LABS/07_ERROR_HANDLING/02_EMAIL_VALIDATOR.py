import re

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

domains = ['.com','.bg','.net','.org']

email = r'([A-Za-z0-9]+)@([A-Za-z]+).([A-Za-z]+)'


current_email = input()
while True:
    if current_email == 'End':
        break

    match = re.match(email,current_email)

    try:
        if '@' in match.groups():
            
    except MustContainAtSymbolError:
        raise MustContainAtSymbolError('Email must contain @')
    
    current_email = input()



    #f not match MustContainAtSymbolError:
    #    raise MustContainAtSymbolError('Email must contain @')

    
    #print(match.group(1))

    #if len (match.group(1)) < 4:
    #    raise NameTooShortError('Name must be more than 4 characters')
    
    #elif match.group(3) not in domains:
    #    raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    #print('Email is valid'
    
   



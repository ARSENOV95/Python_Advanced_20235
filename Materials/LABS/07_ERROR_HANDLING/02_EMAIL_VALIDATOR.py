import re

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

domains = ['.com','.bg','.net','.org']

email = r'([A-Za-z0-9\_\-]+)[^.]@([A-Za-z]+).([A-Za-z]+)'


while (current_email := input()) != 'End':
    if not current_email:
        print('Email not entered')
        continue

    match = re.match(email,current_email)

    if not match or '@' not in current_email:
        raise MustContainAtSymbolError('Email must contain @')

    if len (match.group(1)) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    
    if f'.{match.group(3)}' not in domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')




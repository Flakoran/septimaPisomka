# sem doplnte link na svoj kod
# https://github.com/shalamun/SEN_pisomka_1

import os;

def check_password(password: str) -> bool:    
    small_letter = False
    capital_letter = False
    number = False
    length = False

    for c in password:
        if(c.isdigit()):
            small_letter = True
        elif(c.isupper()):
            capital_letter = True

    if len(password.strip()) >= 8:
        length = True

    return small_letter and capital_letter and number
    return small_letter and capital_letter and number and length


dir = os.path.dirname(__file__)                     # Nacita cestu k suboru
with open(dir + "/passwords.txt", 'r') as file:     # Otvori subor s heslami
    for password in file:                           # Prejde vsetky riadky/hesla
        if check_password(password):                # Skontroluje ich
            print(password, end = "")
#ach jaj aaa

import string
import random
import re

class PassLogin():

    def Letters(self):
        letters = string.ascii_letters
        massLetters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "*", "%", "#", "@", "&", "$", "^", "+", "_", "-"]
        for letter in letters:
            massLetters.append(letter)
        return massLetters


    def passGenerator(self, lenPass) -> str:
        password = ""
        massLetters = self.Letters()
        regPass = "[0-9a-zA-Z!@#$%^&*_-]{"+str(lenPass-1)+",}"
    
        while len(password) < lenPass:
            if re.match(regPass, password) is not None:
                print(password)
                break
            else:
                password+=str(massLetters[random.randint(0, len(massLetters)-1)])
    

    def loginGenerator(self, lenLogin, domainName):
        massLetters = string.ascii_letters
        login = ""
        regLogin = "[0-9a-zA-Z]{"+str(lenLogin-1)+",}"
        while len(login) < lenLogin:
            if re.match(regLogin, login) is not None:
                print(login+"@"+str(domainName))
                break
            else:
                login+=str(massLetters[random.randint(0, len(massLetters)-1)])

PL = PassLogin()   
def checkLenPass():
    lenLogin = int(input("Enter len login (10, 15, 20): "))
    domainName = str(input("Enter domain name (yandex.ru, mail.ru, etc): "))
    lenPass = int(input("Enter len password (10, 15, 20): "))
    if lenLogin and domainName and lenPass:
        PL.loginGenerator(lenLogin, domainName)
        PL.passGenerator(lenPass)
    else:
        checkLenPass()

checkLenPass()

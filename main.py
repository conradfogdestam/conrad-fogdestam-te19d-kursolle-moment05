#kursolle moment05 bankapp
#Conrad Fogdestam te19d

import os # för att kunna wipea alla filer
import FUNKTIONER #py fil med funktioner för att hantera balance
import sys # stänga programmet vid EXIT
from colorama import init #färgtext
from colorama import Fore #färgtext
init(autoreset=True) #färgtext reset efter varje print

file_users = 'accountfile.txt' # sparar alla usernames som registreras
logged_in_user = [] # lista för at kunna använda usernamet som loggas in med i funktionerna
logged_in_password = [] # lista för at kunna använda passwordet som loggas in med i funktionerna


def register():
    print(Fore.LIGHTMAGENTA_EX + 'Input credentials to register account: ')
    username = input(Fore.CYAN + "Username: ")
    password = input(Fore.CYAN + "Password: ")
    with open(username + 'transactions.txt', 'a+') as f: # skriver ner en balance på 1000 till att börja i transacions filen
        f.write('Balance $1000\n')
    with open(username + 'profile.txt', 'w+') as f: # skriver användare info i profile filen
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write(" ")
        f.write('1000')
    with open(file_users, "a") as f: # skriver till alla username och password som registreras till accountfile.txt som login funktionen använder
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write("\n")
        f.close()
        print(Fore.LIGHTMAGENTA_EX + f'Account set up, thank you for choosing CAYMAN ISLANDS NATIONAL BANK™')


def login():
    print(Fore.LIGHTMAGENTA_EX + 'To login please input your credentials')
    username = input(Fore.CYAN + "Username: ")
    password = input(Fore.CYAN + "Password: ")
    logged_in_user.append(username)  # appendar username till logged_in_user så det kan användar i funktionerna sedan
    logged_in_password.append(password)  # appendar passwored till logged_in_password så det kan användar i funktionerna sedan
    for line in open(file_users, "r").readlines(): # löser igenom alla rader i accountfile.txt och letar efter match
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]: # returnar true om båda är sanna
            print(Fore.LIGHTMAGENTA_EX + "LOGGED IN AS '{}'".format(username)) # låter användaren veta att dom loggats in
            return True
    print(Fore.LIGHTRED_EX + "LOGIN FAIL") # ifall username och password inte finns/ matchar
    return False


while True:
    userinput = input(Fore.LIGHTCYAN_EX + '''
        CAYMAN ISLANDS NATIONAL BANK™
            L) Login
            R) Register
            E) EXIT
            ''').upper() # första menyn med register, login och exit

    if userinput == 'R': # kör register funktinen
        try:
            register()
        except:
            print('Invalid input')


    if userinput == 'E': # exitar
        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE')
        break

    if userinput == 'L':
        try:
            if login() == True: #kör login funktionen

                while True:

                    user = (str(logged_in_user).join(logged_in_user)) # joinar listan me username så att den går att använda till funktionerna balance, withdraw, deposit
                    password = (str(logged_in_password).join(logged_in_password)) # joinar listan med password så att den går att använda till funktionerna balance, withdraw, deposit

                    userinput = input(Fore.LIGHTCYAN_EX + 'CAYMAN ISLANDS NATIONAL BANK™\n D) Make deposit\n W) Make withdrawal\n T) Check transactions\n B) Check available balance\n E) EXIT\nEnter "TERMINATE" to delete all data\n').upper()

                    if userinput == 'W':
                        try:
                            ui = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to withdraw? '))
                            if ui < FUNKTIONER.check_balance(str(user)): # checkar så dom inte kan ta ut mer än vad som finns på kontot
                                FUNKTIONER.withdrawal(user, password, ui)# kör withdrawfunktionen som ändrar balance i 'username'+profile filen och skriver ut all info efter ändringen
                                print(Fore.LIGHTMAGENTA_EX + '${} withdrawn from account '.format(ui)) # användarvänligt
                                with open(str(user) + 'transactions.txt', 'a+') as f: # lägger till transaktionen i 'username'+transactions.txt filen
                                    f.write(f'- ${ui}, Available balance: $' + str(FUNKTIONER.check_balance(user)) + '\n')

                            else:
                                print('Insufficient funds!!!!!!')
                                print('Funds currently available to withdraw $', FUNKTIONER.check_balance(str(user))) # om dom skulle skriva in mer än vad som finns i kontot
                        except:
                            print(Fore.LIGHTRED_EX + 'Input error, needs to be integer') # om inputen failar, så krachar inte programmet


                    elif userinput == 'D':
                        try:
                            uis = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to deposit?'))
                            FUNKTIONER.deposit(user, password, uis) # kör funktionen deposit som ändrar balance i 'username'+profile filen och skriver ut all info efter ändringen
                            print(Fore.LIGHTMAGENTA_EX + '${} deposited to account'.format(uis))
                            with open(str(user) + 'transactions.txt', 'a+') as f: # lägger till transaktionen i 'username'+transactions.txt filen
                                f.write(f'+ ${uis}, Available balance: $' + str(FUNKTIONER.check_balance(user)) + '\n')


                        except:
                            print(Fore.LIGHTRED_EX + 'Input error, needs to be an integer') # om inputen failar, så krachar inte programmet

                    elif userinput == 'T':

                        with open(str(user) + 'transactions.txt', 'r+') as f: # printar alla transactions från 'username'transactions med en enkel for loop
                            for line in (str(user) + 'transactions.txt'):
                                print(Fore.LIGHTCYAN_EX + f.read())


                    elif userinput == 'B':
                        print(Fore.LIGHTCYAN_EX + FUNKTIONER.check_balance(str(user))) # kör en simpel balance funktion från FUNKTIONER

                    elif userinput == 'E':
                        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE') # exit till första menyn
                        sys.exit()

                    elif userinput == 'TERMINATE': # deletar alla filer som finns på användaren som är inloggad
                        os.remove(str(user) + 'profile.txt')
                        os.remove(str(user) + 'transactions.txt')
                        with open(file_users, "r") as f: # löser inn alla rader ur accountfile.txt
                            lines = f.readlines()
                        with open(file_users, "w") as f:#skriver in alla rader förutom  'if line.strip("\n") != str(user) + ' ' + str(password):'
                            for line in lines:
                                if line.strip("\n") != str(user) + ' ' + str(password):
                                    f.write(line)
                        print(Fore.LIGHTMAGENTA_EX + 'Sucsessfully deleted all files!!!')# användarvänligt
                        sys.exit()
        except:
            print('No account registerd to that username and password, try to register instead!') # om någon skulle försöka logga in utan att registrera först (så det inte krashar )

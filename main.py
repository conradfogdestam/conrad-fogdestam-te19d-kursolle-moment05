#kursolle moment05 bankapp
#Conrad Fogdestam te19d

import os # för att kunna wipea alla filer
import FUNKTIONER
import sys # stänga programmet vid EXIT
from colorama import init #färgtext
from colorama import Fore #färgtext
init(autoreset=True) #färgtext reset efter varje print

file_users = 'accountfile.txt'
logged_in_user = []
logged_in_password = []


def register():
    print(Fore.LIGHTMAGENTA_EX + 'Input credentials to register account: ')
    username = input(Fore.CYAN + "Username: ")
    password = input(Fore.CYAN + "Password: ")
    with open(username + 'transactions.txt', 'a+') as f:
        f.write('Balance $1000\n')
    with open(username + 'profile.txt', 'w+') as f:
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write(" ")
        f.write('1000')
    with open(file_users, "a") as f:
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
    logged_in_user.append(username)
    logged_in_password.append(password)
    for line in open(file_users, "r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print(Fore.LIGHTMAGENTA_EX + "LOGGED IN AS '{}'".format(username))
            return True
    print(Fore.LIGHTRED_EX + "LOGIN FAIL")
    return False


while True:
    userinput = input(Fore.LIGHTCYAN_EX + '''
        CAYMAN ISLANDS NATIONAL BANK™
            L) Login
            R) Register
            E) EXIT
            ''').upper()

    if userinput == 'R':
        register()


    if userinput == 'E':
        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE')
        break

    if userinput == 'L':
            if login() == True:

                while True:

                    user = (str(logged_in_user).join(logged_in_user))
                    password = (str(logged_in_password).join(logged_in_password))

                    userinput = input(Fore.LIGHTCYAN_EX + 'CAYMAN ISLANDS NATIONAL BANK™\n D) Make deposit\n W) Make withdrawal\n T) Check transactions\n B) Check available balance\n E) EXIT\nEnter "TERMINATE" to delete all data\n').upper()

                    if userinput == 'W':

                        ui = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to withdraw? '))
                        if ui < FUNKTIONER.check_balance(str(user)):
                            print('gg')
                            FUNKTIONER.withdrawal(user, password, ui)
                            print(Fore.LIGHTMAGENTA_EX + '${} withdrawn from account '.format(ui))
                            with open(str(user) + 'transactions.txt', 'a+') as f:
                                f.write(f'- ${ui}, Available balance: $' + str(FUNKTIONER.check_balance(user)) + '\n')

                        else:
                            print('Insufficient funds!!!!!!')
                            print('Funds currently available to withdraw $', FUNKTIONER.check_balance(str(user)))


                    elif userinput == 'D':
                        try:
                            uis = int(input(Fore.LIGHTMAGENTA_EX + 'How much would you like to deposit?'))
                            FUNKTIONER.deposit(user, password, uis)
                            print(Fore.LIGHTMAGENTA_EX + '${} deposited to account'.format(uis))
                            with open(str(user) + 'transactions.txt', 'a+') as f:
                                f.write(f'+ ${uis}, Available balance: $' + str(FUNKTIONER.check_balance(user)) + '\n')


                        except:
                            print(Fore.LIGHTRED_EX + 'Deposit needs to be an integer')

                    elif userinput == 'T':

                        with open(str(user) + 'transactions.txt', 'r+') as f:
                            for line in (str(user) + 'transactions.txt'):
                                print(Fore.LIGHTCYAN_EX + f.read())


                    elif userinput == 'B':
                        print(Fore.LIGHTCYAN_EX + FUNKTIONER.check_balance(str(user)))

                    elif userinput == 'E':
                        print(Fore.LIGHTMAGENTA_EX + 'GOODBYE')
                        sys.exit()

                    elif userinput == 'TERMINATE':
                        os.remove(str(user) + 'profile.txt')
                        os.remove(str(user) + 'transactions.txt')
                        with open(file_users, "r") as f:
                            lines = f.readlines()
                        with open(file_users, "w") as f:
                            for line in lines:
                                if line.strip("\n") != str(user) + ' ' + str(password):
                                    f.write(line)
                        print(Fore.LIGHTMAGENTA_EX + 'Sucsessfully deleted all files!!!')
                        sys.exit()


def check_balance(username):
    with open(username + 'profile.txt', 'r') as f:
        danyboi = f.readline().split(' ')
        return int(danyboi[-1])

def withdrawal(username, password, minus):
    with open(username + 'profile.txt', 'r') as f:
        dankyboi = f.readline().split(' ')
        new = int(dankyboi[2]) - minus
    with open(username + 'profile.txt', 'w+') as f:
        f.truncate()
        f.write(username)
        f.write(' ')
        f.write(password)
        f.write(' ')
        f.write(str(new))

def deposit(username, password, plus):
    with open(username + 'profile.txt', 'r') as f:
        dankyboi = f.readline().split(' ')
        new = int(dankyboi[-1]) + plus
        with open(username + 'profile.txt', 'w+') as f:
            f.truncate()
            f.write(username)
            f.write(' ')
            f.write(password)
            f.write(' ')
            f.write(str(new))





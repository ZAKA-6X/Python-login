import time
users=[]

while True:    
    print('WELCOME TO 6X COMPANY: ')
    print('1.Sign In\n2.Sing Up\n0.Quitter')
    choix=int(input('=>'))
    if choix==0:
        print('goodbye')
        break
    elif choix==1:
        username=input('username: ')
        password=input('password: ')
        if (username, password) in users:
            print('welcome back', username)
            time.sleep(3)
        else:
            print('The Username or the Password is False, please register')
            time.sleep(3)
    elif choix==2:
        username=input('username: ')
        password=input('password: ')
        while (username) in users:
            print('This username is already used please Change it')
            username=input('username: ')
            password=input('password: ')
        users.append((username, password))
        print('You are now registed')
        time.sleep(3)

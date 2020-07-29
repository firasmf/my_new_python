num_tries = 0
while num_tries != 3:

    username = input('Please Insert Your User Name: ')
    password = input('Please Insert Your Password: ')

    if username == 'sam' and password == '123':
        print('Welcome Mr.'+username)
        num_tries = 0
        exit()

    else:
        print('Error !!!')
        num_tries += 1
        print('You Have ' + str(3 - num_tries) + 'left')


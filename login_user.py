login = input('Enter you user name: ')
password = input('Creat password: ')
print('--------------')
login_1 = input('User name: ')
password_1 = input('Password: ')

if login_1 != login.lower() or password_1 != password.lower():
    print('Login Fail. ERROR!')
else:
    print(f'Welcome {login}')

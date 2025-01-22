password = input('Type the password:')
attempt = 3
correct = 'python123'
while password != correct:
    attempt -= 1
    print(f'Incorrect password. Remaining attempts: {attempt}')
    if attempt == 0:
        print('No remaining attempts. Acces denied.')
        break
    password = input()
else:
    print('Access permitted')
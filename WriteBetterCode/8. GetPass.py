'''
    Let's input some sensitive information
'''
print('Input w/o GetPass')

username = input('Username: ')
password = input('Password: ')

print('Logging In...')


'''
    Let's see the better way of doing this
'''

print('Input w/ GetPass')
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Password you have entered is captured rightly : ', password)
print('Logging In...')
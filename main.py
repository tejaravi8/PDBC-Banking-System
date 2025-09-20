print('----------welcome to myBank---------')
print(
'''
1.signUp ( new user )
2.login  ( already have account )
3.exit   ( close )
''')
option=int(input('enter your option: '))

if option==1:
    from signup import signup
    
    signup()
    
if option==2:
    from login import login
    
    login()
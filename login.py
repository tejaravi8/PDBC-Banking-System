import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja_41863',
    database='mybank'
)

cursor=mydb.cursor()


def login():
    print('\nEnter Details here..!\n')
    username=input('Username               : ')
    password=input('Password               : ')
    role=input('Role ( Admin/Customer) : ')
    
    cursor.execute('select * from users where username=%s and password=%s',(username,password,))
    data=cursor.fetchone()
    user_id,uname,pswd,user_role=data
    print(f'\n hello {uname}..\n')
    
    print('\n2.check balance')
    print('1.withdraw balance')
    print('3.Deposite Balance')
    
    option=int(input('\nChoose your option: '))
    
    #1.withdraw money
    
    if option==1:
        print(f'\n hello {uname}..\n')
        amount=int(input('Enter Withdraw Amount : '))
        password=input('\nEnter Password to confirm: ')
        if password==pswd:
            cursor.execute('update accounts set acc_bal=acc_bal-%s where user_id=%s',(amount,user_id,))
            mydb.commit()
            cursor.execute('select * from accounts where user_id=%s',(user_id,))
            acdata=cursor.fetchone()
            acc_id,user_id,acc_type,acc_bal=acdata
            print(f'\nsuccessfully debited,your available balance is {acc_bal}')
    
    # 2.check balance
    
    if option==2:
        print(f'\n hello {uname}..\n')
        password=input('Enter Password to check : ')
        if password==pswd:
            cursor.execute('select acc_bal from accounts where user_id=%s',(user_id,))
            acdata=cursor.fetchone()
            acc_bal=acdata
            print(f'\nyour current balance is {acc_bal}')
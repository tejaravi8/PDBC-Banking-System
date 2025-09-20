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
    
    if option==1:
        print(f'\n hello {uname}..\n')
        amount=int(input('Enter Withdraw Amount : '))
        password=input('Enter Password : ')
        if password==pswd:
            cursor.execute('update accounts set acc_bal=acc_bal-%s where user_id=%s',(amount,user_id,))
            mydb.commit()
            print('successfully debited')
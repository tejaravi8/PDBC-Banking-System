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
    role=input('Role ( Admin/Customer) : ').lower()
    
    cursor.execute('select * from users where username=%s and password=%s',(username,password,))
    data=cursor.fetchone()
    user_id,uname,pswd,user_role=data
    if user_role==role and role=='customer':
        print(f'\n hello {uname}..\n')
        print('\n1.withdraw balance')
        print('2.check balance')
        print('3.Deposite Balance')
        print('4.requests')
        option=int(input('\nChoose your option: '))
        
        #1.withdraw money
        
        if option==1:
            print(f'\n----- withdraw balance -----\n')
            cursor.execute('select * from accounts where user_id=%s',(user_id,))
            ac_data=cursor.fetchone()
            acc_id,user_id,acc_type,acc_bal=ac_data
            
            amount=int(input('Enter Withdraw Amount : '))
            password=input('\nEnter Password to confirm: ')
            
            if password==pswd:
                if amount<=acc_bal:
                    cursor.execute('update accounts set acc_bal=acc_bal-%s where user_id=%s',(amount,user_id,))
                    mydb.commit()
                    cursor.execute('select * from accounts where user_id=%s',(user_id,))
                    acdata=cursor.fetchone()
                    acc_id,user_id,acc_type,acc_bal=acdata
                    print(f'\nsuccessfully debited,your available balance is {acc_bal}')
                else:
                    print('\nInsufficient Balance')
            else:
                print('\nIncorrect password.....!')
        
        # 2.check balance
        
        if option==2:
            print(f'\n----- Check Balance -----\n')
            password=input('Enter Password to check : ')
            if password==pswd:
                cursor.execute('select acc_bal from accounts where user_id=%s',(user_id,))
                acdata=cursor.fetchone()
                acc_bal,=acdata                                            # tuple unpacking single value
                print(f'\nyour current balance is {acc_bal}\n')
        
        #Deposite Amount
          
        if option==3:
            print(f"\n------ Deposite Section ------")
            amount=int(input('\nEnter Withdraw Amount : '))
            cursor.execute('update accounts set acc_bal=acc_bal+%s where user_id=%s',(amount,user_id,))
            mydb.commit()
            cursor.execute('select * from accounts where user_id=%s',(user_id,))
            acdata=cursor.fetchone()
            acc_id,user_id,acc_type,acc_bal=acdata
            print(f'\nsuccessfully Credited {amount},your available balance is {acc_bal}')
        
        #Requests
        
        if option==4:
            print("\n------ Requests section ------\n")
            print("1.Loan")
            print('2.Apply for Atm_card')
            print('3.check book')
            print('4.netbanking')
            
            reqest=int(input('choose your option type(1/2/3/4): '))
            def requests(user_id,req_type,amt):
                cursor.execute('insert into requests(user_id,req_type,req_bal) values(%s,%s,%s)',(user_id,req_type,amt))
                mydb.commit()
                print("\nRequest Raised Successfully\n")
                
            if reqest==1:
                amt=int(input('Enter Amount for Loan: '))
                req_type='loan'
                requests(user_id,req_type,amt)
            elif reqest==2:
                amt=0
                req_type='atm_card'
                requests(user_id,req_type,amt)
            elif reqest==3:
                amt=0
                req_type='check_book'
                requests(user_id,req_type,amt)
            elif reqest==4:
                amt=0
                req_type='net_banking'
                requests(user_id,req_type,amt)
            else:
                print('You choose wrong option')
            
                
    if user_role==role and role=='admin':
        print("\n----------- Admin menu -----------\n")
        print('\n1.Delete customer')
        print('2.Search Customer')
        print('3.xxxxxxxxxxx')
        option=int(input('\nenter you option (1/2/3/4): '))
        
        if option==1:
            cursor.execute('select * from users inner join accounts using(user_id)')
            a=cursor.fetchall()
            print(a)
            
            user_id=int(input('enter userid: '))
            cursor.execute('delete from users where user_id=%s',(user_id,))
            mydb.commit()
            
            print('\nCustomer removed successfully\n')
            
        elif option==2:
            cursor.execute('select * from users inner join accounts using(user_id)')
            a=cursor.fetchall()
            for i in a:
                print(i)
            
            acc_number=int(input('\nenter Account Number : '))
            cursor.execute('select * from users inner join accounts using(user_id) where user_id=%s',(acc_number,))
            a=cursor.fetchone()
            print(f'\n{a}')
        
        else:
            print('You Choose Wrong Option')
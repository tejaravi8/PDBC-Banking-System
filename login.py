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
        print('3.View requests')
        print('4.Manage requests')
        option=int(input('\nenter you option (1/2/3/4): '))
        
        # delete customer
        if option==1:
            cursor.execute('select * from users inner join accounts using(user_id)')
            a=cursor.fetchall()
            print(a)
            
            user_id=int(input('enter userid: '))
            cursor.execute('delete from accounts where user_id=%s',(user_id,))
            cursor.execute('delete from requests where user_id=%s',(user_id,))
            cursor.execute('delete from users where user_id=%s',(user_id,))
            mydb.commit()
            
            print('\nCustomer removed successfully\n')
            
        elif option==2:
            cursor.execute('select * from users inner join accounts using(user_id)')
            a=cursor.fetchall()
            for i in a:
                print(i)
            
            user_id=int(input('\nenter Account Number : '))
            cursor.execute('select * from users inner join accounts using(user_id) where user_id=%s',(user_id,))
            a=cursor.fetchone()
            print(f'\n{a}')
        
        elif option==3:
            def request():
                filter=input('enter req_type ( loan/ atm_card/ check_book/ net_banking/ all) : ')
                if filter=='all':
                    cursor.execute('select * from users inner join requests using(user_id)')
                    data=cursor.fetchall()
                    print(data)
                else:
                    cursor.execute('select * from users inner join requests using(user_id) where req_type=%s',(filter,))
                    data=cursor.fetchall()
                    for i in data:
                        print(i)
            request()
        elif option==4:
            # def requests():
            filter=input('enter req_type ( loan/ atm_card/ check_book/ net_banking/ all) : ')
            # status=input('enter req_status ( pending , rejected, success ) : ')
            if filter=='all':
                status=input('enter req_status ( pending , rejected, success ) : ')
                cursor.execute('select users.user_id,req_bal,req_status,req_type,req_id from users inner join requests using(user_id)')
                data=cursor.fetchall()
                # user_id,req_bal,req_status,req_type,req_id=data
                for i in data:
                    user_id,req_bal,req_status,req_type,req_id=i
                    if req_status==status:
                        print(i)
            else:
                cursor.execute('select users.user_id,req_bal,req_status,req_type,req_id from users inner join requests using(user_id) where req_type=%s',(filter,))
                data=cursor.fetchall()
                status=input('enter req_status ( pending , rejected, success ) : ')
                for i in data:
                    user_id,req_bal,rstatus,req_type,reqid=i
                    if rstatus==status:
                        print(i)
                
            req_id=int(input('enter req_id for req_change: '))
            cursor.execute('select users.user_id,req_bal,req_status,req_type,req_id from users inner join requests using(user_id) where req_id=%s',(req_id,))
            t=cursor.fetchall()
            print(t)
            if req_bal>300000:
                req_status='reject'
                cursor.execute('update requests set req_status=%s where req_id=%s',(req_status,req_id) )
                mydb.commit()
                # cursor.execute('update accounts where acc_bal=acc_bal+req_bal where user_id',(user_id))
                print('reject due to exceeds loan amount')
            elif 0<=req_bal<300000:
                req_status='success'
                cursor.execute('update requests set req_status=%s where req_id=%s',(req_status,req_id))
                cursor.execute('update accounts set acc_bal=acc_bal+%s where user_id=%s',(req_bal,user_id))
                mydb.commit()
                print('your request sanctioned successfully..')
            
            # data=requests()
            # for i in data:
            #     print(i)
            
        else:
            print('You Choose Wrong Option')
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja_41863',
    database='mybank'
)

cursor=mydb.cursor()   # cursor


# cursor.execute('CREATE DATABASE IF NOT EXISTS mybank')

# cursor.execute('''
# create table if not exists users(
# user_id INT PRIMARY KEY AUTO_INCREMENT,
# username VARCHAR(50) UNIQUE NOT NULL,
# password VARCHAR(20) NOT NULL,
# user_role enum("customer","admin") NOT NULL
# )''')

# alter table users auto_increment=1;

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS accounts(
# acc_id BIGINT PRIMARY KEY AUTO_INCREMENT,
# user_id INT NOT NULL,
# acc_type enum("SAVINGS","CUSTOMERS") NOT NULL,
# acc_bal DECIMAL(10,2) NOT NULL,
# FOREIGN KEY (user_id) REFERENCES users(user_id)
# )'''
# )

# ALTER TABLE accounts
# MODIFY COLUMN acc_type ENUM('SAVINGS','CURRENT');

# cursor.execute('show tables;')
# print(cursor.fetchall())


def signup():
    
    print('welcome to mybank , enter your details here..!: \n')
    username=input('enter your name: ').lower().strip()
    password=input('enter your password: ').strip()
    user_role=input('enter your role ( admin / customer ) : ').lower().strip()
    
    cursor.execute("INSERT INTO users(username,password,user_role) values(%s,%s,%s)",(username,password,user_role))
    mydb.commit()
    
    cursor.execute('select * from users where username= %s',(username,))
    data=cursor.fetchone()
    user_id,username,password,user_role=data
    
    print( f'\n hello {username}, enter details to proceed: ')
    
    acc_type=input("enter your account type ( SAVINGS / CURRENT ): ").strip().upper()
    acc_bal=int(input('enter your deposit amount (5000): '))
    cursor.execute("INSERT INTO accounts(user_id,acc_type,acc_bal) values(%s,%s,%s)",( user_id,acc_type,acc_bal))
    
    mydb.commit()
    
    print(f'hello {username},your account created successfully....!')
    
    

print('execute successfully')
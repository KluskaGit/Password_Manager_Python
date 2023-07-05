import mysql.connector
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

#MENU
def menu():
    print("""
    -------MENU-------
    1. Log in
    2. Register
    """)

    choice=input('Option : ')
    match choice:
        case '1':
            log_in()
        case '2':
            register()
        case other:
            print('No match found')
            menu()

def menuPass():
    print("""
    1. Display password
    2. Add new password
    3. Log out
    """)
    choice=input('Option : ')
    match choice:
        case '1':
            log_in()
        case '2':
            register()
        case other:
            print('No match found')
            menu()

#Log in function
def log_in():
    email=input('Email: ')
    password=input('Password: ')
    cursor.execute(f'SELECT * From users where email like "{email}"')

    all_users_data=cursor.fetchall()
    if all_users_data!=[] and len(all_users_data)==1:
        for row in all_users_data:
            try:
                if ph.verify(row['password'], password):
                    menuPass()
            except VerifyMismatchError:
                print('Invalid login or password')
                log_in()
        


#Register function
def register():
    email=input('Your email: ')
    password=input('Password: ')
    r_password=input('Repeat password: ')

    if password==r_password:
        hash_pas=ph.hash(password)
        cursor.execute(f'INSERT INTO users (email, password) values ("{email}", "{hash_pas}")')
        conn.commit()
        #log_in()

    

if __name__=='__main__':
    ph = PasswordHasher()
    
    conn = mysql.connector.connect(
        user='root', 
        password='kamil',
        host='localhost',
        database='m28441_passwords_manager'
        )
    cursor=conn.cursor(dictionary=True)
    menu()




    
    
    
    
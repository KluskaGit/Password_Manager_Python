import mysql.connector
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os

#MENU
def menu():
    os.system('cls')
    print("""
    -------MENU-------
    1. Log in
    2. Register
    """)

    choice=input('Option: ')
    match choice:
        case '1':
            log_in()
        case '2':
            register()
        case other:
            menu()

#Second menu after log in
def menuPass(id):
    os.system('cls')
    print("""
    1. Display password
    2. Add new password
    3. Log out
    4. Exit
    """)
    choice=input('Option: ')
    match choice:
        case '1':
            display_pas(id)
        case '2':
            add_pass(id)
        case '3':
            log_out()
        case '4':
            quit()
        case other:
            menuPass(id)

#View existing passwords
def display_pas(id):
    os.system('cls')
    print('Your passwords:\n')
    cursor.execute(f'SELECT * From all_passwords where user_id={id}')
    rows=cursor.fetchall()
    if rows !=[]:
        for row in rows:
            print(f"Platform: {row['platform']}\nPassword: {row['password']}\n-------------------")
        print('\n1. Go back')
        choice=input("Option: ")
        match choice:
            case '1':
                menuPass(id)
            case other:
                display_pas(id)
    else:
        print('No passwords to display')
        print('\n1. Go back')
        choice=input("Option: ")
        match choice:
            case '1':
                menuPass(id)
            case other:
                display_pas(id)

#Adding new passwords
def add_pass(id):
    os.system('cls')
    print('Add new password here:\n')
    platform=input('Platform name: ')
    password=input('Password: ')
    cursor.execute(f'INSERT INTO all_passwords (user_id, platform, password) values ({id}, "{platform}", "{password}")')
    conn.commit()
    print('Password has been added')
    menuPass(id)

#Log out   
def log_out():
    menu()

#Log in function
def log_in():
    os.system('cls')
    print("Log in here:\n")


    email=input('Email: ')
    password=input('Password: ')
    cursor.execute(f'SELECT * From users where email like "{email}"')

    all_users_data=cursor.fetchall()
    if all_users_data!=[] and len(all_users_data)==1:
        for row in all_users_data:
            try:
                if ph.verify(row['password'], password):
                    menuPass(row['user_id'])
            except VerifyMismatchError:
                print('Invalid login or password')
                log_in()
        
#Register function
def register():
    os.system('cls')
    print("Register here:\n")

    email=input('Your email: ')
    password=input('Password: ')
    r_password=input('Repeat password: ')

    if password==r_password:
        hash_pas=ph.hash(password)
        cursor.execute(f'INSERT INTO users (email, password) values ("{email}", "{hash_pas}")')
        conn.commit()
        menu()
    

    

if __name__=='__main__':

    ph = PasswordHasher()
    
    conn = mysql.connector.connect(
        user='root', 
        password='kamil',
        host='localhost',
        database='m28441_passwords_manager'
        )
    cursor=conn.cursor(dictionary=True)



    while(True):
        menu()




    
    
    
    
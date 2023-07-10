import mysql.connector
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os

#MENU
def menu(err):
    os.system('cls')
    print("""
    -------MENU-------
    1. Log in
    2. Register
    """)

    choice=input('Option: ')
    match choice:
        case '1':
            log_in(err)
        case '2':
            register(err)
        case other:
            menu(err)

#Second menu after log in
def menuPass(id, err):
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
            display_pas(id, err)
        case '2':
            add_pass(id, err)
        case '3':
            log_out(err)
        case '4':
            quit()
        case other:
            menuPass(id, err)

#View existing passwords
def display_pas(id, err):
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
                menuPass(id, err)
            case other:
                display_pas(id, err)
    else:
        print('No passwords to display')
        print('\n1. Go back')
        choice=input("Option: ")
        match choice:
            case '1':
                menuPass(id, err)
            case other:
                display_pas(id, err)

#Adding new passwords
def add_pass(id, err):
    os.system('cls')
    print('Add new password here:\n')
    platform=input('Platform name: ')
    password=input('Password: ')
    cursor.execute(f'INSERT INTO all_passwords (user_id, platform, password) values ({id}, "{platform}", "{password}")')
    conn.commit()
    print('Password has been added')
    menuPass(id, err)

#Log out   
def log_out(err):
    menu(err)

#Log in function
def log_in(err):
    os.system('cls')
    print("Log in here:\n")
    print(err)

    email=input('Email: ')
    password=input('Password: ')
    cursor.execute(f'SELECT * From users where email like "{email}"')

    all_users_data=cursor.fetchall()
    if all_users_data!=[] and len(all_users_data)==1:
        for row in all_users_data:
            try:
                if ph.verify(row['password'], password):
                    err=''
                    menuPass(row['user_id'], err)
            except VerifyMismatchError:
                err='Invalid login or password'
                log_in(err)
        
#Register function
def register(err):
    os.system('cls')
    print("Register here:\n")
    print(err)
    email=input('Your email: ')
    password=input('Password: ')
    r_password=input('Repeat password: ')

    if email_verify(email):
        if password==r_password:
            hash_pas=ph.hash(password)
            cursor.execute(f'INSERT INTO users (email, password) values ("{email}", "{hash_pas}")')
            conn.commit()
            err=''
            menu(err)
        else:
            err='The passwords are not the same'
            register(err)
    else:
        err='Account with this email already exist'
        register(err)

#Prevent accounts with the same email
def email_verify(em):
    cursor.execute(f'SELECT * FROM users where email like "{em}"')
    rows=cursor.fetchall()
    return rows==[]

if __name__=='__main__':

    ph = PasswordHasher()
    
    conn = mysql.connector.connect(
        user='root', 
        password='kamil',
        host='localhost',
        database='m28441_passwords_manager'
        )
    cursor=conn.cursor(dictionary=True)


    error=""
    while(True):
        menu(error)




    
    
    
    
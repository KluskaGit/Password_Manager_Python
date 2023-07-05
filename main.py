import mysql.connector
from argon2 import PasswordHasher

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


#Log in function
def log_in():
    login=input('Login: ')
    password=input('Password: ')

#Register function
def register():
    email=input('Your email: ')
    password=input('Password: ')
    r_password=input('Repeat password: ')

    if password==r_password:
        hash_pas=ph.hash(password)
        cursor.execute(f'INSERT INTO users (email, password) values ("{email}", "{hash_pas}")')
        conn.commit()
        log_in()

    

if __name__=='__main__':
    ph = PasswordHasher()
    
    conn = mysql.connector.connect(
        user='root', 
        password='kamil',
        host='localhost',
        database='m28441_passwords_manager'
        )
    cursor=conn.cursor()

    register()
        



    
    
    
    
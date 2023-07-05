import mysql.connector

def menu():
    print("""
    -------MENU-------
    1. Log in
    2. Sign in
    """)

if __name__=='__main__':
    
    conn = mysql.connector.connect(
        user='root', 
        password='kamil',
        host='localhost',
        database='m28441_passwords_manager'
        )
    cursor=conn.cursor()


    while(True):
        choice=input('Option : ')
        

    
    
    
    
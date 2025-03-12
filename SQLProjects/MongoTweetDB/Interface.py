import sqlite3, os, re, random, math
from compose_tweet import compose_tweet
from list_followers import list_all_followers
from search_tweets import search_tweets
from search_users import search_users
from Loginnout import register_user, login, display_tweets

con = None #initialize con
cur = None #initialize cur
usr = None #initialize user id

def clear_screen():
    """
    clear screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def Databaseconnect():
    """ 
    Given a database file path, connect the database
    """
    global con, cur
    while True:
        inp = input("Please provide a path to your database: ")
        try:
            con = sqlite3.connect(inp)
            cur = con.cursor()
            cur.execute('SELECT * FROM users u;')
            print("Connection successful")
            return
        except:
            print("Error connecting to database '" + inp + "', please try again.")

def workflow():
    """
    Main workflow of our program, we use 2 while loop to represent main page and main user page as we need to go back and forth
    """
    
    global usr
    clear_screen()
    while True:
        print("""
------------------------------------
Welcome to CMPUT291 MiniProject #1
Please select from one of the following operations:
L - Login in with your user id and password
R - Register a new account
Q - Quit the program immediately
------------------------------------
          """)
        while True:
            option = input("> ").lower()
            if option in ['r','l','q']:
                break
            else:
                print("""
------------------------------------
 Error: Please enter a valid operations
------------------------------------""")
        if option == 'r':
            clear_screen()
            register_user(con,cur)
    
        elif option == 'q':
            return
    
        elif option == 'l':
            global usr
            while True:
                usr = login(con,cur)
                if usr == '2':
                    break
                elif usr is not None:
                    
                    cur.execute("SELECT name FROM users WHERE usr = ?", (usr,))
                    user_name = cur.fetchall()[0][0]
                    break
            if usr == '2':
                continue
                  
            print(f"""
------------------------------------
Welcome to User Page, {user_name}!
Following are tweets from people you followed
""")
            display_tweets(con,cur,usr)
            while True:
                #clear_screen()
                print("""
------------------------------------
Please select from one of the following operations:
ST - Search for tweets
SU - Search for users
C - Compose a tweet
L - List followers
Q - Logout
------------------------------------
                  """)
            
                while True:
                    option_1 = input("> ").lower()
                    if option_1 in ['st','su','c','l','q']:
                        break
                    else:
                        print("""
------------------------------------
 Error: Please enter a valid operations
 ------------------------------------""")
                if option_1 == 'st':
                    search_tweets(con, cur, usr)
            
                elif option_1 == 'su':
                    search_users(con, cur, usr)
            
                elif option_1 == 'c':
                    compose_tweet(usr, con, cur, rid=None)
            
                elif option_1 == 'l':
                    list_all_followers(usr, con, cur)
            
                elif option_1 == 'q':
                    break

if __name__ =="__main__":
    Databaseconnect()
    workflow()
    
    

import sqlite3
from getpass import getpass
import re,random

def register_user(con, cur):
    """
    register user with name, email, phone number and password. Generate a unique usr id for user
    """
    while True:
        name = input("Enter your name: ").strip()
        if len(name) > 0:
            break
        else:
            print("Name cannot be empty.")
    
    # Input and validate email
    while True:
        email = input("Enter your email: ").strip()
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
        if re.match(email_pattern, email):
            break
        else:
            print("Invalid email format.")
    
    # Input and validate phone number
    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit() and len(phone) in range(10, 15):  # typical phone number length
            break
        else:
            print("Phone number must be numeric and 10-15 digits.")
    
    # Input password with getpass to make it invisible
    while True:
        pwd = getpass("Enter your password: ").strip()
        if len(pwd) >= 6:
            break
        else: 
            print("Please enter at least 6 digits for password")
    
    # Generate a unique user ID
    while True:
        new_userid = random.randint(0, 999999)
        cur.execute("SELECT usr FROM users WHERE usr = ?", (new_userid,))
        if cur.fetchone() is None:  # ID is unique if no record is returned
            break
    
    # Insert the user into the database
    cur.execute('''
        INSERT INTO users (usr, name, email, phone, pwd)
        VALUES (?, ?, ?, ?, ?)
    ''', (new_userid, name, email, phone, pwd))

    con.commit()

    print(f"User registered successfully with ID: {new_userid}")

def login(con, cur):
    """
    user can login in with user id and password or choose to return to main page
    """
    print("\nLogin to your account or press Q to return")

    
    usr = input("Enter your user id: ")
    if usr == 'q' or usr == 'Q':
        return '2'
        
    pwd = getpass("Enter your password: ")

    #validate user id and password
    cur.execute('''
    SELECT * FROM users WHERE usr = ? AND pwd = ?
    ''', (usr, pwd))

    user = cur.fetchone()

    # If user Not found, Ask user to enter again
    # If user is found, return user id as it was important to proceed next operations
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid username or password. Please try again")
        return None


def get_tweets_and_retweets(con, cur, user_id):
    """
    get tweets and retweets information
    """
    
    cur.execute("""
        SELECT tid, writer_id, text, tdate, ttime
        FROM tweets
        WHERE writer_id IN (SELECT flwee FROM follows WHERE flwer = ?)
        
        UNION ALL

        SELECT tid AS tid, retweeter_id AS writer_id, 
               (SELECT text FROM tweets WHERE tid = retweets.tid) AS text,
               rdate AS tdate, 'retweet' AS ttime
        FROM retweets
        WHERE retweeter_id IN (SELECT flwee FROM follows WHERE flwer = ?)
        
        ORDER BY tdate DESC, ttime DESC
    """,(user_id,user_id))

    return cur.fetchall()

def display_tweets(con, cur, user_id):
    """
    After getting tweets and retweets, display them 5 at a time
    """
    posts = get_tweets_and_retweets(con, cur, user_id)

    # print message when no tweets or retweets are found
    if not posts:
        print("No tweets or retweets found.")
        return

    # print tweets 5 at a time, user can choose to see next 5 tweets or proceed to main user page
    start = 0
    while True:
        end = min(start + 5, len(posts))
        for post in posts[start:end]:
            if len(post) == 5:
                print(f"Tweet ID: {post[0]} | Writer ID: {post[1]} | {post[2]} | Date: {post[3]} Time: {post[4]}")
                
        if end < len(posts):
            action = input("\nPress 'y' to show next 5 tweets or Press Enter to proceed to main menu\n> ").strip().lower()
            if action != 'y':
                break
            start = end
        else:
            break

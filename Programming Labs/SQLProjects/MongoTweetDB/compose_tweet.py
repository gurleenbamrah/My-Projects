import sqlite3
from datetime import date,datetime

def creates_tid(cursor) -> int:  #gets a new tweet id 
    
    cursor.execute("SELECT MAX(tid) FROM tweets;")
    tid = cursor.fetchone() 

    #gets max tid from tweets table and increments by 1 so its unique 
    if tid is None or tid[0] is None:  #if no tweets then return 1 as its the first tweets id 
        return 1
    else:
        return tid[0] + 1


def insert_tweet(cursor, tid, writer_id, text, tdate, ttime,replyto_tid=None): # inserts new weets into table 

    cursor.execute(''' INSERT INTO tweets (tid, writer_id, tdate, ttime, text, replyto_tid) VALUES (?, ?, ?, ?, ?, ?); ''', (tid, writer_id, tdate, ttime, text, replyto_tid))


def insert_mentions(tid, hashtag, cursor): #inserts mentions (hashtag) associated with a specific tweet 

    cursor.execute(''' INSERT INTO hashtag_mentions (tid, term) VALUES (?, ?); ''', (tid, hashtag))


def compose_tweet(uid, connection, cursor, rid=None):

    tid = creates_tid(cursor) #stores tid 
    tweet_date = date.today() #gets todays date 
    hashtags = set() #creates set to store hastags so no duplicates 
    tweet = input("Enter text: ") #input the tweet 
    words = tweet.split() #splits tweet into words so we can find hashtags 
    ttime = datetime.now().strftime('%H:%M:%S')
    
    for word in words:
        if word.startswith("#") and len(word) > 1: #gets words starting with # and ensures that hastags are at least 2 character long
            hashtags.add(word) #adds hashtag

    insert_tweet(cursor, tid, uid, tweet, tweet_date, ttime,rid) #inserts tweet into table  

    for hashtag in hashtags:
        insert_mentions(tid, hashtag, cursor) #inserts hashtags into hashtag table 

    connection.commit()

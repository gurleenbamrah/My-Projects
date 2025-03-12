import sqlite3
from datetime import date


def follow_user(uid, connection, cursor, flwer_id): #inserts follow into the follows table 

    cursor.execute('''INSERT INTO follows(flwer, flwee, start_date) VALUES (?, ?, ?);''', (uid, flwer_id, date.today()))
    connection.commit() #commit changes to database 
    print(f"You are now following {flwer_id}!")


def view_follower_tweets(uid, connection, cursor, flwer_id): # displays tweets of follower
    
    #gets all tweets by follower ordered by date and time 
    cursor.execute('''SELECT text, tdate, ttime FROM tweets WHERE writer_id = ? ORDER BY tdate DESC, ttime DESC;''', (flwer_id, ))
    tweets = cursor.fetchall()

    if tweets:
        print("\nTweets: ")
        for tweet in tweets:
            text, tdate, ttime = tweet
            print(f"{tdate} {ttime} - {text}")
    else:
        print("No tweets found ")

    input("\nPress Enter to go back to the follower details.")
    view_details(uid, connection, cursor, flwer_id)


def list_all_followers(uid, connection, cursor): #lists followers showing 5 at a time 

    #gets all followers of the user from follows table 
    cursor.execute('''SELECT f.flwer, u.name, u.email FROM follows f JOIN users u ON f.flwer = u.usr WHERE f.flwee = ?;''', (uid, ))
    followers = cursor.fetchall() #fetches all followers

    if not followers: #if no followers are found in the list 
        print("No followers found.")
        return

    total_followers = len(followers) #total number of followers 
    start = 0 #index to display first 5 followers 

    while start < total_followers:
        print(f"\nFollowers (Displaying {start + 1} to {min(start + 5, total_followers)}): ")

        #displays current 5 followers
        for i in range(start, min(start + 5, total_followers)):
            flwer_id, name, email = followers[i]
            print(f"{i+1}. {name} ({email})")

        #if more followers exist after this first 5 ask the user to see more or quit 
    
        user_option = input("\nEnter 'm' to see more followers, or 'q' to quit, or the number of the follower you want to select: ").strip().lower()
        if user_option == 'm':
            start += 5
            if start > total_followers:
                print("No more folllowers.")
                start -= 5
        elif user_option == 'q':
            return
        else:
            try:

                follower_index = int(user_option) - 1 #gets correct index of follower like if first follower is index 0 we need to minus 1 from the input 
                if 0 <= follower_index < len(followers):
                    flwer_id = followers[follower_index][0]
                    view_details(uid, connection, cursor, flwer_id) #passes correct follower id to view details 
                else:
                    print("Invalid number")
            except ValueError:
                print("Invalid input")


def view_details(uid, connection, cursor, flwer_id):


    #gets followers info from database
    cursor.execute("SELECT name, email, phone FROM users WHERE usr = ?", (flwer_id, ))
    follower_info = cursor.fetchone() #returns first row of query

    if follower_info: #if info found
        name, email, phone = follower_info
        print(f"\nFollower Details:\nName: {name}\nEmail: {email}\nPhone: {phone}")

        #gets number of tweets from follower
        cursor.execute("SELECT COUNT(*) FROM tweets WHERE writer_id = ?", (flwer_id, ))
        num_tweets = cursor.fetchone()[0]

        #gets number of users the follower is following
        cursor.execute("SELECT COUNT(*) FROM follows WHERE flwee = ?", (flwer_id, ))
        num_following = cursor.fetchone()[0]

        #gets number of followers that this follower has
        cursor.execute("SELECT COUNT(*) FROM follows WHERE flwee = ?", (flwer_id, ))
        num_followers = cursor.fetchone()[0]

        print(f"Number of Tweets: {num_tweets}")
        print(f"Number of Following: {num_following}")
        print(f"Number of Followers: {num_followers}")

        #gets the 3 most recent tweets of the follower
        cursor.execute('''SELECT text, tdate, ttime FROM tweets WHERE writer_id = ? ORDER BY tdate DESC, ttime DESC LIMIT 3; ''', (flwer_id))
        tweets = cursor.fetchall() #gets most recent tweets

        #prints the tweets
        if tweets:
            print("\nRecent Tweets: ")
            for tweet in tweets:
                text, tdate, ttime = tweet
                print(f"{tdate} {ttime} - {text}") #prints tweet with date and time 
        else:
            print("No recent tweets found.")

        #asks user if they want to follow the use, see more tweets, or go back to main
        option = input("\nWould you like to follow this user (f), or see more tweets (t), or go back to main page (b)? ").strip().lower()

        if option == 'f':
            follow_user(uid, connection, cursor, flwer_id) #if user wants to follow 
        elif option == 't':
            view_follower_tweets(uid, connection, cursor, flwer_id) #if user wants to see more tweets
        elif option == 'b':
            list_all_followers(uid, connection, cursor) #if user wants to go back
        else:
            view_details(uid, connection, cursor, flwer_id) #if anything else then the prompt comes up again 





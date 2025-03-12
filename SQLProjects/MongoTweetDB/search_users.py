from datetime import date   
import sqlite3, math

def check_string_len(string, max_len=300):
    # checks to make sure string isn't extremely long
    return len(string) <= max_len

def follow_user(con, cur, usr, flwee):
    # executes a follow request for a chosen user
    try:
        cur.execute("INSERT into follows values (?,?,?);", (str(usr), str(flwee), str(date.today())))
        # usr as the follower, flwee is the user information we are checking and they are the objective 
        con.commit()
        # submit it to the database and permanent store it 
        print("User {} has been followed.".format(flwee))
        print()
    except sqlite3.IntegrityError:
        print("User has already been followed. Returning to previous page.")
        print()

def display_tweets(con, cur, usr, flwee):
    # retrieves user information and the tweets of a chosen user
    # Set teh tweets query to store all tweets in the time descending order  
    tweet_query = """
    select *
    from tweets t
    where t.writer_id == ?
    order by DATE(t.tdate) desc;
    """
    # The user query store the user name, the number of followers, followees, and tweets 
    # each ? is a params in the params tuple
    user_query = """
    select u.name, following, followers, tweet_count
    from users u, 
    (
        select count(u.usr) as following
        from follows f, users u
        where u.usr = ? AND u.usr = f.flwer
    ),
    (
        select count(u.usr) as followers
        from follows f, users u
        where u.usr = ? and u.usr = f.flwee
    ),
    (
        select count(t.tid) as tweet_count
        from users u, tweets t
        where u.usr = ? AND u.usr = t.writer_id AND t.replyto_tid IS NULL
    )
    where u.usr = ?;
    """

    # execute queries to retrieve information
    tweet_page = 0  #initialize the page for tweets
    viewed_user = flwee # flwee is the user that we are checking now 
    params = [str(viewed_user), str(viewed_user), str(viewed_user), str(viewed_user)] 
    # since we need 4 information about the user, so we need 4 different params
    params = tuple(params)
    cur.execute(user_query, params) # to process all result 
    user_info = cur.fetchall()[0] # get the first result tuple for the opration 
    
    # get the exact text and time for the tweets belong to the user we choose 
    val = [str(viewed_user)]
    val = tuple(val)
    cur.execute(tweet_query, val)
    tweet_query = cur.fetchall() # return all the result tuples for the operation 
    total_pages = math.ceil(len(tweet_query)/3) # calculate the page number 

    # display all queried information
    while True:
        print("User information:")
        # <(int) is to justify our output text to the left 
        print ("{:<3} {:<5} {:<15} {:<10} {:<10} {:<8}".
            format('', 'UID', 'Name','Followers','Following','Tweets'))
        print ("{:<3} {:<5} {:<15} {:<10} {:<10} {:<8}".
            format('', str(viewed_user), user_info[0],user_info[1],user_info[2],user_info[3]))
        print()
        # Get only the 3 tweets on this page
        tweet_query_3 = tweet_query[3*tweet_page:3*tweet_page+3]
        # if tweet_page = 0, then the tweets from index 0 to 3
        # if tweet_pae  = 1, then the tweets from 1 * 3 to 1 * 3 + 3
        # ...
        i = 0
        print ("{:<3} {:<8} {:<8} {:<20} {:<10}".
                format(' ', '  TID',' User','   Date','  Text'))
        for tweet in tweet_query_3:
            print ("{:<3} {:<8} {:<8} {:<20} {:<10}".
                format(f"NO.{i+1} -", tweet[0], tweet[1], tweet[2], tweet[3]))
            i += 1
        print("{:<44}{}".format('', "Page({}/{})".format(
            tweet_page+1, max(total_pages,1))))
        
        # menu for choosing options
        print("""(</>) - Previous/Next, "Q" to return to search page. To follow this user, select 'F'.
    ---------------------------------
            """)
        inp = input("> ").lower().strip()
        print()
        if inp == 'f':
            follow_user(con, cur, usr, str(viewed_user))
        elif inp == '<':
            tweet_page=max(tweet_page-1, 0)
        elif inp == '>':
            tweet_page=min(tweet_page+1, total_pages-1)
        elif inp == "q":
            return
        
def display_users(con, cur, usr, user_match):
    if not user_match:  # if no result 
        print("Did not find any user, please try another keyword.")
        return    
    
    # Displays all given users
    total_pages = math.ceil(len(user_match)/5)
    tweet_page = 0
    while True:
        print("User Search Results:")
        print ("{:<8} {:<15} ".
            format('UID','Name'))
        # Get only the 5 users on this page
        user_match_5 = user_match[5*tweet_page:5*tweet_page+5]
        i = 0
        for user in user_match_5:
            print ("{:<8} {:<15} ".
                format( user[0], user[1]))
            i += 1
        print("{:<44}{}".format('', "Page({}/{})".format(
            tweet_page+1, max(total_pages,1))))
        
        print("""(</>) - Previous/Next, "Q" to return to search.
                
    Type the UID to get more information about the user you want to know.
    ---------------------------------
            """)
        inp = input("> ").lower().strip()
        print()
        if inp == '<':
            tweet_page=max(tweet_page-1, 0)
        elif inp == '>':
            tweet_page=min(tweet_page+1, total_pages-1)
        elif inp == "q":
            return        
        else:
            valid_id = False
            for user in user_match:
                if user[0] == int(inp):
                    flwee = inp
                    display_tweets(con, cur, usr, flwee)
                    valid_id = True
            if not valid_id:
                print("Invalid UID, please try again.")

percentage_str= "%"

def order_data(name_users):
    # orders the data as given, first within their catagories, and then splices
    # list together for overall search result
    user_list = []

    #order the data by ascending name/city lengths
    name_users.sort(key=lambda result: len(result[1]))
    
    return name_users

def process_keyword(input):
    # processes keyword and ensures that keyword is valid
    if len(input) == 0:
        print("Error: Keyword cannot be empty.")
        return False
    elif input.isalnum() != True:
        print("Error: Keywords must be alphanumeric.")
        return False
    elif not check_string_len(input):
        print("Error: Keywords must be less than 300 characters.")
        return False
    return True

def search_users(con, cur, usr):
    '''
     Search for users: 
     
     Requirement 1:
         The user should be able to enter a keyword and the system should retrieve all users whose names contain the keyword. 
         A keyword can be interpreted as a sequence of alphanumeric characters. 
         The search query DOES NOT need to match the username exactly. 
         For example, if you search "foy", it should show results: Foy, Malfoy. 
     
     Requirement 2:
         The outputs should display both the user id and the user name so that users with same names can be distinguished.  
         The result would be sorted in an ascending order of name length. 
         If there are more than 5 matching users, only 5 would be shown and the user would be given an option to see more but again 5 at a time. 
     
     Requirement 3:
         The user should be able to select a user and see more information about the user including the number of tweets, 
         the number of users being followed by the user, the number of followers, 
         and up to 3 most recent tweets. The user should be given the option to follow the user or see more tweets.
    
    Tutorial for using the sqlite3 python standard library: https://docs.python.org/3/library/sqlite3.html
    
    Parameters:
        con: (sqlite3.connection) Use con.commit() to save database changes. See above link for more.
        cur: (sqlite3.cursor) Use curr.execute("SELECT * FROM ...") to conduct queries. See above link for more.
        usr: (int) Primary key for currently signed-in user. 
    
    Return: Upon the termination of this function, the main hub menu will be shown again, 
        where the user may choose their next action (e.g., log out, search tweets...).
    '''
    print("------Searching Users------")
    while True:    
        print("Type in keyword to search with. Type 'Q' to exit search.")
        # process keyword input
        inp = input("> ")
        print()
        
        if len(inp) == 0:
            print("Please input keyword or 'q'")
        elif inp.lower() == "q":
            return
        else:
            #process and check for valid input
            inp = inp.strip()
            good_input = process_keyword(inp)
            if good_input == False:
                print("Error on processing keyword. Returning to main menu.")
                return
            
            #prepare query for users
            params = []
            value = percentage_str + inp + percentage_str
            params.append(value)
            params = tuple(params)
            name_query = """
            select u.usr, u.name
            from users u
            where u.name LIKE LOWER(?);
            """
            cur.execute(name_query, params)
            name_users = cur.fetchall()
            user_list = order_data(name_users)
            display_users(con, cur, usr, user_list)

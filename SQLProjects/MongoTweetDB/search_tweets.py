from datetime import date, datetime
import sqlite3, math
from compose_tweet import compose_tweet

def check_string_len(string, max_len=300):
    return len(string) <= max_len

def display_tweet_stats(con, cur, tid):
    # Get the number of retweets and replies for a specific tweet
    cur.execute("SELECT COUNT(*) FROM retweets WHERE tid = ?", (tid,))
    retweet_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM tweets WHERE replyto_tid = ?", (tid,))
    reply_count = cur.fetchone()[0]

    print(f"Retweets: {retweet_count}, Replies: {reply_count}")
    print()

def search_tweets(con, cur, usr):
    print("------Searching Tweets------")
    
    while True:
        inp = input("Enter keywords to search (or 'Q' to quit): ").strip()
        if inp.lower() == 'q':
            return
        
        keywords = inp.split()
        keyword_conditions = []
        params = []

        for keyword in keywords:
            if keyword.startswith("#"):
                keyword_conditions.append("LOWER(ht.term) = ?")
                params.append(keyword[0:].lower())
            else:
                keyword_conditions.append("LOWER(t.text) LIKE ?")
                params.append(f"%{keyword.lower()}%")
        
        where_clause = " OR ".join(keyword_conditions)
        query = f"""
        SELECT t.tid, t.writer_id, t.text, t.tdate
        FROM tweets t
        LEFT JOIN hashtag_mentions ht ON t.tid = ht.tid
        WHERE {where_clause}
        ORDER BY t.tdate DESC;
        """
        
        cur.execute(query, tuple(params))
        tweets = cur.fetchall()
        
        # Check if no tweets were found and display a message
        if not tweets:
            print("No tweets found with the given keywords.")
            continue
        
        total_pages = math.ceil(len(tweets) / 5)
        page = 0

        while True:
            tweets_page = tweets[page * 5: (page + 1) * 5]
            
            print("\nTweets:")
            for idx, tweet in enumerate(tweets_page, start=1):
                tid, writer_id, text, tdate = tweet
                print(f"{idx}. TID: {tid}, Writer ID: {writer_id}, Date: {tdate}, Text: {text[:50]}...")
            
            print(f"Page {page + 1} of {total_pages}")
            inp = input("(</>) - Previous/Next, 'Q' to quit, 'S' for stats, 'R' to reply, 'RT' to retweet, or tweet number to interact: ").strip().lower()

            if inp == '<':
                page = max(page - 1, 0)
            elif inp == '>':
                page = min(page + 1, total_pages - 1)
            elif inp == 'q':
                return
            elif inp == 's':
                try:
                    tweet_index = int(input("Enter tweet number for stats: ")) - 1
                    if 0 <= tweet_index < len(tweets_page):
                        display_tweet_stats(con, cur, tweets_page[tweet_index][0])
                    else:
                        print("Invalid tweet number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif inp == 'r':
                try:
                    tweet_index = int(input("Enter tweet number to reply: ")) - 1
                    if 0 <= tweet_index < len(tweets_page):
                        selected_tid = tweets_page[tweet_index][0]
                        compose_tweet(usr, con, cur, selected_tid)
                        print("Reply posted successfully.")
                    else:
                        print("Invalid tweet number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif inp == 'rt':
                try:
                    tweet_index = int(input("Enter tweet number to retweet: ")) - 1
                    if 0 <= tweet_index < len(tweets_page):
                        selected_tid = tweets_page[tweet_index][0]
                        cur.execute(
                            "INSERT INTO retweets (tid, retweeter_id, writer_id, spam, rdate) VALUES (?, ?, ?, ?, ?)",
                            (selected_tid, usr, tweets_page[tweet_index][1], 0, date.today())
                        )
                        con.commit()
                        print("Retweet posted successfully.")
                    else:
                        print("Invalid tweet number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                try:
                    tweet_index = int(inp) - 1
                    if 0 <= tweet_index < len(tweets_page):
                        selected_tid = tweets_page[tweet_index][0]
                        print(f"Selected Tweet ID: {selected_tid}")
                        # Additional interaction, such as liking, can be implemented here.
                    else:
                        print("Invalid tweet number.")
                except ValueError:
                    print("Invalid input. Please try again.")


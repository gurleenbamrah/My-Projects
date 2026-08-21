WITH ListTweet AS (
    SELECT l.owner, l.lname, COUNT(*) AS total_tweets, COUNT(r.retweeter) AS retweeted_tweets
    FROM lists l
    JOIN includes i ON l.owner = i.owner AND l.lname = i.lname
    JOIN tweets t ON i.writer = t.writer AND i.tdate = t.tdate AND i.ttime = t.ttime
    LEFT JOIN retweets r ON t.writer = r.writer AND t.tdate = r.tdate AND t.ttime = r.ttime
    GROUP BY l.owner, l.lname
)
SELECT owner, lname
FROM ListTweet
WHERE total_tweets > 3
AND retweeted_tweets * 2 >= total_tweets;  



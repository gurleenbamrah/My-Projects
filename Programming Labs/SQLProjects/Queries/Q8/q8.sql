WITH counting_tweets AS (
    SELECT strftime('%m', tdate) AS month_number, COUNT(*) - COUNT(replyto_w) AS tweet_count, COUNT(replyto_w) AS reply_count  
    FROM tweets
    WHERE strftime('%Y', tdate) = '2024'
    GROUP BY month_number
),
counting_retweet AS (
    SELECT strftime('%m', rdate) AS month_number, COUNT(*) AS retweet_count  
    FROM retweets
    WHERE strftime('%Y', rdate) = '2024'
    GROUP BY month_number
)
SELECT ct.month_number, ct.tweet_count, ct.reply_count, COALESCE(cr.retweet_count, 0) AS retweet_count, (ct.tweet_count + ct.reply_count + COALESCE(cr.retweet_count, 0)) AS total
FROM counting_tweets ct
LEFT JOIN counting_retweet cr ON ct.month_number = cr.month_number
ORDER BY ct.month_number;

















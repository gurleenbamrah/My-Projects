SELECT t.writer, t.tdate, t.ttime, t.text
FROM tweets t
JOIN retweets r ON t.writer = r.writer 
JOIN follows f ON f.flwer = r.retweeter
AND t.tdate = r.tdate
AND t.ttime = r.ttime
AND f.flwee = t.writer
GROUP BY t.writer, t.tdate, t.ttime, t.text
HAVING COUNT(DISTINCT r.retweeter) >= 3;

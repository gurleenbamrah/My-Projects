SELECT writer, tdate, ttime, text
FROM (
    SELECT t.writer,t.tdate,t.ttime,t.text, RANK() OVER (ORDER BY COUNT(r.retweeter) DESC) AS ranking
    FROM tweets t
    JOIN retweets r ON t.writer = r.writer 
      AND t.tdate = r.tdate 
      AND t.ttime = r.ttime
    GROUP BY t.writer, t.tdate, t.ttime, t.text
)
WHERE ranking <= 3;





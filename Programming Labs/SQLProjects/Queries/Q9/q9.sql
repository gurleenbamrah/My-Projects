CREATE VIEW tStat AS
SELECT t.writer, t.tdate, t.ttime, t.text,
    (SELECT COUNT(*) 
     FROM tweets t2 
     WHERE t2.replyto_w = t.writer 
     AND t2.replyto_d = t.tdate 
     AND t2.replyto_t = t.ttime) AS counting_replies,
    
    (SELECT COUNT(*) 
     FROM retweets r 
     WHERE r.writer = t.writer 
     AND r.tdate = t.tdate 
     AND r.ttime = t.ttime) AS counting_retweets,
   
    (SELECT COUNT(*) 
     FROM tweets t3 
     WHERE t3.mention_has = t.mention_has 
     AND t3.mention_has IS NOT NULL) AS similar_hashtags
    
FROM tweets AS t;

SELECT * FROM tStat;







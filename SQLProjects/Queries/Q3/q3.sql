SELECT t1.writer 
FROM tweets t1, tweets t2, tweets t3
WHERE t1.writer = t2.writer
AND t1.writer = t3.writer
AND (t1.text != t2.text OR t1.tdate != t2.tdate)
AND (t2.text != t3.text OR t2.tdate != t3.tdate)
AND LOWER(t1.text) LIKE '%edmonton%'
AND LOWER(t2.text) LIKE '%edmonton%'
AND LOWER(t3.text) LIKE '%edmonton%'

EXCEPT 

SELECT f.flwee
FROM follows f;

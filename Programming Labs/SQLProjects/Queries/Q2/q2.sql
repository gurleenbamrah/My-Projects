SELECT DISTINCT f1.flwer
FROM follows f1
JOIN users u1 ON f1.flwer = u1.usr
JOIN follows f2 ON f1.flwee = f2.flwee
JOIN users u2 ON f2.flwer = u2.usr
WHERE julianday('now') - julianday(f1.start_date) >= 90
AND LOWER(u2.name) = 'john doe'
AND julianday('now') - julianday(f2.start_date) < 90;

SELECT u1.usr, u1.name
FROM users u1
LEFT JOIN tweets t ON u1.usr = t.writer
WHERE t.writer IS NULL
AND NOT EXISTS (
  SELECT f1.flwee
  FROM follows f1
  JOIN users u2 ON f1.flwer = u2.usr
  WHERE LOWER(u2.name) = 'john doe'

  EXCEPT
  SELECT f2.flwee
  FROM follows f2
  WHERE f2.flwer = u1.usr
);

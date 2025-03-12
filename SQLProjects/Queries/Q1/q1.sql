SELECT DISTINCT u.usr
FROM users u
JOIN follows f ON u.usr = f.flwee
JOIN includes i ON u.usr = i.writer;

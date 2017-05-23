-- Solution to codewars kata https://www.codewars.com/kata/sql-basics-group-by-day/

SELECT  created_at::date as day, description, count(name)
FROM    events
WHERE   name = 'trained'
GROUP BY day, description
ORDER BY day

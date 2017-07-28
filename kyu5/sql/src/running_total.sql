-- Solution to codewars kata http://www.codewars.com/kata/calculating-running-total/

WITH cte AS (SELECT created_at::date as date FROM posts)

SELECT date, count(date), SUM(count(date)) OVER (ORDER BY date)::integer as total
FROM cte
GROUP BY date;

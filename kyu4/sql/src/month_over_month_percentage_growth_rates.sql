-- Solution to codewars kata https://www.codewars.com/kata/calculating-month-over-month-percentage-growth-rate

WITH cte AS (SELECT created_at::date as date FROM posts)

SELECT date, count(date), lag(count(*), 1) OVER (ORDER BY date)
FROM cte
GROUP BY date;

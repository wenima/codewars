-- Solution to codewars kata https://www.codewars.com/kata/calculating-month-over-month-percentage-growth-rate

WITH cte AS (SELECT created_at::date as date FROM posts)

SELECT date, count(date),
100 * (count(*) - lag(count(*), 1) OVER (ORDER BY date)) / lag(count(*), 1) OVER (ORDER BY date) || '%' as percent_growth
FROM cte
GROUP BY date;

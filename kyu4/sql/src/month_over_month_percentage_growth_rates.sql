-- Solution to codewars kata https://www.codewars.com/kata/calculating-month-over-month-percentage-growth-rate
-- SQL Flavor: Postgres 9.6

WITH cte AS (SELECT date_trunc('month', created_at)::date as date FROM posts)

SELECT date, count(date),
ROUND(100 * (count(*) - lag(count(*), 1) OVER (ORDER BY date)) / lag(count(*), 1) OVER (ORDER BY date)::numeric,1) || '%' as percent_growth
FROM cte
GROUP BY date;

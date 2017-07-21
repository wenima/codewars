-- Solution to codewars kata http://www.codewars.com/kata/calculating-running-total/

WITH CTE AS (SELECT created_at::date as date FROM posts)

select date, count(date)
from cte
group by date;

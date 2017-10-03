--Solution for https://www.codewars.com/kata/sqlonacci-sequence/

WITH RECURSIVE fib(number,n2) AS (
      SELECT 0::bigint,1::bigint
    UNION ALL
      SELECT n2::bigint,number+n2::bigint
      FROM fib
)
SELECT number FROM fib LIMIT 90

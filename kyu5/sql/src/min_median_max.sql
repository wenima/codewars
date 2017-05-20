-- Solution to codewars kata https://www.codewars.com/kata/sql-statistics-min-median-max/

SELECT
  MIN(score),
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY score)::numeric, 2)::float as median,
  MAX(score)
FROM result;

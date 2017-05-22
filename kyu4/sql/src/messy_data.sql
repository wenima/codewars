-- Solution to codewars kata https://www.codewars.com/kata/dealing-with-messy-data/

CREATE EXTENSION pg_trgm;

CREATE INDEX prospects_idx ON prospects USING GIN(full_name gin_trgm_ops);

SELECT
  c.first_name,
  c.last_name,
  c.credit_limit AS "old_limit",
  max(p.credit_limit) AS "new_limit"
FROM customers c, prospects p
WHERE lower(p.full_name) LIKE '%' || lower(c.first_name) || '%'
AND lower(p.full_name) LIKE '%' || lower(c.last_name) || '%'
AND p.credit_limit > c.credit_limit
GROUP BY c.first_name, c.last_name, c.credit_limit
ORDER BY first_name;

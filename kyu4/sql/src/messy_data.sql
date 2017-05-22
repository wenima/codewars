-- Solution to codewars kata https://www.codewars.com/kata/dealing-with-messy-data/

CREATE EXTENSION pg_trgm;

CREATE INDEX prospects_idx ON prospects USING GIN(full_name gin_trgm_ops);

WITH higher_limits (id, first_name, last_name, old_limit, new_limit)
AS (
  SELECT c.id, c.first_name, c.last_name,
    c.credit_limit AS "old_limit",
    p.credit_limit AS "new_limit"
    FROM customers c, prospects p
    WHERE lower(p.full_name) LIKE '%' || lower(c.first_name) || '%'
    AND lower(p.full_name) LIKE '%' || lower(c.last_name) || '%'
    AND p.credit_limit > c.credit_limit
  )

SELECT c.first_name, c.last_name, h.old_limit, max(h.new_limit) AS new_limit
FROM higher_limits h, customers c
WHERE h.id = c.id
GROUP BY c.first_name, c.last_name, h.old_limit
ORDER BY first_name;

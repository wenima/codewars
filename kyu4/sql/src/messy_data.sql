-- Solution to codewars kata https://www.codewars.com/kata/dealing-with-messy-data/

-- working but includes lower credit limits than max as well
CREATE EXTENSION pg_trgm;

CREATE INDEX prospects_idx ON prospects USING GIN(full_name gin_trgm_ops);

SELECT distinct c.id, c.first_name, c.last_name, c.credit_limit AS "old_limit",
                p.credit_limit AS "new_limit"
FROM customers c, prospects p
WHERE lower(p.full_name) LIKE '%' || lower(c.first_name) || ' ' || lower(c.last_name) || '%'
AND p.credit_limit > c.credit_limit;

-- Solution to codewars kata https://www.codewars.com/kata/dealing-with-messy-data/

-- working but includes lower credit limits than max as well
CREATE EXTENSION pg_trgm;

CREATE INDEX prospects_idx ON prospects USING GIN(full_name gin_trgm_ops);

SELECT distinct c.id, c.first_name, c.last_name, c.credit_limit AS "old_limit",
                max(p.credit_limit) AS "new_limit"
FROM customers c, prospects p
WHERE lower(p.full_name) LIKE '%' || lower(c.first_name) || ' ' || lower(c.last_name) || '%'
AND p.credit_limit > c.credit_limit;

-- not showing the max values for some cases and missing records
WITH higher_limits (id, first_name, last_name, old_limit, new_limit)
AS
(SELECT distinct c.id, c.first_name, c.last_name, c.credit_limit as "old_limit",
p.credit_limit as "new_limit"
FROM customers c, prospects p
where lower(p.full_name) like '%' || lower(c.first_name) || ' ' || lower(c.last_name) || '%'
and p.credit_limit > c.credit_limit)

select c.id, c.first_name, c.last_name, h.old_limit, max(h.new_limit) as new_limit
from higher_limits h, customers c
where h.id = c.id
group by c.id, c.first_name, c.last_name, h.old_limit
order by first_name;

--trying to split the like search in 2
WITH higher_limits (id, first_name, last_name, old_limit, new_limit)
AS
(SELECT distinct c.id, c.first_name, c.last_name, c.credit_limit as "old_limit",
p.credit_limit as "new_limit"
FROM customers c, prospects p
where lower(p.full_name) like '%' || lower(c.first_name) || '%'
and lower(p.full_name) like '%' || lower(c.last_name) || '%'
and p.credit_limit > c.credit_limit)

select c.id, c.first_name, c.last_name, h.old_limit, max(h.new_limit) as new_limit
from higher_limits h, customers c
where h.id = c.id
group by c.id, c.first_name, c.last_name, h.old_limit
order by first_name;

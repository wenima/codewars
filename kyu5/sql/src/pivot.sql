-- Solution for kata https://www.codewars.com/kata/sql-basics-simple-pivoting-data/sql

CREATE EXTENSION tablefunc;

CREATE TEMP TABLE product_details (
  name text,
  detail text,
  ct integer
);

INSERT INTO product_details
SELECT p.name, d.detail, count(d.detail) as ct
FROM products p, details d
WHERE p.id = d.product_id
GROUP BY p.name, d.detail;

SELECT *
FROM crosstab(
  'SELECT name, detail, ct
  FROM product_details
  ORDER BY 1,2'
  ,$$VALUES ('good'::text), ('ok'::text), ('bad'::text)$$)
AS ct("name" text, "good" int, "ok" int, "bad" int);


-- most upvoted

CREATE EXTENSION tablefunc;

SELECT *
FROM  crosstab(
      'SELECT p.name, detail, COUNT(d.id)
      FROM products p
      JOIN details d
      ON p.id = d.product_id
      GROUP BY p.name, d.detail
      ORDER BY 1,2')
AS ct (name text, bad bigint, good bigint, ok bigint)

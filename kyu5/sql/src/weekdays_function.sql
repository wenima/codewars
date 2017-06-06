-- Submitted solution for https://www.codewars.com/kata/count-weekdays/
CREATE OR REPLACE FUNCTION weekdays (date, date) RETURNS Integer
  AS 'WITH weekdays AS (
  SELECT count(*)
  FROM generate_series(0, ($1::date - $2::date::date)) i
  WHERE date_part(''dow'', $2::date::date + i) NOT IN (0,6)

  UNION

  SELECT count(*)
  FROM generate_series(0, ($2::date - $1::date::date)) i
  WHERE date_part(''dow'', $1::date::date + i) NOT IN (0,6))

  SELECT max(count)::int from weekdays;'
  LANGUAGE SQL
  IMMUTABLE;

--Solution doing manual variable switching
CREATE OR REPLACE FUNCTION weekdays (date, date) RETURNS INTEGER AS $$
DECLARE
  d1 date;
  d2 date;
  days int;
BEGIN
  IF $1 > $2 THEN
    d1 := $1;
    d2 := $2;
  ELSE
    d1 := $2;
    d2 := $1;
  END IF;

  RETURN SELECT count(weekdays)
  FROM generate_series(0, (d1::date - d2::date::date)) i
  WHERE date_part('dow', d2::date::date + i) NOT IN (0,6);
END;
$$
LANGUAGE plpgsql;

--better solution using least/greatest and extract instead of date_part
CREATE FUNCTION weekdays(DATE, DATE)
RETURNS INTEGER
LANGUAGE sql AS
$$
  SELECT COUNT(days)::int
  FROM generate_series(LEAST($1, $2), GREATEST($1, $2), '1 day') as days
  WHERE EXTRACT(DOW FROM days) NOT IN(0, 6);
$$;

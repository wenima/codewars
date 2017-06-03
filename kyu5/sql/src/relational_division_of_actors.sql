-- Solution to codewars kata https://www.codewars.com/kata/relational-division-find-all-movies-two-actors-cast-in-together/sql

SELECT F.title
FROM
  (SELECT FA.film_id
  FROM film_actor FA
  WHERE FA.actor_id=105
  INTERSECT
  SELECT FA.film_id
  FROM film_actor FA
  WHERE FA.actor_id=122) R, film F
WHERE F.film_id=R.film_id
ORDER BY title

-- Solution to codewars kata http://www.codewars.com/kata/challenge-two-actors-who-cast-together-the-most

-- get fist and second actor co-starring the most together
SELECT tp.actor_id, fa.actor_id as costar, count(fa.actor_id) as starts
FROM film_actor fa, film_actor tp
WHERE fa.film_id = tp.film_id
AND fa.actor_id <> tp.actor_id
GROUP BY tp.actor_id, fa.actor_id
order by starts DESC, tp.actor_id;


-- get top entry and map to actor names
WITH top_team (actor1, actor2, starts)
AS
(
  SELECT tp.actor_id, fa.actor_id as costar, count(fa.actor_id) as starts
  FROM film_actor fa, film_actor tp
  WHERE fa.film_id = tp.film_id
  AND fa.actor_id <> tp.actor_id
  GROUP BY tp.actor_id, fa.actor_id
  ORDER BY starts DESC, tp.actor_id
  LIMIT 1
)

SELECT a1.first_name||' '||a1.last_name AS "first_actor",
      a2.first_name||' '||a2.last_name AS "second_actor", tt.starts
FROM actor a1, actor a2, top_team tt
WHERE tt.actor1 = a1.actor_id
AND tt.actor2 = a2.actor_id;

-- join in film table to get all titles
WITH top_team (actor1, actor2, starts)
AS
(
  select tp.actor_id, fa.actor_id as costar, count(fa.actor_id) as starts
  from film_actor fa, film_actor tp
  WHERE fa.film_id = tp.film_id
  AND fa.actor_id <> tp.actor_id
  GROUP BY tp.actor_id, fa.actor_id
  order by starts DESC, tp.actor_id
  LIMIT 1
)

SELECT a1.first_name||' '||a1.last_name as "first_actor",
      a2.first_name||' '||a2.last_name as "second_actor",
      f.title
FROM actor a1, actor a2, top_team tt, film f
WHERE tt.actor1 = a1.actor_id
AND tt.actor2 = a2.actor_id
AND f.film_id IN (
    select fa1.film_id from film_actor fa1, film_actor fa2
    where fa1.film_id = fa2.film_id
    and fa1.actor_id = a1.actor_id
    and fa2.actor_id = a2.actor_id
                );

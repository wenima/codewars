-- Solution to codewars kata http://www.codewars.com/kata/challenge-two-actors-who-cast-together-the-most

-- get fist and second actor co-starring the most together
SELECT tp.actor_id, fa.actor_id as co-star, count(fa.actor_id) as starts
FROM film_actor fa, film_actor tp
WHERE fa.film_id = tp.film_id
AND fa.actor_id <> tp.actor_id
GROUP BY tp.actor_id, fa.actor_id
order by starts DESC, tp.actor_id;

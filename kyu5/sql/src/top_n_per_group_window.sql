--- Solution for example database dvdrental
WITH film_categories AS (select f.title, c.name, count(r.rental_id) as cnt,
dense_rank() OVER (PARTITION BY c.name ORDER BY count(r.rental_id) DESC) as rnk
from film_category fc
JOIN category c ON fc.category_id = c.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title, c.name)

SELECT * from film_categories where rnk <= 2
ORDER BY cnt DESC;

--- Solution for https://www.codewars.com/kata/using-window-functions-to-get-top-n-per-group
WITH posts_per_category AS (select c.id as category_id, c.category, p.title,
p.views as views, p.id as post_id,
rank() OVER (PARTITION BY p.category_id ORDER BY p.views DESC, p.id) as rnk
from categories c
LEFT JOIN posts p ON c.id = p.category_id
GROUP BY c.id, c.category, p.title, p.id)

SELECT category_id, category, title, views, post_id
FROM posts_per_category
WHERE rnk <= 2
ORDER BY category, views DESC, post_id;

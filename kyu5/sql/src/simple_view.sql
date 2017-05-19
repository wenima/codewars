-- Solution to codewars kata https://www.codewars.com/kata/sql-basics-simple-view/sql

CREATE VIEW members_approved_for_voucher AS
SELECT m.id, m.name, m.email, SUM(p.price) as total_spending
FROM members m, sales s, products p
WHERE m.id = s.member_id
AND s.product_id = p.id
AND s.department_id IN (
    SELECT s.department_id
    FROM products p, sales s
    WHERE s.product_id = p.id
    GROUP BY s.department_id
    HAVING SUM(p.price) > 10000
)
GROUP BY m.id
HAVING SUM(p.price) > 1000
ORDER BY m.id;

SELECT * from members_approved_for_voucher;

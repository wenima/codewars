-- Solution to codewars kata https://www.codewars.com/kata/sql-tuning-function-calls/

-- starting sql statement to be tuned:
SELECT e.employee_id,
        e.first_name,
        e.last_name,
        d.department_name,
        e.salary AS old_salary,
        e.salary * (1 + pctIncrease(e.department_id)) AS new_salary
   FROM employees   e,
        departments d
  WHERE e.department_id = d.department_id
  AND e.salary = 0
  ORDER BY 1



  -- starting sql statement to be tuned:

-- create tmp_table for increase of salary per department so we don't call the function for every employee

CREATE TEMP TABLE department (
  department_id integer,
  department_name text,
  increase decimal
);

INSERT INTO department SELECT
department_id, department_name, pctIncrease(department_id) as increase
FROM departments;

SELECT e.employee_id,
        e.first_name,
        e.last_name,
        d.department_name,
        e.salary AS old_salary,
        e.salary * 1 + d.increase AS new_salary
   FROM employees   e,
        department d
  WHERE e.department_id = d.department_id
  ORDER BY 1


  -- using subquery

  SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name,
       e.salary AS old_salary,
       e.salary * d.pctinc AS new_salary
  FROM employees   e,
       (SELECT department_id,
               department_name,
               1 + pctIncrease(department_id) pctinc
          FROM departments) d
 WHERE e.department_id = d.department_id
 ORDER BY 1;


 -- using CTE

 WITH CTE AS (SELECT d.department_id
                   ,d.department_name
                   ,pctIncrease(d.department_id) as IncrecasePercentage
             FROM departments d)



SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name,
       e.salary AS old_salary,
       e.salary * (1 + d.IncrecasePercentage) AS new_salary
  FROM employees   e
       INNER JOIN CTE d ON e.department_id = d.department_id
  ORDER BY 1;

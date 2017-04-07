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

  

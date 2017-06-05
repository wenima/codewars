--- Solution https://www.codewars.com/kata/sql-data-company-data-totals-per-day/
-- simple solution assuming company doesn't have shift going into next day
select
  sum(date_part('hour', age(t.logout, t.login))) as total_hours,
  d.name as department_name,
  t.login::date as day
from timesheet t
join department d
on t.department_id = d.id
group by 1, 2
order by 1, 2

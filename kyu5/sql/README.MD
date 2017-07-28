# Summary

this repository includes all of my completed code-katas from the
[CodeWars SQL challenges](http://wwww.codewars.com) with a difficulty of
kyu5 or higher. [History of the term kyu](https://en.wikipedia.org/wiki/Ky%C5%AB)

# SQL coding challenges:

## kyu5

* SQL Tuning: Function Calls
* Simple Hierarchical structure
* Simple PIVOTING data
* Simple View
* Group By Day
* Relational Division
* Calculating Running Total

## beta

* Using Window Functions To Get Top N per Group
* SQL Data: Company Data - totals per day
* Count Weekdays

## Details for each kata completed

### SQL Tuning: Function Calls
* Description of Kata: Your objective in this kata is to optimize this query.
The success criteria is to manage to run the query within the allowed kata
solution time window (12 seconds for SQL katas).
* Difficulty: kyu5
* Module: efficient_salary_increase.sql
* [Link](https://www.codewars.com/kata/sql-tuning-function-calls/)

### Simple Hierarchical structure
* Description of Kata: For this challenge you need to create a RECURSIVE Hierarchical query
* Difficulty: kyu5
* Module: hierachical_structure.sql
* [Link](https://www.codewars.com/kata/sql-basics-simple-hierarchical-structure/sql)

### Simple PIVOTING data
* Description of Kata: For this challenge you need to PIVOT data using crosstab.
* Difficulty: kyu5
* Module: pivot.sql
* [Link](https://www.codewars.com/kata/sql-basics-simple-pivoting-data/sql)

### Simple View
* Description of Kata: Create a simple view
* Difficulty: kyu5
* Module: simple_view.sql
* [Link](https://www.codewars.com/kata/sql-basics-simple-view/sql)

### SQL Statistics: MIN, MEDIAN, MAX
* Description of Kata: SQL Statistics: Your task is to calculate the MIN, MEDIAN
and MAX scores of the students from the results table.
* Difficulty: kyu5
* Module: min_median_max.sql
* [Link](https://www.codewars.com/kata/sql-statistics-min-median-max/sql)

### Group By Day
* Description of Kata: There is an events table used to track different key
activities taken on a website. For this task you need to filter the name field
to only show "trained" events. Events should be grouped by the day they happened
and counted. The description field is used to distinguish which items the events
happened on.
* Difficulty: kyu5
* Module: group_by_day.sql
* [Link](https://www.codewars.com/kata/sql-basics-group-by-day/sql)

### Relational Divison
* Description of Kata: Given film_actor and film tables from the DVD Rental sample
database find all movies both Sidney Crowe (actor_id = 105) and Salma Nolte
(actor_id = 122) cast in together and order the result set alphabetically.
* Difficulty: kyu5
* Module: relational_division_of_actors.sql
* [Link](https://www.codewars.com/kata/relational-division-find-all-movies-two-actors-cast-in-together/sql)

### Calculating Running Total
* Description of Kata: Given a posts table that contains a created_at timestamp
column write a query that returns date (without time component), a number of
posts for a given date and a running (cumulative) total number of posts up until
a given date
* Difficulty: kyu5
* Module: running_total.sql
* [Link](https://www.codewars.com/kata/calculating-running-total/)

### Using Window Functions To Get Top N per Group
* Description of Kata: Given the schema presented below write a query, which
uses a window function, that returns two most viewed posts for every category.
* Difficulty: beta
* Module: top_n_per_group_window.sql
* [Link](https://www.codewars.com/kata/using-window-functions-to-get-top-n-per-group)

### SQL Data: Company Data - totals per day
* Description of Kata: Your task is simple, given the data you must calculate
on each day how many hours have been clocked up for each department.
* Difficulty: beta
* Module: time_clocked.sql
* [Link](https://www.codewars.com/kata/sql-data-company-data-totals-per-day/)

### Count Weekdays
* Description of Kata: You need to create a function that calculates the number
of weekdays (Monday through Friday) between two dates inclusively.
The function should be named weekdays accept two arguments of type DATE and return
an INTEGER value. The order of arguments shouldn't matter.
* Difficulty: beta
* Module: weekdays_function.sql
* [Link](https://www.codewars.com/kata/count-weekdays/sql)
* Comments: using least/greatest to get the dates in the right order and generating
a series of days and then filtering on days which are not in 0 and 6.

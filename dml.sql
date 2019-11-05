--How many cities appeared more than twice in your results table?
SELECT city, count(*)
FROM results
GROUP BY city
ORDER BY count(*) DESC


SELECT
   DISTINCT created_at
FROM
   results;

SELECT
  a.animal_id,
  a.name
FROM
  animal_ins AS a
  JOIN animal_outs AS b ON a.animal_id = b.animal_id
ORDER BY
  DATEDIFF(b.datetime, a.datetime) DESC
LIMIT
  2;
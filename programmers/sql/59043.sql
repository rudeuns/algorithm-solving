SELECT
  a.animal_id,
  a.name
FROM
  animal_ins AS a
  JOIN animal_outs AS b ON a.animal_id = b.animal_id
WHERE
  a.datetime > b.datetime
ORDER BY
  a.datetime;
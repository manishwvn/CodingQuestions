SELECT
    t1.user_id,
    t1.steps_date,
    ROUND((t1.steps_count + t2.steps_count + t3.steps_count) / 3.0, 2) AS rolling_average
FROM
    Steps t1
JOIN
    Steps t2 ON t1.user_id = t2.user_id AND t1.steps_date = t2.steps_date + INTERVAL '1' DAY
JOIN
    Steps t3 ON t1.user_id = t3.user_id AND t2.steps_date = t3.steps_date + INTERVAL '1' DAY
ORDER BY
    t1.user_id, t1.steps_date;
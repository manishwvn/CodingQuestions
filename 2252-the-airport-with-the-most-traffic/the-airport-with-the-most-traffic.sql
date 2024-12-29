WITH departcount AS (
    SELECT
        departure_airport AS airport_id,
        SUM(flights_count) AS departs
    FROM
        flights
    GROUP BY
        1
),
arrivecount AS (
    SELECT
        arrival_airport AS airport_id,
        SUM(flights_count) AS arrives
    FROM
        flights
    GROUP BY
        1
),
airport_traffic AS ( -- New CTE to combine and calculate total traffic
SELECT
    COALESCE(d.airport_id, a.airport_id) AS airport_id,
    COALESCE(d.departs, 0) + COALESCE(a.arrives, 0) AS total_traffic
FROM
    departcount d
LEFT JOIN
    arrivecount a ON d.airport_id = a.airport_id
UNION ALL
SELECT
    COALESCE(d.airport_id, a.airport_id) AS airport_id,
    COALESCE(d.departs, 0) + COALESCE(a.arrives, 0) AS total_traffic
FROM
    departcount d
RIGHT JOIN
    arrivecount a ON d.airport_id = a.airport_id
WHERE d.airport_id IS NULL
)
SELECT airport_id
FROM airport_traffic
WHERE total_traffic = (SELECT MAX(total_traffic) FROM airport_traffic); -- Filter for max traffic
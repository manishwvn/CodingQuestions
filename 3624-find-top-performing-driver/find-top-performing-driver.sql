WITH cte AS (
    SELECT
        v.fuel_type,
        d.driver_id,
        ROUND(AVG(t.rating), 2) AS rating,
        SUM(t.distance) AS distance,
        DENSE_RANK() OVER (
            PARTITION BY v.fuel_type
            ORDER BY ROUND(AVG(t.rating), 2) DESC, SUM(t.distance) DESC, d.accidents ASC
        ) AS rnk
    FROM
        trips t
    LEFT JOIN
        vehicles v ON t.vehicle_id = v.vehicle_id
    JOIN
        drivers d ON v.driver_id = d.driver_id
    GROUP BY
        v.fuel_type, d.driver_id
)

SELECT
    fuel_type,
    driver_id,
    rating,
    distance
FROM
    cte
WHERE
    rnk = 1
ORDER BY
    fuel_type;
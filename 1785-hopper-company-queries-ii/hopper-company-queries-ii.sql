WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
),

active_drivers AS (
    SELECT 
        driver_id,
        CASE 
            WHEN YEAR(join_date) < 2020 THEN 1 
            ELSE MONTH(join_date) 
        END AS start_month
    FROM Drivers
    WHERE YEAR(join_date) <= 2020
),

accepted_rides AS (
    SELECT 
        MONTH(r.requested_at) AS month,
        a.driver_id
    FROM AcceptedRides a
    JOIN Rides r ON a.ride_id = r.ride_id
    WHERE YEAR(r.requested_at) = 2020
)

SELECT 
    m.month,
    ROUND(
        COALESCE(
            CASE 
                WHEN COUNT(DISTINCT ad.driver_id) = 0 THEN NULL
                ELSE COUNT(DISTINCT ar.driver_id) * 100.0 / COUNT(DISTINCT ad.driver_id)
            END,
        0), 2) AS working_percentage
FROM months m
LEFT JOIN active_drivers ad ON ad.start_month <= m.month
LEFT JOIN accepted_rides ar ON ar.month = m.month
GROUP BY m.month
ORDER BY m.month;
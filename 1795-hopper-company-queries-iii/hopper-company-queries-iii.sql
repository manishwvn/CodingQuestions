-- This CTE generates the 10 starting months for our 3-month windows.
WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 10
),
-- This CTE prepares the raw ride data for the year 2020.
Rides2020 AS (
    SELECT
        MONTH(r.requested_at) AS ride_month,
        ar.ride_distance,
        ar.ride_duration
    FROM
        Rides r
    JOIN
        AcceptedRides ar ON r.ride_id = ar.ride_id
    WHERE
        YEAR(r.requested_at) = 2020
)
-- Main query to calculate the rolling averages
SELECT
    m.month,
    ROUND(
        -- Use COALESCE to handle windows with no rides, turning a NULL sum into 0.
        COALESCE(SUM(r.ride_distance), 0) / 3.0,
        2
    ) AS average_ride_distance,
    ROUND(
        COALESCE(SUM(r.ride_duration), 0) / 3.0,
        2
    ) AS average_ride_duration
FROM
    -- Start FROM our complete list of months to ensure none are missed.
    Months m
LEFT JOIN
    -- Join ride data if the ride's month falls within the 3-month window.
    Rides2020 r ON r.ride_month BETWEEN m.month AND (m.month + 2)
GROUP BY
    m.month
ORDER BY
    m.month;
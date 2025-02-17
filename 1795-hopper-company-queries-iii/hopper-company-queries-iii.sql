WITH RECURSIVE Months AS (
    SELECT 1 AS month_num
    UNION ALL
    SELECT month_num + 1
    FROM Months
    WHERE month_num < 10
),
RideData AS (
    SELECT
        month(r.requested_at) AS ride_month,
        ar.ride_distance,
        ar.ride_duration
    FROM
        Rides r
    JOIN
        AcceptedRides ar ON r.ride_id = ar.ride_id
    WHERE YEAR(r.requested_at) = 2020
),
MonthlyAverages AS (
    SELECT
        m.month_num,
        SUM(CASE WHEN rd.ride_month BETWEEN m.month_num AND m.month_num + 2 THEN rd.ride_distance ELSE 0 END) AS total_distance,
        SUM(CASE WHEN rd.ride_month BETWEEN m.month_num AND m.month_num + 2 THEN rd.ride_duration ELSE 0 END) AS total_duration
    FROM
        Months m
    LEFT JOIN
        RideData rd ON 1=1  -- All rows from RideData should be considered
    GROUP BY
        m.month_num
)
SELECT
    month_num AS month,
    ROUND(total_distance / 3.0, 2) AS average_ride_distance,
    ROUND(total_duration / 3.0, 2) AS average_ride_duration
FROM
    MonthlyAverages
ORDER BY
    month;
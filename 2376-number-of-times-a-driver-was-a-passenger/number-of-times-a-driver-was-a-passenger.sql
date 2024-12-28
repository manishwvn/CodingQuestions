# Write your MySQL query statement below
WITH drivers AS(
    SELECT DISTINCT driver_id 
    FROM Rides
)
SELECT d.driver_id, COUNT(ride_id) AS cnt
FROM drivers d
LEFT JOIN Rides r ON d.driver_id = r.passenger_id
GROUP BY d.driver_id
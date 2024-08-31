SELECT 
    COALESCE(
        ROUND(
            CASE 
                WHEN COUNT(DISTINCT user_id) = 0 THEN 0
                ELSE COUNT(DISTINCT session_id) * 1.0 / COUNT(DISTINCT user_id)
            END, 
        2), 
    0.00) AS average_sessions_per_user
FROM 
    Activity 
WHERE activity_date:: DATE BETWEEN '2019-07-28'::DATE - INTERVAL '30 day' 
AND '2019-07-27'::DATE
WITH total_friend_requests AS (
    SELECT COUNT(*) AS total_count 
    FROM (
        SELECT DISTINCT sender_id, send_to_id 
        FROM FriendRequest
    ) AS distinct_requests
),
total_accepted_requests AS (
    SELECT COUNT(*) AS accept_count 
    FROM (
        SELECT DISTINCT requester_id, accepter_id 
        FROM RequestAccepted
    ) AS distinct_acceptances
)
SELECT 
    CASE 
        WHEN (SELECT total_count FROM total_friend_requests) = 0 THEN 0.00
        ELSE ROUND(
            (SELECT accept_count FROM total_accepted_requests)::DECIMAL /
            (SELECT total_count FROM total_friend_requests), 2
        )
    END AS accept_rate;
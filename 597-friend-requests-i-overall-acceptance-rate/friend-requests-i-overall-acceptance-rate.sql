SELECT 
    CASE 
        WHEN (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS req) = 0 THEN 0.00
        ELSE ROUND(
            (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS acc)::DECIMAL /
            (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS req), 2
        )
    END AS accept_rate;
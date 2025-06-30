SELECT
    ROUND(
        CASE
            -- First, check if the denominator is zero
            WHEN (SELECT COUNT(DISTINCT sender_id, send_to_id) FROM FriendRequest) = 0
            THEN 0.00
            -- If it's not zero, perform the division
            ELSE
                CAST((SELECT COUNT(DISTINCT requester_id, accepter_id) FROM RequestAccepted) AS FLOAT)
                /
                (SELECT COUNT(DISTINCT sender_id, send_to_id) FROM FriendRequest)
        END
    , 2) AS accept_rate;
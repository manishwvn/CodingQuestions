WITH t1 AS (
    SELECT
        user1_id user_id,
        user2_id friend_id
    FROM
        Friendship
    UNION
    SELECT
        user2_id user_id,
        user1_id friend_id
    FROM
        Friendship
)
SELECT
    t1.user_id,
    l1.page_id,
    COUNT(1) friends_likes
FROM
    t1
JOIN
    Likes l1
ON
    t1.friend_id = l1.user_id
LEFT JOIN
    Likes l2
ON
    t1.user_id = l2.user_id
AND
    l2.page_id = l1.page_id
WHERE
    l2.page_id IS NULL
GROUP BY
    t1.user_id,
    l1.page_id

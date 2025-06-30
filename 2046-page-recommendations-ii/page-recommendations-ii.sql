-- Step 1: Create the bidirectional friend list. This is the correct first step.
WITH Friends AS (
    SELECT user1_id, user2_id FROM Friendship
    UNION
    SELECT user2_id, user1_id FROM Friendship
)
-- Step 2: Join friends to the pages they like, filter, and aggregate in one step.
SELECT
    f.user1_id AS user_id,
    l.page_id,
    COUNT(*) AS friends_likes
FROM
    Friends f
JOIN
    Likes l ON f.user2_id = l.user_id -- Find pages liked by the friend (f.user2_id)
LEFT JOIN
    -- Use an ANTI-JOIN to check if the user (f.user1_id) already likes the page
    Likes user_likes ON f.user1_id = user_likes.user_id AND l.page_id = user_likes.page_id
WHERE
    -- This condition keeps only the rows where the user does NOT already like the page
    user_likes.user_id IS NULL
GROUP BY
    f.user1_id,
    l.page_id
ORDER BY
    f.user1_id,
    l.page_id;
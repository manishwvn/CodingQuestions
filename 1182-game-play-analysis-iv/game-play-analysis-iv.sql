WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login_date
    FROM
        activity
    GROUP BY
        player_id
),
RecurringPlayers AS (
    SELECT
        fl.player_id
    FROM
        FirstLogin fl
    JOIN
        activity a
    ON
        fl.player_id = a.player_id
    AND
        a.event_date = fl.first_login_date + INTERVAL 1 day
)

SELECT
    ROUND(
        COUNT(rp.player_id) / (
            SELECT COUNT(DISTINCT player_id)
            FROM activity
        ), 
        2
    ) AS fraction
FROM
    RecurringPlayers rp;
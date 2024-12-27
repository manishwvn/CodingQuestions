WITH Bins AS (
    SELECT '[0-5>' AS bin UNION ALL
    SELECT '[5-10>' AS bin UNION ALL
    SELECT '[10-15>' AS bin UNION ALL
    SELECT '15 or more' AS bin
)
SELECT
    b.bin,
    COALESCE(COUNT(s.session_id), 0) AS total
FROM
    Bins b
LEFT JOIN
    Sessions s ON
        CASE
            WHEN s.duration < 300 THEN '[0-5>'
            WHEN s.duration >= 300 AND s.duration < 600 THEN '[5-10>'
            WHEN s.duration >= 600 AND s.duration < 900 THEN '[10-15>'
            ELSE '15 or more'
        END = b.bin
GROUP BY
    b.bin;
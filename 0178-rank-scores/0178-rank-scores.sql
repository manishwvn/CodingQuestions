SELECT
    S.SCORE, 
    COUNT(DISTINCT T.SCORE) AS 'rank'
FROM
    SCORES S
JOIN
    SCORES T
ON 
    S.SCORE <= T.SCORE
GROUP BY
    S.ID,
    S.SCORE
ORDER BY
    1 DESC;
SELECT
    S.SCORE, 
    DENSE_RANK() OVER (ORDER BY S.SCORE DESC) AS 'rank'
FROM
    SCORES S
ORDER BY
    1 DESC;
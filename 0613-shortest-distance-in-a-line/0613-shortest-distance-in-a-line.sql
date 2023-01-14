SELECT
    MIN(T.DIST) AS 'shortest'
FROM 
    (SELECT 
        ABS(A.X - B.X) AS DIST 
        FROM POINT A
        INNER JOIN
        POINT B
        ON A.X <> B.X
        ) AS T;
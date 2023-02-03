-- USING CASE

SELECT 
    ID AS 'id',
    CASE
        WHEN P_ID IS NULL THEN 'Root'
        WHEN ID IN (SELECT P_ID FROM TREE) THEN 'Inner'
        ELSE 'Leaf'
    END AS 'Type'
FROM
    TREE
ORDER BY
    1;
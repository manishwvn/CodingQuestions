SELECT
    NAME AS 'name'
FROM 
    SALESPERSON
WHERE 
    SALES_ID NOT IN (
        SELECT SALES_ID 
        FROM ORDERS O
        JOIN COMPANY C 
        ON O.COM_ID = C.COM_ID
        WHERE C.NAME = 'RED');
SELECT 
    COUNT(DISTINCT CUSTOMER_ID) AS 'rich_count'
FROM 
    STORE
WHERE
    AMOUNT > 500;
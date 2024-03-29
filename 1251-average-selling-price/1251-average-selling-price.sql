SELECT DISTINCT
    P.PRODUCT_ID AS 'product_id', 
    ROUND(SUM(U.UNITS*P.PRICE)/SUM(U.UNITS), 2) AS 'average_price'
    
    
FROM 
    PRICES P
INNER JOIN
    UNITSSOLD U
ON
    P.PRODUCT_ID = U.PRODUCT_ID
WHERE
    U.PURCHASE_DATE BETWEEN P.START_DATE AND P.END_DATE
GROUP BY
    P.PRODUCT_ID;
    
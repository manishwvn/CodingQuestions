SELECT
    DATE_FORMAT(ORDER_DATE, '%Y-%m') as 'month',
    COUNT(DISTINCT ORDER_ID) AS 'order_count',
    COUNT(DISTINCT CUSTOMER_ID) AS 'customer_count'    
FROM
    ORDERS
WHERE
    INVOICE > 20
GROUP BY
    month;

    
    
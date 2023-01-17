SELECT
    SALE_DATE AS 'sale_date',
    SUM(CASE 
        WHEN FRUIT = 'apples' THEN SOLD_NUM 
        WHEN FRUIT = 'oranges' THEN -SOLD_NUM ELSE 0 END) 
    AS 'diff'
    
FROM
    SALES

GROUP BY
    SALE_DATE;
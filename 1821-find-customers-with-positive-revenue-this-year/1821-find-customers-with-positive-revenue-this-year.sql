SELECT
    CUSTOMER_ID AS 'customer_id'
FROM
    CUSTOMERS
WHERE
    YEAR = '2021' AND REVENUE > 0
ORDER BY
    CUSTOMER_ID;
    
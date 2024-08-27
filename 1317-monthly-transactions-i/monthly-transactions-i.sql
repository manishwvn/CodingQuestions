SELECT
    TO_CHAR(TRANS_DATE, 'YYYY-MM') AS month,
    COUNTRY,
    COUNT(*) as trans_count,
    SUM(CASE WHEN STATE = 'approved' THEN 1 ELSE 0 END) as approved_count,
    SUM(AMOUNT) AS trans_total_amount,
    SUM(CASE WHEN STATE = 'approved' THEN AMOUNT ELSE 0 END) as approved_total_amount
FROM
    TRANSACTIONS
GROUP BY MONTH, COUNTRY
ORDER BY 1,2;
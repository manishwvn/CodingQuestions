SELECT
    DATE_FORMAT(TRANS_DATE, '%Y-%m') AS 'month',
    COUNTRY AS 'country',
    COUNT(STATE) AS 'trans_count',
    COUNT(CASE WHEN STATE = 'approved' THEN 1 ELSE NULL END) AS 'approved_count',
    SUM(AMOUNT) AS 'trans_total_amount',
    SUM(CASE WHEN STATE = 'approved' THEN AMOUNT ELSE 0 END) AS 'approved_total_amount'
    
FROM
    TRANSACTIONS
GROUP BY
    1, 2;
    
    
    
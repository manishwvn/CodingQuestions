SELECT 
    CUSTOMER_ID,
    COUNT(V.VISIT_ID) AS count_no_trans
FROM 
    VISITS AS V
LEFT JOIN 
    TRANSACTIONS T
ON 
    V.VISIT_ID = T.VISIT_ID
WHERE
    T.VISIT_ID IS NULL
GROUP BY 
    V.CUSTOMER_ID;


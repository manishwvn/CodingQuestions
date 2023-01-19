SELECT
    QUERY_NAME AS 'query_name',
    ROUND(AVG((RATING) / (POSITION)), 2) AS 'quality',
    ROUND(AVG(RATING < 3)*100, 2) AS 'poor_query_percentage'
    
FROM
    QUERIES
    

GROUP BY
    QUERY_NAME;


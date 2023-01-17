SELECT
    QUERY_NAME AS 'query_name',
    ROUND(AVG((RATING) / (POSITION)), 2) AS 'quality',
    ROUND((((
        COUNT(
             CASE WHEN RATING < 3 
             THEN RATING 
             ELSE NULL 
             END)) / 
             (COUNT(RATING))) * 100), 2)
    AS 'poor_query_percentage'
    
FROM
    QUERIES

GROUP BY
    QUERY_NAME;


# SELECT
#     COUNT(CASE WHEN RATING < 3 THEN RATING ELSE NULL END)
# FROM
#     QUERIES;
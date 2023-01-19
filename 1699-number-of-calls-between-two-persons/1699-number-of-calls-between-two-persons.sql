SELECT
    IF(FROM_ID < TO_ID, FROM_ID, TO_ID) AS 'person1',
    IF(FROM_ID < TO_ID, TO_ID, FROM_ID) AS 'person2',
    COUNT(*) AS 'call_count',
    SUM(DURATION) AS 'total_duration'
FROM
    CALLS
GROUP BY 
    1, 2;
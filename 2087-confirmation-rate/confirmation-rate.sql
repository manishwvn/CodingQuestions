SELECT
    S.USER_ID,
    ROUND(AVG(CASE WHEN C.ACTION = 'confirmed' then 1 else 0 end), 2)
        as confirmation_rate
FROM
    SIGNUPS S
LEFT JOIN
    CONFIRMATIONS C
ON
    S.USER_ID = C.USER_ID
GROUP BY S.USER_ID;
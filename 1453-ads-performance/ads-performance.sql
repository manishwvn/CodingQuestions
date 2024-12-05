SELECT
    ad_id,
    ROUND(
        IFNULL(
            (SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) / 
            (SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) + 
             SUM(CASE WHEN action = 'Viewed' THEN 1 ELSE 0 END))), 
        0) * 100, 2
    ) AS ctr
FROM
    ads
GROUP BY
    ad_id
ORDER BY
    ctr DESC,
    ad_id ASC;
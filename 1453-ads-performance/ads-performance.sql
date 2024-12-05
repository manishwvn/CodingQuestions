WITH ad_clicks AS (
    SELECT
        ad_id,
        COUNT(*) AS count_clicks
    FROM
        ads
    WHERE
        action = 'Clicked'
    GROUP BY
        ad_id
),
ad_views AS (
    SELECT
        ad_id,
        COUNT(*) AS count_views
    FROM
        ads
    WHERE
        action = 'Viewed'
    GROUP BY
        ad_id
)
SELECT
    a.ad_id,
    CASE
        WHEN IFNULL(ad_clicks.count_clicks, 0) + IFNULL(ad_views.count_views, 0) = 0 THEN 0.00
        ELSE ROUND(IFNULL(ad_clicks.count_clicks, 0) / (IFNULL(ad_clicks.count_clicks, 0) + IFNULL(ad_views.count_views, 0)), 4) * 100
    END AS ctr
FROM
    (SELECT DISTINCT ad_id FROM ads) a -- Corrected base table
LEFT JOIN
    ad_clicks
ON
    a.ad_id = ad_clicks.ad_id
LEFT JOIN
    ad_views
ON
    a.ad_id = ad_views.ad_id
ORDER BY
    ctr DESC,
    a.ad_id ASC;
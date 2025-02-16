WITH cte AS (
    SELECT
        o.seller_id,
        i.item_brand,
        o.order_date
    FROM orders o
    JOIN items i ON o.item_id = i.item_id
),
cte2 AS (
    SELECT
        u.user_id AS seller_id,
        u.favorite_brand,
        c.item_brand,
        DENSE_RANK() OVER (PARTITION BY u.user_id ORDER BY c.order_date) AS rnk,
        COUNT(c.seller_id) OVER (PARTITION BY u.user_id) AS trans
    FROM users u
    LEFT JOIN cte c ON u.user_id = c.seller_id
)
SELECT
    seller_id,
    CASE 
        WHEN trans < 2 THEN 'no'
        WHEN rnk = 2 AND favorite_brand = item_brand THEN 'yes'
        ELSE 'no'
    END AS 2nd_item_fav_brand
FROM cte2
WHERE rnk = 2 OR trans < 2;
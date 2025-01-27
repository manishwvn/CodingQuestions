WITH upd_prices AS (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    FROM
        products
    WHERE
        change_date <= DATE('2019-08-16')
)
SELECT
    p.product_id,
    COALESCE(up.new_price, 10) AS price
FROM
    products p
LEFT JOIN
    upd_prices up
ON
    p.product_id = up.product_id AND up.rnk = 1
GROUP BY
    p.product_id, up.new_price;
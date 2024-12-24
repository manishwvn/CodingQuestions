SELECT DISTINCT s.buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
AND p.product_name = 'S8'
AND s.buyer_id NOT IN
(
    SELECT DISTINCT buyer_id
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
    AND p.product_name = 'iPhone'
    )